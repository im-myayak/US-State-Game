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

        if user_answer in state:
            state_true = state_data[state_data.state == user_answer]

            self.goto(int(state_true.x), int(state_true.y))
            self.correct_list.append(user_answer)
            self.score = len(self.correct_list)
            self.write_state_name(user_answer)

    def not_guessed_states(self):
        if self.score == 50:
            return 'All the states were guessed'
        else:
            missing_state = list(set(state_data.state) - set(self.correct_list))
            new_data = pd.DataFrame(missing_state)
            new_data.to_csv("states_not_guessed")
            return " "

    def write_state_name(self, user_answer):
        self.write(f"{user_answer} ")
