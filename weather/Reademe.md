#### 爬虫功能 (暂定)

1. 爬取中国天气网上中国各地区 (精确到县区) 近七天天气信息，在数据库内实现更新操作，以省份为表名
2. 将各省省会信息单独存入一个数据表内，以  provincial_capital 为表名

##### 运行时修改

1. 提前创好数据库 **weather**
2. 修改 `/weather/weather/pipelines.py` 内的 `self.engine = create_engine('mysql+pymysql://数据库用户名:数据库密码@localhost/weather?charset=utf8')`
3. 运行时直接对 `weather/weather/spiders/main.py` 进行运行即可，不需要运行 scrapy 爬虫 命令

