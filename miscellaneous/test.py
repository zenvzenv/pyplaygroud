import requests
import json

head = '【摸鱼办】提醒您，'
rep = requests.get("http://timor.tech/api/holiday/tts")
print(rep.text)
holiday = json.loads(rep.text)
print(head + holiday['tts'])
