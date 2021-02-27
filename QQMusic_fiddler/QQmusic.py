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
"""
https://isure.stream.qqmusic.qq.com/C400003sIpH04C5Bch.m4a?
		guid=606146752&
		vkey=787D813239970DCCED046CFE3E716EDEA2B454DF7A06F91E92204DEBCF73FAFFE5CE76D75FBE10CB926E0AC8CC44D6173159E46AE2A5D12E&
		uin=0&
		fromtag=66
guid: 606146752
vkey: 787D813239970DCCED046CFE3E716EDEA2B454DF7A06F91E92204DEBCF73FAFFE5CE76D75FBE10CB926E0AC8CC44D6173159E46AE2A5D12E
uin: 0
fromtag: 66
//  搜索 vkey 得到可能有用信息
url : https://u.y.qq.com/cgi-bin/musics.fcg?
参数		-: getplaysongvkey4857823391872029
		g_tk: 5381
		sign: zzaugmi8hzfzjkum5i9820abaa5657f306676243f3e31d0ba5
		loginUin: 0
		hostUin: 0
		format: json
		inCharset: utf8
		outCharset: utf-8
		notice: 0
		platform: yqq.json
		needNewCode: 0
		data: {"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"606146752","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"606146752","songmid":["003sIpH04C5Bch"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}
filename: C400003sIpH04C5Bch.m4a
purl : "C400003sIpH04C5Bch.m4a?
		guid=606146752&
		vkey=787D813239970DCCED046CFE3E716EDEA2B454DF7A06F91E92204DEBCF73FAFFE5CE76D75FBE10CB926E0AC8CC44D6173159E46AE2A5D12E&
		uin=0&
		fromtag=66"
songmid :   "003sIpH04C5Bch"
vkey : "787D813239970DCCED046CFE3E716EDEA2B454DF7A06F91E92204DEBCF73FAFFE5CE76D75FBE10CB926E0AC8CC44D6173159E46AE2A5D12E"
////
https://u.y.qq.com/cgi-bin/musics.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%22606146752%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22606146752%22%2C%22songmid%22%3A%5B%22003J99IP14XeZC%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
https://u.y.qq.com/cgi-bin/musics.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%22606146752%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A+%7B%22guid%22%3A%22606146752%22%2C%22songmid%22%3A%5B%22004DAuTp2dXb2q%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A+%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
"""
import requests
from multiprocessing.pool import Pool


