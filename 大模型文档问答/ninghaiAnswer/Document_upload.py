# -*- coding:utf-8 -*-
import hashlib
import base64
import hmac
import time
import random
from urllib.parse import urlencode
import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class Document_Upload:
    def __init__(self, APPId, APISecret, timestamp):
        self.APPId = APPId
        self.APISecret = APISecret
        self.Timestamp = timestamp

    def get_origin_signature(self):
        m2 = hashlib.md5()
        data = bytes(self.APPId + self.Timestamp, encoding="utf-8")
        m2.update(data)
        checkSum = m2.hexdigest()
        return checkSum


    def get_signature(self):
        # 获取原始签名
        signature_origin = self.get_origin_signature()
        # 使用加密键加密文本
        signature = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha1).digest()
        # base64密文编码
        signature = base64.b64encode(signature).decode(encoding='utf-8')
        return signature

    def get_header(self):
        signature = self.get_signature()
        header = {
            "appId": self.APPId,
            "timestamp": self.Timestamp,
            "signature": signature,
        }
        return header

    # 提交网络文件
    def get_body(self):
        body = {
            "file": "",
            "url": "文件网络地址 例如： https://xxx.xx.com/xxx.pdf",
            "fileName": "文件名, 例如：xxx.pdf",
            "fileType": "wiki",
            "callbackUrl": "your_callbackUrl"
        }
        form = MultipartEncoder(
            fields=body,
            boundary='------------------' + str(random.randint(1e28, 1e29 - 1))
        )
        return form

    # 提交本地文件
    def get_files_and_body(self):
        body = {
            "url": "",
            "fileName": "B-21分析报告.txt",
            "fileType": "wiki",
            "needSummary": False,
            "stepByStep": False,
            "callbackUrl": "your_callbackUrl",
        }
        files = {'file': open('B-21分析报告.txt', 'rb')}
        return files, body



if __name__ == '__main__':
    # 先去 开放平台控制台（https://console.xfyun.cn）创建应用，获取下列应用信息进行替换
    APPId = "xxxxx"
    APISecret = "xxxxx"

    curTime = str(int(time.time()))
    request_url = "https://chatdoc.xfyun.cn/openapi/v1/file/upload"

    document_upload = Document_Upload(APPId, APISecret, curTime)
    headers = document_upload.get_header()

    # ******************提交网络文件
    # body = document_upload.get_body()
    # headers['Content-Type'] = body.content_type
    # response = requests.post(request_url, data=body, headers=headers)

    # ******************提交本地文件
    files, body = document_upload.get_files_and_body()
    response = requests.post(request_url, files=files, data=body, headers=headers)

    print("请求头", response.request.headers, type(response.request.headers))
    print('onMessage：\n' + response.text)

    # 文档上传成功
