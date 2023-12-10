import os
import random
import time

def sendsms(Phone,content):
    time.sleep(5)
    os.shell(f"adb shell am start -a android.intent.action.SENDTO -d sms:+620{Phone} --es sms_body {content}")



def start() :
    xx = int(input("Nomor Telepon:"))
    cc = input("Text:")
    sendsms(xx,cc)

start()