class QQMusic(object):
	def __init__(self, guid):
		# 公共变量
		self.guid = guid
		self.vkeys_headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
			              'Chrome/86.0.4240.111 Safari/537.36',
			'origin':'https://y.qq.com',
			'Referer': 'https://y.qq.com/',
			'Cookie': 'RK=YQTo4kDi4r; ptcz=2e643e79578d23f9172a0396beda81f4dc020d4974bb24caefdbb93c27781908; '
			          'tvfe_boss_uuid=1b8a1d5297f8cb6d; pgv_pvid=606146752; o_cookie=2985374516; pgv_pvi=8658309120; '
			          'LW_sid=v1h5v9Y6O976z078b0T0U1P983; LW_uid=v1Z5G9s609z6G0m8d0Z001S9l5; '
			          'eas_sid=D1I5W9H609N680l8M0v1N5G4S3; uin_cookie=o2985374516; ied_qq=o2985374516; '
			          '_qpsvr_localtk=1605091449181; pgv_info=ssid=s5154468592; pgv_si=s3880585216; '
			          'qqmusic_fromtag=66',
		}
		self.song_mid_headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
			              'Chrome/86.0.4240.111 Safari/537.36',
			'origin': 'https://y.qq.com',
			'referer': 'https://y.qq.com/',
			'cookie': 'RK=YQTo4kDi4r; ptcz=2e643e79578d23f9172a0396beda81f4dc020d4974bb24caefdbb93c27781908; '
			          'tvfe_boss_uuid=1b8a1d5297f8cb6d; pgv_pvid=606146752; o_cookie=2985374516; pgv_pvi=8658309120; '
			          'LW_sid=v1h5v9Y6O976z078b0T0U1P983; LW_uid=v1Z5G9s609z6G0m8d0Z001S9l5; '
			          'eas_sid=D1I5W9H609N680l8M0v1N5G4S3; uin_cookie=o2985374516; ied_qq=o2985374516; '
			          'ts_uid=2483393792; userAction=1; _qpsvr_localtk=1605091449181; pgv_info=ssid=s5154468592; '
			          'ts_refer=www.baidu.com/link; pgv_si=s3880585216; yqq_stat=0; player_exist=1; '
			          'qqmusic_fromtag=66; yplayer_open=1; ts_last=y.qq.com/n/yqq/playlist/7085583499.html; '
			          'yq_index=2',
		}
		self.download_headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
			              'Chrome/86.0.4240.111 Safari/537.36',
			'Referer': 'https://y.qq.com/',
			'Host': 'ws.stream.qqmusic.qq.com',
			'Cookies': 'K=YQTo4kDi4r; ptcz=2e643e79578d23f9172a0396beda81f4dc020d4974bb24caefdbb93c27781908; '
			           'tvfe_boss_uuid=1b8a1d5297f8cb6d; pgv_pvid=606146752; o_cookie=2985374516; pgv_pvi=8658309120; '
			           'LW_sid=v1h5v9Y6O976z078b0T0U1P983; LW_uid=v1Z5G9s609z6G0m8d0Z001S9l5; '
			           'eas_sid=D1I5W9H609N680l8M0v1N5G4S3; uin_cookie=o2985374516; ied_qq=o2985374516; '
			           '_qpsvr_localtk=1605091449181; pgv_info=ssid=s5154468592; pgv_si=s3880585216; '
			           'qqmusic_fromtag=66',
		}

	def get_song_mids(self, guid):
		"""
		通过歌单的id，获取所有歌单下面的songmid
		"""
		base_url = f"https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?" \
		           f"type=1&" \
		           f"json=1&" \
		           f"utf8=1&" \
		           f"onlysong=0&" \
		           f"new_format=1&" \
		           f"disstid={self.guid}&" \
		           f"g_tk_new_20200303=5381&" \
		           f"g_tk=5381&" \
		           f"loginUin=0&" \
		           f"hostUin=0&" \
		           f"format=json&" \
		           f"inCharset=utf8&" \
		           f"outCharset=utf-8&" \
		           f"notice=0&" \
		           f"platform=yqq.json&" \
		           f"needNewCode=0"
		response = requests.get(base_url, headers=self.song_mid_headers)
		song_infos = []
		for data in response.json()['cdlist'][0]['songlist']:
			name = data['name']
			mid = data['mid']
			song_infos.append((name, mid))
		# print(song_infos)
		return song_infos

	def get_song_purl(self, mid):
		base_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'
		params = {
			# '-': 'getplaysongvkey4857823391872029',
			'g_tk': '5381',
			# 'sign': 'zzaugmi8hzfzjkum5i9820abaa5657f306676243f3e31d0ba5',
			'loginUin': '0',
			'hostUin': '0',
			'format': 'json',
			'inCharset': 'utf8',
			'outCharset': 'utf-8',''
			'notice': '0',
			'platform': 'yqq.json',
			'needNewCode': '0',
			'data': '{"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"'+self.guid+'","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param": {"guid":"'+self.guid+'","songmid":["'+mid+'"],"songtype":[0],"uin":"0","loginflag":1,"platform": "20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'
		}
		response = requests.get(base_url, params=params, headers=self.vkeys_headers)
		# print(response.json())
		purl = response.json()['req_0']['data']['midurlinfo'][0]['purl']
		return purl

	def download_music(self, name, url):
		try:
			print("开始下载", name)
			full_url = 'https://isure.stream.qqmusic.qq.com/' + url
			response = requests.get(full_url, headers=self.download_headers)
			with open('./music/'+ name + '.m4a', 'wb') as fp:
				fp.write(response.content)
			print(name, '下载成功')
		except Exception as e:
			print(e)
			print(name, '下载失败')

	def download_music_by_mid(self, song_infos):
		name = song_infos[0]
		mid = song_infos[1]

		purl = self.get_song_purl(mid)
		self.download_music(name, purl)

	def run(self):
		# 通过 歌曲 mid 获取 所有歌单下的 songmid
		song_infos = self.get_song_mids(self.guid)
		# print(song_infos)
		p = Pool()
		p.map(self.download_music_by_mid, song_infos)
		# for name, mid in song_infos:
		# 	purl = self.get_song_purl(mid)
		# 	self.download_music(name, purl)


if __name__ == '__main__':
	guid = '606146752'
	QQMusic(guid).run()