# -*- encoding: utf-8 -*-
import requests
import json
import time, datetime

github_url = "https://github.com/cocos-creator/engine/pulls"
headers = {"Accept": "application/vnd.github.v3+json"}


try:
	response = requests.get(url=github_url, headers=headers, timeout=10)
	if response.status_code == 200:
		print("页面(%s)访问成功(%s)" % (github_url, response.status_code))
		pulls = response.json()
		#return pulls
		print(pulls)
	else:
		print("页面(%s)访问失败(%s)" % (github_url, response.status_code))
except Exception as e:
	print("URL(%s) 请求失败(%s)" % (github_url, e))
