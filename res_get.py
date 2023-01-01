import requests
import json
import os

from os import makedirs
from os.path import exists

url = "https://api.openai.com/v1/completions"

with open("F:\openai_demo\questions.txt", "r") as q,open("F:\openai_demo\\answer.txt","a") as f:
    question = q.readline()
    while question:

        payload = json.dumps({
          "model": "text-davinci-003",
          "prompt": question,
          "max_tokens": 25,
          "temperature": 0
        })
        headers = {
          'Authorization': 'Bearer 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',
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        js = json.dumps(response.text)

        answer = json.loads(response.text)
        text = answer["choices"]

        json.dump(text,f)
        f.write('\n')
        print("files updated...")

        question = q.readline()
q.close()
f.close()
