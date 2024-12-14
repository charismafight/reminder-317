import requests
import json

def fetchUndoneNames(id,cookies):
    undoneUrl = f'https://nursetrain-prd.317hu.com/nurse-train-web/nursetrain/web/course/read/v1.0.1/studyDetailPage?pageNum=1&pageSize=100&hospitalBranchIds=&deptIds=&wardIds=28040&status=1&releaseId={id}'
    allUrl = f'https://nursetrain-prd.317hu.com/nurse-train-web/nursetrain/web/course/read/v1.0.1/studyDetailPage?pageNum=1&pageSize=100&hospitalBranchIds=&deptIds=&wardIds=28040&status=-9&releaseId={id}'
    staff = json.loads(requests.get(undoneUrl,cookies=cookies).text)
    
    sl = staff['data']['result']
    for s in sl:
        print(s['accountName'])

# login
r = requests.post('https://usercentral.317hu.com/userCentral-web/user/accountRest/login', 
                  data={
                      'login': '15927366191',
                        'password':'5CWS06PhM4jlIGEzbe2lpLt6zoMo8RsY4dJz1WdYjjWsnCmVz3eQJWSgky01U59Z',
                        'code':'',
                        'source':'2'
                        })
assert r.status_code==200

# set cookie
c = r.cookies

plansUrl = 'https://nursetrain-prd.317hu.com/nurse-train-web/nursetrain/web/course/release/v1.0.1/releases?hospitalId=1222&loginUserId=409730&depts=28040&role=3&levelCode=0&rangeType=0&type=0&pageNum=1&pageSize=100'
plans = requests.get(plansUrl,
                     cookies=c)
assert plans.text != ''

plansData = json.loads(plans.text)

if len(plansData['data']['result']) == 0:
    print('no plan results')
else:
    print('fetch succeed')
# structure of plans:
# use id as the next step's releaseId

planList = plansData['data']['result']

for p in planList:
    print(p['id'])
    fetchUndoneNames(p['id'],c)
