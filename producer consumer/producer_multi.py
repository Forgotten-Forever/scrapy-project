"""
.--,       .--,
 ( (  \.---./  ) )
  '.__/o   o\__.'
     {=  ^  =}
      >  -  <
     /       \
    //       \\
   //|   .   |\\
   "'\       /'"_.-~^`'-.
      \  _  /--'         `
    ___)( )(___
   (((__) (__)))    高山仰止,景行行止.虽不能至,心向往之。
"""
import threading
import requests
import pymongo
from queue import Queue

"""
实例
对象
类
一个实例化 --> 对象 (类的实例化)
__new__() --> 创建类
__init__() --> 创建对象
"""


class TencentData(threading.Thread):

	def __init__(self, q_page, crawl):
		super().__init__()
		self.base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1605322197637&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
		self.q_page = q_page
		self.name = crawl
		# 创建链接
		self.client = pymongo.MongoClient()
		# 创建数据库
		self.db = self.client['tencent_data']

	def get_json(self, url):
		"""
			获取 JSON 数据
			"""
		headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
			'cookie': '_ga=GA1.2.977222291.1597654741; pgv_pvi=170857472; _gcl_au=1.1.1099538350.1597654742; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22fd640ff343d78439d2faaa261bce126c%40devS%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22173fba4aea4444-0c8760db5362df-3323765-1327104-173fba4aea5c30%22%7D; loading=agree',
			'referer': 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index=2',
		}
		response = requests.get(url, headers=headers)
		return response.json()

	def write_to_mongo(self, item):
		"""
		导入 mongo
		"""
		self.db["招聘信息"].update({"PostId": item['PostId']}, {'$set': item}, True)
		print(item)

	def get_page_data(self, i):
		# 获取 json 数据
		json_data = self.get_json(self.base_url.format(i))
		for data in json_data['Data']['Posts']:
			pass

	def run(self):
		while True:
			if self.q_page.empty():
				break
			# 获取一个页码
			page = self.q_page.get()
			print(f"开始爬取第 {page} 页 @ {self.name}")
			self.get_page_data(page)


if __name__ == '__main__':
	# 创建一个队列, 初始化任务队列
	q_page = Queue()
	for i in range(1, 101):
		q_page.put(i)
	# 创建 list
	crawl_list = ["Data_A", "Data_B", "Data_C", "Data_D"]
	# 循环 list 开启多线程
	for crawl in crawl_list:
		t = TencentData(q_page, crawl)
		t.start()