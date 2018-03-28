import requests
import re
import ast

def SaveHTML(fileName):
    f = open(fileName + ".html", 'w')
    f.write(result.text)
    f.close()

def SaveXML(fileName):
    f = open(fileName + ".xml", 'w')
    f.write(result.text)
    f.close()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_SSO_Global_Logout_url="get^http://eclass.kangnam.ac.kr/eclass/sso/logout.jsp$";'
}

payload = {
    'gid':'gid_web',
    'returl': 'https://web.kangnam.ac.kr/sso/index.jsp',
    'uid': '',
    'password': ''
}

session = requests.Session()

result = session.post('https://knusso.kangnam.ac.kr/sso/pmi-sso-login-uid-password.jsp',data=payload,headers=headers, verify=False)
print(result.headers)
print(result.cookies)
print("================")
locationDic = []
ssoToken = ""
for index in result.history:
    headerDic = {}
    print(index.headers)
    headerDic = ast.literal_eval(str(index.headers))
    print("header loc->", headerDic["Location"])
    locationDic.append(headerDic["Location"])
    if "sso_token" in headerDic:
        ssoToken = headerDic["sso_token"]
    # break
pmiSso = re.search("pmi-sso-return=(.+?)\n", locationDic[0] + "\n")
if pmiSso != None:
    print("pmi->", pmiSso.group(1))
print("sso->", ssoToken)
print("cookies->", session.cookies)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

result = session.post('https://knusso.kangnam.ac.kr/sso/pmi-sso-login-uid-password.jsp',data=payload,headers=headers, verify=False)
print(result.headers)
print(result.cookies)
print("================")

url = "http://eclass.kangnam.ac.kr/eclass/total_main.jsp"
result = session.get(url,headers= headers, verify=False)
print("session cookie->", session.cookies)
print("main content->", result.content)

url = "http://eclass.kangnam.ac.kr/eclass/eclass/SSO_Login.action?task=SSO_LOGIN"
result = session.get(url,headers= headers, verify=False)
print("session cookie->", session.cookies)
print("main content->", result.content)

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_YS&sysType=ECLS', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_YS")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_NEW_PAPER&sysType=ECLS', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_NEW_PAPER")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_MAIN_MENU_LIST&sysType=ECLS&clubId=201501180&userFg=E0004007&mainPageType=main&lang=ko_KR', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_MAIN_MENU_LIST")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_MY_LECT&clubStat=%27S02001%27', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_MY_LECT")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_STU_MAIN&sysType=ECLS&clubId=ECLS_MAIN&menuCode=1000&menuNo=1&flag=system', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_STU_MAIN")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_STU_MAIN&sysType=ECLS&clubId=ECLS_MAIN&menuCode=1005&menuNo=1&flag=class', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_STU_MAIN2")

result = session.post('http://eclass.kangnam.ac.kr/eclass/eclass/findMain.action?taskId=F_STU_MAIN&flag=homeWork', headers= headers, verify=False)
print(result.headers)
print(result.content)
SaveXML("F_STU_MAIN3")