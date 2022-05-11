# -*- coding: utf-8 -*-
result = {
  "task":"OK",
  "msg": "wahah"
}
print(f"::set-output name={Task}::{result['task']}")
print(f"::set-output name={MSG}::{result['msg']}")
