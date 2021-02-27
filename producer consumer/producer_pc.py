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


class Product(threading.Thread):

	def __init__(self, q_page):
		super().__init__()
		print("Product")
		self.base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1605322197637&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
		self.q_page = q_page

	def get_json(self, url):
		"""
		获取 JSON 数据
		"""
		headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
			'referer': 'https://careers.tencent.com/search.html',
		}
		response = requests.get(url, headers=headers)
		# print(response.text)
		return response.json()

	def main(self):
		# 1、确定url
		base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1605322197637&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
		for i in range(1, 101):
			# 获取json数据
			json_data = self.get_json(base_url.format(i))

	# for i in range(1, 101):
	# 	json_data = self.get_json(self.base_url.format(i))

	def run(self):
		while True:
			if self.q_page.empty():
				break
		# 获取一个页码
		page = self.q_page.get()
		print(page)
		# 获取该页面的 json 数据 -- json_data -- p生产的数据
		json_data = self.get_json(self.base_url.format(page))
		# 将 p 生产的数据放入到公共队列
		q_json_data.put(json_data)


class Consumer(threading.Thread):

	def __init__(self):
		super().__init__()
		print("Consumer")
		# 创建链接
		self.client = pymongo.MongoClient()
		# 连接数据库
		self.db = self.client["tencent_data"]

	def write_to_mongo(self, item):
		'''
        写入mongo
        :param item:
        :return:
        '''
		self.db['招聘信息'].update({'PostId': item['PostId']}, {'$set': item}, True)
		print(item['PostId'])

	def parse_data(self, json_data):
		for data in json_data['Data']['Posts']:
			self.write_to_mongo(data)

	def run(self):
		while True:
			# 难点1:消费者的停止条件
			# 公共池对象空了，但是消费者不一定要停止消费
			# p停止工作和公共池为空这两个条件同时满足，消费者才停止消费
			if q_json_data.empty() and flag == True:
				break
			try:
				# 难点2：需要将公共池队列get方法设置一个非阻塞，
				# 并使用try,except来式程序正常执行，不会卡死
				json_data = q_json_data.get(block=False)
				print(json_data)
				self.parse_data(json_data)
			except Exception:
				pass


if __name__ == '__main__':
	# 设置一个 p 和 c 的池
	q_json_data = Queue()
	# 轮询参数, 定义工作是否完成
	flag = False
	# 开启一个 p 的多线程
	# 开启一个任务队列
	q_page = Queue()
	# 初始化
	for i in range(1, 101):
		q_page.put(i)
	# 循环开启 p 的多线程
	crawl_p_list = []
	for i in range(4):
		print('ready')
		t_p = Product(q_page)
		t_p.start()
		crawl_p_list.append(t_p)

	# 开启c 的多线程
	# 循环开启消费者线程
	for i in range(3):
		print("c ready")
		t_c = Consumer()
		t_c.start()
	# 阻塞 当前主线程,询问 p 是否还在工作
	for crawl_p in crawl_p_list:
		crawl_p.join()
	# 工作完成
	flag = True
