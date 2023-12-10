import os
import random
import time

def sendsms(Phone,content):
    time.sleep(5)
    os.shell(f"adb shell am start -a android.intent.action.SENDTO -d sms:+620{Phone} --es sms_body {content}")
    time.sleep(2)
    os.shell("adb shell input keyevent KEYCODE_TAB")
    os.shell("adb shell input keyevent KEYCODE_TAB")
    time.sleep(1)
    os.shell("adb shell input keyevent KEYCODE_ENTER")


def start() :
    xx = int(input("Nomor Telepon:"))
    cc = input("Text:")
    sendsms(xx,cc)

start()
