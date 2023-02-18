#!/usr/bin/python3
from B import test
import importlib
import time
# 測試如何透過重新載入 B.py
# 達到不關閉程式動態修改腳本

dict={}
imm = "strin\'g"
dict["12345"] = ['NAMe','URL',123,imm]
print(dict["12345"])

John = test('林義雄')
John.prints('Nick')

# while input('Enter = ') != 'Q' :
#    print('Hello')
importlib.reload(B)
test.prints(John,'Nick')
