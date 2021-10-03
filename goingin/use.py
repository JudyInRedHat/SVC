# 导入库
import sys
import os
from . import globalvar
import win32api,win32con


def init(list):
    os.makedirs(".svc")
    win32api.SetFileAttributes('.svc/', win32con.FILE_ATTRIBUTE_HIDDEN)
    print("初始化项目成功")



def cd(list):
    try:
        os.chdir(list[0])
        globalvar.path = os.getcwd()
        # 设置询问语
        globalvar.ask_voice = f'{globalvar.path} $'
    except:
        print("错误：无法切换到该路径")



def exit(list):
    sys.exit()
