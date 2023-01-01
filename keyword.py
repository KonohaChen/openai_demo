import os
import sys

import requests
import json

#the program will try to match the words from the input with the keywords folders
question = input('Please enter the question')

words_list = question.split(" ");

dir = "F:\openai_demo\keywords"
list = os.listdir(dir)
for type in list:
    if os.path.isfile(os.path.join(dir,type)):
        list.remove(type)

for word in words_list:
    if word in list:
        print ("keyword matched!")
        answer_path = os.path.join("F:\openai_demo\keywords/",word,"answer.txt")
        question_path = os.path.join("F:\openai_demo\keywords/",word,"question.txt")
        with open(answer_path, "r") as a,open(question_path,"r") as q:
            print("best match question:" + q.readline())
            print("best match answer:" + a.readline())
            sys.exit()
print("keyword not found!")
# with open("F:\openai_demo\questions.txt", "r") as q,open("F:\openai_demo\\answer.txt","a") as f:
