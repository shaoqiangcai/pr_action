# -*- coding: utf-8 -*-
import os
result = {
  "task":"OK",
  "msg": "wahah"
}

os.popen("echo ::set-output name=task::%s" % result['task'])
os.popen("echo ::set-output name=msg::%s" % result['msg'])
