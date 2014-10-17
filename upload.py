#!/usr/bin/env python
# coding=utf8

__author__ = 'snowonion'

import time
import os
from oss.oss_api import OssAPI
# from oss.oss_xml_handler import *

HOST = "oss-cn-beijing.aliyuncs.com"
ACCESS_ID = "KXHYBr8lH9kJQufz"
SECRET_ACCESS_KEY = raw_input("请输入 KXHYBr8lH9kJQufz 对应的 SECRET_ACCESS_KEY:")
BUCKET = "mus1c"
REMOTE_PATH = "new_age/bandari/sunny_bay"

LOCAL_PATH = "/home/snowonion/download"
FILE_LIST = [
    'A Woodland Night.mp3'
    , 'Childhood Memory.mp3'
]

sep = '=' * 50


def upload(oss, filename_local, object_name_remote):
    res = oss.put_object_from_file(BUCKET, object_name_remote, filename_local)
    if (res.status / 100) == 2:
        print "put_object_from_file OK"
    else:
        print "put_object_from_file ERROR"
        print "upload response", res.status, res.read()
    print sep


if __name__ == "__main__":

    oss = OssAPI(HOST, ACCESS_ID, SECRET_ACCESS_KEY)

    bucket_inp = raw_input("请输入 Bucket, 默认 " + BUCKET)
    if bucket_inp != '':
        print "Bucket 修改"
        BUCKET = bucket_inp

    remote_inp = raw_input("请输入远程目录路径, 默认 " + REMOTE_PATH)
    if remote_inp != '':
        print "远程目录修改"
        REMOTE_PATH = remote_inp

    path_inp = raw_input("请输入文件所在文件夹, 直接回车则使用默认的 " + LOCAL_PATH)
    if path_inp != '':
        print "本地路径修改"
        LOCAL_PATH = path_inp

    while True:
        print "默认上传文件: ", FILE_LIST
        file_name_inp = raw_input("直接回车则上传上述文件, 输入文件名回车则向其中添加待上传文件:")
        if file_name_inp == '':
            break
        else:
            FILE_LIST.append(file_name_inp)

    for file_name_inp in FILE_LIST:
        # # 关键是文件名前的那个符. 倒着找. 于是允许 / \ 混用.
        # splitter = '\\' if reversed(fp).find('\\') >= 0 else '/'
        # file_name_pure = fp.split(splitter)[-1]

        file_local = LOCAL_PATH + '/' + file_name_inp
        file_remote = REMOTE_PATH + '/' + file_name_inp
        print "上传 %s 至 %s" % (file_local, file_remote)
        upload(oss, file_local, file_remote)

