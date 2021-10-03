# 导入库
import os
import ctypes
from . import globalvar


# 初始化语句
def init(user_name):
    # 检查是否有管理员权限
    globalvar.admin = bool(ctypes.windll.shell32.IsUserAnAdmin())
    # 设置输出提示语
    if globalvar.admin:
        globalvar.output_list.append("Administrator")
    else:
        globalvar.output_list.append("User")
    globalvar.output_list.append("@")
    globalvar.output_list.append(user_name)
    for ch in globalvar.output_list:
        globalvar.output_voice = globalvar.output_voice + ch
    # 设置工作路径
    os.chdir("C:\\Users\\Administrator\\Desktop")
    globalvar.path = os.getcwd()
    # 设置询问语
    globalvar.ask_voice = f'{globalvar.path} $'

def change_the_voice(user_name):
    pass
