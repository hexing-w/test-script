# -*- coding:utf-8 -*-
from locust import HttpLocust, TaskSet, task,events
import json
import random
import time

class CodeError(Exception):
    pass
usernames = []
def createName():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        name = ""
        for i in range(10):
            name = name + chars[random.randint(0,len(chars)-1)]

        if usernames.count(name) == 0:
            usernames.append(name)
            return name
            break

def createUid():
    uid = 0
    uid = 100000000 + random.randint(1,1087)
    return uid
# def returnMulti(param):
#     r = redis.Redis(host='192.168.32.159',port=6380,db=0)
#     star = r.hget('user_'+str(param),'star')
#     build_info = r.hgetall('star_'+str(param)+'_'+str(star))
#     for i in range(1,6):
#         info = '1300'+str(i)
#         level_info = json.loads(build_info[info])
#         if level_info['level'] != 5:
#             info = '1300'+ str(i)
#             build = info + str(level_info['level'])
#             break
#     return star, build

class UserBehavior(TaskSet):
    def __init__(self, p):
        TaskSet.__init__(self, parent=p)
        self.url = "http://192.168.40.34:85"
        self.token = ""
        self.uid = ""

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # locust -f ssgame.py --host=http://192.168.32.159
        # self.heartbeat()
        


  
    @task(3)
    def openturntable(self):
        param_openturntable = {"uid": createUid(),
                               "token": ""}
        self.send_post("/OpenTurntable", param_openturntable, "openturntable")

    def send_post(self, interfacename, data, name):
        data = json.dumps(data)
        url = interfacename
        starttime = time.time()
        result = self.client.post(url, data)
        response_time = int((time.time() - starttime) * 1000)
        print result.text
        # code  = result_json["code"]
        # if code == 1000:
        #     respones_error = CodeError(code)
        #     #events.request_failure.fire(request_type="POST", name=name, response_time=response_time,exception=respones_error)
        # print result_json

        # if name == "login":
        #     self.token = result_json["data"]["token"]
        #     self.uid = result_json["data"]["uid"]
        # print result.text
        # response_time = int((time.time() - starttime) * 1000)



class WebsiteUser(HttpLocust):
    host = 'http://192.168.40.34:85'
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 5000