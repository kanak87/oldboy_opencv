# -*- coding: utf-8 -*-

import requests
import json

appid = 'oldboy'
apikey = 'f546be3c87a011e5b1690cc47a1fcfae'
sender = '01071211947'
receivers = ['01096886656']
content = '하하?'

url = 'https://api.bluehouselab.com/smscenter/v1.0/sendsms'
params = {
    'sender'     : sender,
    'receivers'  : receivers,
    'content'    : content,
}
headers = {'Content-type': 'application/json; charset=utf-8',}
r = requests.post(url, data=json.dumps(params),
                auth=(appid, apikey), headers=headers)

print r.status_code, r.reason
if r.status_code == 200:
    print r.json()