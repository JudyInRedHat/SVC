# 执行语句分析器
# 导入包
from . import use

# 初始化字典
input_dict = {
    "cd": use.cd,
    "init": use.init,
    "exit": use.exit
}


def analyze(input_voice):
    input_list = input_voice.split(" ")
    key = input_list[0]
    do_list = input_list[1:]
    try:
        input_dict[key](do_list)
    except Exception as e:
        if e == "unhashable type: 'list'":
            print("错误：没有该语句")
