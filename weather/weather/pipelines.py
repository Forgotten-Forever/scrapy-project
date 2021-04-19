# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class WeatherPipeline:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:root@localhost/weather?charset=utf8')
        # 创建链接
        self.Session_class = sessionmaker(bind=self.engine)
        # 生成实例
        self.Session = self.Session_class()

    def clear_capital(self):
        """
        由于 每次传递的省会信息都是一个独立的 DF 所以需要 append 存储，如果 省会表已经存在则会导致 append 是找不到对应列名
        通过原生 SQL 语句对 省会表进行删除
        """
        cmd_sql = "DROP TABLE provincial_capital"
        self.Session.execute(cmd_sql)
        self.Session.commit()
        self.Session.close()

    def process_item(self, item, spider):
        # weather = item["weather_df"].to_dict(orient='records')
        # 将各个省份近七天信息存储至 数据库中各个省份的表内，数据库表名为省份名
        # sql_cmd = f"SELECT * FROM {item['city']}"
        # old_df = pd.read_sql(sql=sql_cmd, con=self.engine)

        item["weather_df"].to_sql(item["city"], con=self.engine, if_exists='replace', index=False)
        # print(item["provincial_capital"])
        # 将所有省份省会近七天天气信息存储至 provincial_capital 表内 ，以 append 形式存储
        item["provincial_capital"].to_sql("provincial_capital", con=self.engine, if_exists='append', index=False)

        return item
