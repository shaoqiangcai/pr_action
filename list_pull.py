# -*- encoding: utf-8 -*-
import requests
import os
import json
import time, datetime
from githup import Github

github_url = "https://github.com/cocos-creator/engine/pulls"
github_url = "https://github.com/OperationsYU/pr_action/pulls"
headers = {"Accept": "application/vnd.github.v3+json"}

'''
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
'''

#token = os.getenv(secrets.ACCESS_TOKEN)
#g = Github(token)
# Github Enterprise with custom hostname
#g = Github(base_url="https://githup.com/api/v3", login_or_token=token)
g = Github()
g = Github(base_url="https://githup.com/api/v3")
repo = g.get_repo('OperationsYU/pr_action')
#get_pulls()参数不写的，就是获取所有open的pull_request.
pull_requests = repo.get_pulls(state='open')
for pr in pull_requests:
	#这里可以用debug模式，获取你想要的数据，例如分支，目标分支，content等数据
    #author = pr.xx.longin
    #content = pr.head.ref
	print(pr.user.login)
	print(pr.title)
	print(pr.body)
	print(pr.base.ref)
	print(pr.head.ref)


