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
BUCKET = "shota"
REMOTE_PATH = "h"
LOCAL_PATH = "/home/snowonion/archive/media/"
# "C:\\Users\\snowonion\\Videos\\h"
sep = '='*50


def upload(oss, filename, object_name):
    res = oss.put_object_from_file(BUCKET, object_name, filename)
    if (res.status / 100) == 2:
        print "put_object_from_file OK"
    else:
        print "put_object_from_file ERROR"
        print "upload response", res.status, res.read()
    print sep


if __name__ == "__main__":

    oss = OssAPI(HOST, ACCESS_ID, SECRET_ACCESS_KEY)
    path_inp = raw_input("请输入文件所在文件夹, 直接回车则使用默认的 " + LOCAL_PATH)
    if path_inp != '':
        print "路径修改"
        LOCAL_PATH = path_inp

    # while True:
    #     file_name_pure = raw_input("输入文件名, 直接回车则结束程序:")
    '''
    file_list=[
        'My Pico 1 For Full Ages Part 2 of 2.flv'
    ,'My PICO Series 1.rmvb'
    ,'My PICO Series 2.rmvb'
    ,'My PICO Series 3.rmvb'
    ,'Xian Xi De Ai (Xing Fu Hua Yuan).rmvb'
    ,'Jian Dao Shao Nian.rmvb'
    ,'']
    '''
    file_list=[
        '剑道少年.mpeg'
        #'a.txt'
    ]
    for file_name_pure in file_list:
        if file_name_pure == '':
            break
        # # 关键是文件名前的那个符. 倒着找. 于是允许 / \ 混用.
        # splitter = '\\' if reversed(fp).find('\\') >= 0 else '/'
        # file_name_pure = fp.split(splitter)[-1]
        fp = LOCAL_PATH + '/' + file_name_pure
        fn = REMOTE_PATH + '/' + file_name_pure
        print fn, fp
        upload(oss, fp, fn)

        #
        # #对特定的URL签名，默认URL过期时间为60秒
        # method = "GET"
        # #bucket = "test" + time.strftime("%Y-%b-%d%H-%M-%S").lower()
        # object = "test_object"
        # url = "http://" + HOST + "/oss/" + bucket + "/" + object
        # headers = {}
        # resource = "/" + bucket + "/" + object
        #
        # timeout = 60
        # url_with_auth = oss.sign_url_auth_with_expire_time(method, url, headers, resource, timeout)
        # print "after signature url is: ", url_with_auth
        # print sep
        # #创建属于自己的bucket
        # acl = 'private'
        # headers = {}
        # res = oss.put_bucket(bucket, acl, headers)
        # if (res.status / 100) == 2:
        # print "put bucket ", bucket, "OK"
        # else:
        # print "put bucket ", bucket, "ERROR"
        # print sep
        #
        # #列出创建的bucket
        # res = oss.get_service()
        # if (res.status / 100) == 2:
        # body = res.read()
        #     h = GetServiceXml(body)
        #     print "bucket list size is: ", len(h.list())
        #     print "bucket list is: "
        #     for i in h.list():
        #         print i
        # else:
        #     print res.status
        # print sep

        # #把指定的字符串内容上传到bucket中,在bucket中的文件名叫object。
        # object_name = "object_test-1"
        # input_content = "hello, OSSsssssssss"
        # content_type = "text/HTML"
        # headers = {}
        # res = oss.put_object_from_string(bucket, object_name, input_content, content_type, headers)
        # if (res.status / 100) == 2:
        #     print "put_object_from_string OK"
        # else:
        #     print "put_object_from_string ERROR"
        #     print res.reason
        #     print res.status
        #     print res.read()
        # print sep



        #
        # #指定文件名, 把这个文件上传到bucket中,在bucket中的文件名叫object。
        # object = "object_test"
        # filename = __file__
        # content_type = "text/HTML"
        # headers = {}
        #
        # fp = open(filename, 'rb')
        # res = oss.put_object_from_fp(bucket, object, fp, content_type, headers)
        # fp.close()
        # if (res.status / 100) == 2:
        #     print "put_object_from_fp OK"
        # else:
        #     print "put_object_from_fp ERROR"
        # print sep
        #
        # #下载bucket中的object，内容在body中
        # object = "object_test"
        # headers = {}
        #
        # res = oss.get_object(bucket, object, headers)
        # if (res.status / 100) == 2:
        #     print "get_object OK"
        # else:
        #     print "get_object ERROR"
        # print sep
        #
        # #下载bucket中的object，把内容写入到本地文件中
        # object = "object_test"
        # headers = {}
        # filename = "get_object_test_file"
        #
        # res = oss.get_object_to_file(bucket, object, filename, headers)
        # if (res.status / 100) == 2:
        #     print "get_object_to_file OK"
        # else:
        #     print "get_object_to_file ERROR"
        # print sep
        #
        # #查看object的meta 信息，例如长度，类型等
        # object = "object_test"
        # headers = {}
        # res = oss.head_object(bucket, object, headers)
        # if (res.status / 100) == 2:
        #      print "head_object OK"
        #      header_map = convert_header2map(res.getheaders())
        #      content_len = safe_get_element("content-length", header_map)
        #      etag = safe_get_element("etag", header_map).upper()
        #      print "content length is:", content_len
        #      print "ETag is: ", etag
        #
        # else:
        #     print "head_object ERROR"
        # print sep
        #
        # #查看bucket中所拥有的权限
        # res = oss.get_bucket_acl(bucket)
        # if (res.status / 100) == 2:
        #     body = res.read()
        #     h = GetBucketAclXml(body)
        #     print "bucket acl is:", h.grant
        # else:
        #     print "get bucket acl ERROR"
        # print sep
        #
        # #列出bucket中所拥有的object
        # prefix = ""
        # marker = ""
        # delimiter = "/"
        # maxkeys = "100"
        # headers = {}
        # res = oss.get_bucket(bucket, prefix, marker, delimiter, maxkeys, headers)
        # if (res.status / 100) == 2:
        #     body = res.read()
        #     h = GetBucketXml(body)
        #     (file_list, common_list) = h.list()
        #     print "object list is:"
        #     for i in file_list:
        #         print i
        #     print "common list is:"
        #     for i in common_list:
        #         print i
        # print sep
        #
        # #以object group的形式上传大文件，object group的相关概念参考官方API文档
        # res = oss.upload_large_file(bucket, object, __file__)
        # if (res.status / 100) == 2:
        #     print "upload_large_file OK"
        # else:
        #     print "upload_large_file ERROR"
        #
        # print sep
        #
        # #得到object group中所拥有的object
        # res = oss.get_object_group_index(bucket, object)
        # if (res.status / 100) == 2:
        #     print "get_object_group_index OK"
        #     body = res.read()
        #     h = GetObjectGroupIndexXml(body)
        #     for i in h.list():
        #         print "object group part msg:", i
        # else:
        #     print "get_object_group_index ERROR"
        #
        # res = oss.get_object_group_index(bucket, object)
        # if res.status == 200:
        #     body = res.read()
        #     h = GetObjectGroupIndexXml(body)
        #     object_group_index = h.list()
        #     for i in object_group_index:
        #         if len(i) == 4 and len(i[1]) > 0:
        #             part_name = i[1].strip()
        #             res = oss.delete_object(bucket, part_name)
        #             if res.status != 204:
        #                 print "delete part ", part_name, " in bucket:", bucket, " failed!"
        #             else:
        #                 print "delete part ", part_name, " in bucket:", bucket, " ok"
        # print sep
        # #multi part upload相关操作
        # #get a upload id
        # upload_id = ""
        # res = oss.init_multi_upload(bucket, object, headers)
        # if res.status == 200:
        #     body = res.read()
        #     h = GetInitUploadIdXml(body)
        #     upload_id = h.upload_id
        #
        # if len(upload_id) == 0:
        #     print "init upload failed!"
        # else:
        #     print "init upload OK!"
        #     print "upload id is: %s" % upload_id
        #
        # #upload a part
        # data = "this is test content string."
        # part_number = "1"
        # res = oss.upload_part_from_string(bucket, object, data, upload_id, part_number)
        # if (res.status / 100) == 2:
        #     print "upload part OK"
        # else:
        #     print "upload part ERROR"
        #
        # #complete upload
        # part_msg_xml = get_part_xml(oss, bucket, object, upload_id)
        # res = oss.complete_upload(bucket, object, upload_id, part_msg_xml)
        # if (res.status / 100) == 2:
        #     print "complete upload OK"
        # else:
        #     print "complete upload ERROR"
        #
        # res = oss.get_object(bucket, object)
        # if (res.status / 100) == 2 and res.read() == data:
        #     print "verify upload OK"
        # else:
        #     print "verify upload ERROR"
        #
        # print sep
        #
        #
        # #删除bucket中的object
        # object = "object_test"
        # headers = {}
        # res = oss.delete_object(bucket, object, headers)
        # if (res.status / 100) == 2:
        #     print "delete_object OK"
        # else:
        #     print "delete_object ERROR"
        # print sep
        #
        # #删除bucket
        # res = oss.delete_bucket(bucket)
        # if (res.status / 100) == 2:
        #     print "delete bucket ", bucket, "OK"
        # else:
        #     print "delete bucket ", bucket, "ERROR"
        #
        # print sep
        #
        #
