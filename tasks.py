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

def normalize_path(filename):
    if filename.startswith("http:") or filename.startswith("https:"):
        return filename
    else:
        return "file://"+os.path.abspath(filename)
def findEntry(fileName,Name,delimiter=","):
    print("finding ... ",end="")
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
def Program():
    while True:
        print("탐색할 파일 목록:")
        print("")
        print ("(1) 내 컴퓨터에 있는 파일")
        print ("(2) 인터넷에 있는 파일")
        print("")
        NumStr=input("번호를 선택하세요[1,2]: ")
        if not NumStr:
            break
        BadInput=False
        try:
            NumChoice=int(NumStr)
        except:
            BadInput=True
        if BadInput:
            continue
        if NumChoice==1:
            fileName="aaa.cvs"
        elif NumChoice==2:
            fileName="https://christianlike-super.000webhostapp.com/smalls/remote-csv/aaa.cvs"
        else:
            continue
        while True:
            Name=input("\n고객님의 성함을 입력하십시오: ")
            if not Name:
                break
            entry=findEntry(fileName,Name)
            if entry!=None:
                fmt="\n{이름}님이 주문하신 {제품명}는 {주소} {주소2}로 배송되며 전화번호는 {폰번호}입니다."
                print(fmt.format(이름=entry["이름"], 제품명="제품명",주소=entry["주소"], 주소2=entry["주소2"], 폰번호=entry["폰번호"]))
            else:
                print("\n그 성함을 가진 고객은 목록에 없습니다.")
                ReplyToActivity(fill=message, text="\n그 성함을 가진 고객은 목록에 없습니다.").send()
    return  
  
  
      
def echo_response(message):
  print(message)

  if message["type"] == "message":
    if "s8" and "capture" in message["text"]:
  
      msg = "A screenshot is a snapshot of your device screen saved as a photo. There are several ways to capture screenshots on your device. After the screenshots are captured, they will be automatically saved to the Gallery. If you want to know how to capture the screen on your galaxy S8 & S8+, click the link below."
      print(msg)
      msg2 = "http://www.samsung.com/us/support/answer/ANS00062596/"
      print(msg2)
      ReplyToActivity(fill=message, text=msg).send()
      ReplyToActivity(fill=message, text=msg2).send() 
      ReplyToActivity(fill=message, text=msg4).send()
    else:
      msg = "Sorry. I can't understand. Please enter the product name with the keyword. For example, you can ask me like \"S8 screen capture\" or \"How can I capture my screen on my S8?\"."
      print(msg)
        


      ReplyToActivity(fill=message,
                      text=msg).send()
    
    ReplyToActivity(fill=message, text="\n그 성함을 가진 고객은 목록에 없습니다.").send()
