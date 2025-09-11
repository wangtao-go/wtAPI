import requests
import json
from APIServer.func.get_token import get_token
def get_sampleContext(sample_id):
   url = f"http://101.126.75.103:8080/admin/report-details/{sample_id}"

   # 你的 Bearer Token
   token = get_token()  # 请替换为实际 token
   print(token)
   # token='MDcWz6iZtZvyfgqotfoxoHEPk2UD03nHWXqQT05gVbZc1JT0HvNJu9hh'

   headers = {
      'Content-Type': 'application/json',
      'Accept': '*/*',
      'Connection': 'keep-alive',
      "Authorization": f"Bearer {token}"
   }

   response = requests.request("GET", url, headers=headers)
   response.encoding = 'utf-8'
   return response.text






