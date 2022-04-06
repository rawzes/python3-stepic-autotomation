import json

import requests

url = "https://kpvk1s00.plrm.zone/PiratesVk/Segment00/segment.ashx"
data = '{"s":{"x":"NaN","np":false,"a":true,"vk":{"b":true},"de":null,"fl":false,"p":null,"n":"Roman Razumeyko",' \
       '"gr":null,"s":null,"i":"vk23253695","t":0,' \
       '"u":"https://sun1.beltelecom-by-minsk.userapi.com/s/v1/if1' \
       '/ecSRAqhU1LbvcWNGwBks6jTGcDJwoiVwsjMuEPtluJHrefORTLZVBOUX-UUhPqW05r9QWYAx.jpg?size=200x297&quality=96&crop' \
       '=801,0,1289,1920&ava=1","ar":null,"d":"Roman;Razumeyko;NaN;ru_RU;0;;","tg":0,"l":"en-US","im":false},' \
       '"i":"vk23253695","mr":"","t":-180,"f":["vk1244397","vk4451020","vk10930553","vk20845880","vk44288023",' \
       '"vk50429171","vk63255645","vk66736569","vk72073270","vk89911823","vk95265133","vk97308303","vk99640825",' \
       '"vk104344732","vk107490731","vk108152924","vk115680794","vk116777010","vk117584410","vk120163531",' \
       '"vk125567375","vk131619770","vk133061304","vk135362886","vk139561085","vk161970855","vk162916144",' \
       '"vk164551705","vk175522799","vk175536827","vk198614184","vk225085720","vk232523132","vk236327955",' \
       '"vk237274997","vk237546492","vk412129441","vk516823934","vk634692268","vk636254524"],"l":"unknown",' \
       '"c":{"x":1536,"sfb":false,"v":"1.0","cpu":"x86","pht":null,"ht":null,"mc":null,"y":864,"i":13},"rr":null} '
header = {'Host': 'kpvk1s00.plrm.zone',
          'Connection': 'keep-alive',
          'Content-Length': '1115',
          'Accept': '*/*',
          'Content-Type': 'text/html',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Client/Win VKApp/24.59875 Safari/537.36',
          'client-type': '1',
          'client-ver': '646',
          'locale-name': 'ru-RU',
          'server-method': 'SignIn',
          'sign-code': '9b46fd9d0477d1294dc08892abf0a8d27378c8be4035779092296e80a8b92674',
          'signin-authKey': 'c38df1b15fb4cb0b8953a8a1658951da',
          'signin-authSeed': '25a993378c73310bf850d6afb673fac85625ebe723d7bb06133b33222ef4d1e11bd17da0059012f0aa778',
          'signin-userId': 'vk23253695',
          'Origin': 'https://cdn01.x-plarium.com',
          'X-Requested-With': 'ShockwaveFlash/32.0.0.223',
          'Sec-Fetch-Site': 'cross-site',
          'Sec-Fetch-Mode': 'no-cors',
          'Referer': 'https://cdn01.x-plarium.com/pirates/new_client/prod/vk/20220216_1136_oukg2y2t330.swf',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'}
sess = requests.Session()
resp = sess.post(url, params=json.dumps(data), headers=header)
# response = requests.post(url=url, params=data, headers=header, verify=True, timeout=1000)
print(resp.content)
