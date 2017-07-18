from microsoftbotframework import ReplyToActivity
import requests
import json

import csv
import os
import codecs
from urllib.request import urlopen
import sys

# https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment
"""
POST
https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment
Ocp-Apim-Subscription-Key:4cfe6f744f1b486db3fa83d874bafdd9
Content-Type:application/json
Accept:application/json
"""

# https://api.korbit.co.kr/v1/ticker
fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"

def normalize_path(filename):
    fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
    if filename.startswith("http:") or filename.startswith("https:"):
        return filename
    else:
        return "file://"+os.path.abspath(filename)
    
fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
def findEntry(fileName,Name,delimiter=","):
    fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
    print("탐색 중 ... ",end="")
    sys.stdout.flush() # 표준 입력 버퍼를 출력하고 버퍼를 비움
    NoFile=False
    Entry=None
    fileName=normalize_path(fileName)
    try:
        with urlopen(fileName) as  ftpstream:
            csvfile = csv.DictReader(codecs.iterdecode(ftpstream, 'utf-8'),delimiter=delimiter)
            for e in csvfile:
                if e["이름"] == Name:
                    Entry=e
                    break
    except:
        NoFile=True
    print(" 탐색 완료")
    if NoFile:
        print("파일을 찾을 수 없습니다.")
    return Entry
  
  
fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
def echo_response(message):
  print(message)
  fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
  if message["type"] == "message":
  Name=message
  entry=findEntry(fileName,Name)
  fmt="\n{이름}님이 주문하신 {제품명}는 {주소} {주소2}로 배송되며 전화번호는 {폰번호}입니다."
  print(fmt)
  ReplyToActivity(fill=message, text=fmt.format(이름=entry["이름"], 제품명="제품명",주소=entry["주소"], 주소2=entry["주소2"], 폰번호=entry["폰번호"])).send()

  
    else:
      msg = "I'm sorry. Please enter the product name and keyword. For example, you can ask me like \"S8 screen capture\" or \"How can I capture my screen on my S8?\"."
      print(msg)


      ReplyToActivity(fill=message,
                      text=msg).send()
