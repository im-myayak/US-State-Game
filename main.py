
from turtle import Screen

from mymodule import MyTurtle

screen = Screen()
myTurtle = MyTurtle()
screen.listen()
screen.setup(width=725, height=491)
# this is image has to be downloaded  before executing
screen.bgpic("blank_states_img.gif")

play_is_on = True
while len(myTurtle.correct_list) < 50:
    user_answer = screen.textinput(f"{len(myTurtle.correct_list)}/50 States_Correct", "What's another State Name")
    myTurtle.is_state_exist(user_answer.title())

screen.exitonclick()
