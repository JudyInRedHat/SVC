from . import init
from . import globalvar
from . import inputanalizer


class goingLooper:
    def __init__(self, user_name):
        init.init(user_name)

    def main_running(self):
        while True:
            print(globalvar.output_voice)
            key_input = input(globalvar.ask_voice)
            inputanalizer.analyze(key_input)
