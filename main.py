from goingin import tool


# 设置读入文件的脚本
def read_file(filename):
    temple = open(filename, mode="r")
    return_value = temple.read()
    return return_value


user_name = read_file("goingin/log in data.txt")
if user_name == "":
    user_name = "访客"

t = tool.goingLooper(user_name)
t.main_running()
