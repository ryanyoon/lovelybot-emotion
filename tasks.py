from microsoftbotframework import ReplyToActivity
import requests
import json

# https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment
"""
POST
https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment

Ocp-Apim-Subscription-Key:4cfe6f744f1b486db3fa83d874bafdd9
Content-Type:application/json
Accept:application/json
"""

# https://api.korbit.co.kr/v1/ticker

def echo_response(message):
  print(message)
  
  if message["type"] == "message":
    if "s8" and "capture" in message["text"]:

      r = requests.get("https://api.korbit.co.kr/v1/ticker")
      bitcoin_price = r.json()["last"]
      msg = "A screenshot is a snapshot of your device screen saved as a photo. There are several ways to capture screenshots on your device. After the screenshots are captured, they will be automatically saved to the Gallery. If you want to know how to capture the screen on your galaxy S8 & S8+, click the link below."
      print(msg)
      msg2 = "http://www.samsung.com/us/support/answer/ANS00062596/"
      print(msg2)
      ReplyToActivity(fill=message, text=msg).send()
      ReplyToActivity(fill=message, text=msg2).send()      
    else:
      msg = "I'm sorry. Please enter the product name and keyword. Forexample, you can ask me like ""S8 screen capture"" or ""How can I capture my screen on my S8?""."
      print(msg)


      ReplyToActivity(fill=message,
                      text=msg).send()
