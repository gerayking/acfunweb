import  json

def saveCookie(cookie:dict):
    jsObj = json.dumps(cookie)
    file = open('token.json','w+')
    file.write(jsObj)
    file.close()

def getCookie():
    with open('token.json','r') as json_file:
        dic = json.load(json_file)
    return dic
