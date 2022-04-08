import pandas as pd

from turtle import Turtle
state_data = pd.read_csv("50_states.csv")

FONT = ("Courier", 15, "bold")


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.correct_list = []

    def is_state_exist(self, user_answer):

        state = list(state_data.state)
        print(type(state))
        if user_answer in state:
            state_true = state_data[state_data.state == user_answer]

            self.goto(int(state_true.x), int(state_true.y))
            self.correct_list.append(user_answer)
            self.score = len(self.correct_list)
            self.write_state_name(user_answer)

    def write_state_name(self, user_answer):
        self.write(f"{user_answer} ")
