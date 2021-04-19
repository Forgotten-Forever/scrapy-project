import scrapy
import pandas as pd
from ..items import WeatherItem


class ChinaWeatherSpider(scrapy.Spider):
    name = 'china_weather'
    # allowed_domains = ['www']
    start_urls = ["http://www.weather.com.cn/textFC/hb.shtml"]

    def parse(self, response):
        ul_list = response.xpath('//div[@class="lqcontentBoxH"]/div[@class="lqcontentBoxheader"]/ul')
        print("开始爬取")
        province_url_dir = {}
        for ul in ul_list:
            li_list = ul.xpath('.//li')
            for li in li_list:
                # 省份 URL
                province_urls = li.xpath('.//a/@href').extract()
                province_names = li.xpath('.//a/text()').extract()
                for province_name, province_url in zip(province_names, province_urls):
                    province_url = 'http://www.weather.com.cn' + province_url
                    # 省份 名称
                    province_url_dir[province_name] = province_url
                    yield scrapy.Request(province_url, callback=self.get_detail, encoding='utf-8')

    def get_detail(self, response):
        weather_infos = response.xpath('//div[@class="hanml"]/div')
        city = response.xpath('//div[@class="contentboxTab"]/h1/a[3]/text()').extract_first()
        # release_time = response.xpath('//div[@class="contentboxTab"]/h1/span/text()').extract_first().replace('\n', '')
        # print(release_time)
        # print(city)
        # 定义一个 空的 DF 存储天气信息
        weather_df = pd.DataFrame()
        for weather_info in weather_infos:
            # 获取页面中 所有天气信息表格
            tables = pd.read_html(weather_info.extract())
            # 提取 表头中的 日期信息
            day = tables[0].loc[0, 2].split('(')[1].split(')')[0]
            title = tables[0].iloc[:, :-1]
            # 建立一个空列表 用于将 tables 中所有 DF 进行上下合并 形成 一天 的 天气信息 DF
            empty_df = pd.DataFrame()
            for i in range(1, len(tables)):
                # 将表格合并
                empty_df = pd.concat([empty_df, tables[i].iloc[:, :-1]], axis=0, ignore_index=True, copy=True)
            empty_df = empty_df.loc[:, [0, 1, 2, 4, 7]]
            # 更改 表头 列名
            columns = {0: '市', 1: '区/县', 2: day+'天气现象', 4: day+'最高气温', 7: day+'最低气温'}
            empty_df.rename(columns=columns, inplace=True)
            # 生成一个和并表, 合并表内是每个表的 列名
            merge_col = [col for col in list(empty_df.columns) if col not in list(weather_df.columns)]
            # print(merge_col)
            # 合并 每天的天气表 将七天内 天气表合并为 一个 DF
            # 表头为 市  区/县 1月xx日天气现象 1月xx日最高气温 1月xx日最低气温 1月xx日天气现象 1月xx日最高气温 1月xx日最低气温 1月xx日天气现象 1月xx日最高气温 1月xx日最低气温 1月xx日天气现象 1月xx日最高气温 1月xx日最低气温 1月xx日天气现象 1月xx日最高气温 1月xx日最低气温 1月xx日天气现象       | 1月28日最高气温       | 1月28日最低气温       | 1月29日天气现象       | 1月29日最高气温       | 1月29日最低气温       |
            weather_df = pd.merge(weather_df, empty_df[merge_col], left_index=True, right_index=True, how='right')
        # weather_df.to_dict(orient='records')
        # print(weather_df)

        # 省份省会天气信息 DF
        provincial_capital = weather_df.iloc[:1, :].copy()
        columns = {'市': '省', '区/县': '省会'}
        provincial_capital.rename(columns=columns, inplace=True)
        provincial_capital.loc[:, "省"] = city
        # provincial_capital.to_dict(orient='records')
        # print(provincial_capital)

        item = WeatherItem()
        item['city'] = city
        item['weather_df'] = weather_df
        item['provincial_capital'] = provincial_capital
        yield item

