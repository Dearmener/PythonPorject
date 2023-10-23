import http.client

# Disable SSL certificate verification
conn = http.client.HTTPSConnection("jw.ustc.edu.cn", context=ssl._create_unverified_context())

payload = ''
headers = {
  'Cookie': 'SESSION=8c9df3ee-69d4-45cc-b38a-b80610c3fb43; SVRNAME=student1; SESSION=57507f30-f14a-4117-99ac-7ff0b54297ff',
  'Origin': 'https://jw.ustc.edu.cn',
  'Referer': 'https://jw.ustc.edu.cn/for-std/course-select/371337/turn/802/select'
}

conn.request("POST", "/ws/for-std/course-select/add-request?studentAssoc=371337&lessonAssoc=151663&courseSelectTurnAssoc=802&scheduleGroupAssoc=null&virtualCost=0", payload, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
