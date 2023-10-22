# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:20:32 2023

@author: user
"""
import configparser
import sys
import os
import easyocr
import cv2
# 建立 ConfigParser
# determine if application is a script file or frozen exe
# 取得當前執行路徑

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
    
    
cf = configparser.ConfigParser()
# 讀取 INI 設定檔 有包含中文字
cf.read('config.ini',encoding='utf-8-sig')
# 取得設定值
os.system("cls")
print('===============開始讀取config.ini檔案========================')
captcha_input_file=cf['PATH']['captcha_input_file']
captcha_output_file=cf['PATH']['captcha_output_file']
colorTogray=cf['COLOR']['colorTogray']
print('--------------------讀取設定檔config.ini---------------------')
print('CAPTCHA圖片input檔名:',captcha_input_file)
print('CAPTCHA辨識output檔名:',captcha_output_file)
print('彩色轉灰階:',colorTogray)
print('-'*60)
print(' ')
print(' ')
image = cv2.imread(captcha_input_file)
#OpenCV 彩色轉灰階
if colorTogray == 'Y':
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
reader=easyocr.Reader(['en'],gpu=False)
#result=reader.readtext(captcha_input_file,detail=0)
result=reader.readtext(image,detail=0)
result=str(result)
result = result.replace(',', '')
result = result.replace('\'', '')
result = result.replace('[', '')
result = result.replace(']', '')
result = result.replace(' ', '')
result = result.replace('&', '8')
print('-----------------------OCR辨識結果---------------------------')
print(result)
print('-'*60)

path = captcha_output_file
f = open(path, 'w')
f.writelines(result)
f.close()