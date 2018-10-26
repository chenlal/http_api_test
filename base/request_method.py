# coding=utf-8

import requests
import json


class RunMain:

    # def __init__(self, url, method, data=None, header=None):
    #     if method == 'Post':
    #         self.send_post(url, data, header)
    #     else:
    #         self.send_get(url,header)

    def send_post(self, url, data, header=None):
        if header:
            res = requests.post(url, data, header).json()
        else:
            res = requests.post(url, data).json()
        # print(json.dumps(res, ensure_ascii=False))
        # print(res.text)
        return json.dumps(res, ensure_ascii=False)

    def send_get(self, url, header=None):
        if header:
            res = requests.get(url, header).json()
        else:
            res = requests.get(url).json()
        # print(json.dumps(res, ensure_ascii=False))
        # print(res.text)
        return json.dumps(res, ensure_ascii=False)

    # def run_main(self,url,method,data=None,header=None):
    #     if method == 'Post':
    #         self.send_post(url, data, header)
    #     else:
    #         self.send_get(url, header)

# if __name__ == '__main__':
#     url = 'http://192.168.49.157:8200/index/login.do'
#     data = {
#         'username': 'admin',
#         'password': 'admin123'
#     }
#     run = RunMain(url, 'Post', data)
