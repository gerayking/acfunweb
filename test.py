import browsercookie
import requests
import base64
from acfun import fileController
from bupt import excelController
from bs4 import BeautifulSoup
import json
from http import cookiejar
from acfun import tokenController as tC



def getsession(username:str,password:str):
    url = "http://id.app.acfun.cn/rest/web/login/signin"
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6",
    }
    data={
        "username":username,
        "password":password,
        "key":"",
        "captcha":""
    }
    session = requests.Session()
    response = session.post(url,headers=header,data=data)
    responsedict = json.loads(response.text)
    return responsedict,session

def getmain(session):
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6",
    }
    # cookie = tC.getCookie()
    response = session.get("http://www.acfun.cn/member/#area=splash",headers=header,verify=False)
    html = response.text
    fileController.savehtml("self",html)
    return response

def load(session):
    response = getmain(session)
    soup = BeautifulSoup(response.text,features="lxml")
    hintlist =  soup.find_all('span',attrs={'class':'hint'})
    ptslist = soup.find_all('span',attrs={'class':'pts'})
    username = soup.find_all('a',attrs={'class':'name', 'href':'/u/26550691'})
    print('用户名: ' + str(username[0].string))
    for i in range(len(ptslist)):
        print(str(hintlist[i].string)+': ' + str(ptslist[i].string))

def follow(toUserId:str,Session):
    data={
        'toUserId': toUserId,
        'action': '1',
        'groupId': "0"
    }
    referce = "https://www.acfun.cn/u/"+toUserId
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": referce,
        "Origin": "https://www.acfun.cn",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    response = Session.post('http://www.acfun.cn/rest/pc-direct/relation/follow',headers=header,data=data,verify=False)
    print(response.json())
    responsedict = response.json()
    if(responsedict['result'] == 0):
        return 1
    return -1



if __name__ == "__main__":
    # 登录验证
    while True :
        print('请输入用户名:')
        username = str(input())
        print('请输入密码:')
        password = str(input())
        response,session = getsession(username,password)
        if response['result'] != 0:
            print(response['error_msg'])
            continue
        else:
            print("=============登录成功---欢迎您=============")
            load(session)
            break
    while True:
        print("1.关注某人")
        op = int(input())
        if op == 1:
            print("请输入关注人的Uid")
            userId = str(input())
            res = follow(userId,session)
            if res == -1:
                print("关注失败")
            else:
                print("关注成功")