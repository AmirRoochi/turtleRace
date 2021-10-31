from turtle import Turtle, Screen
import random
s = Screen()
s.colormode(255)
s.setup(500, 400)


def race():
    result = []
    t_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    ans = s.textinput(title="Make your Bet!", prompt="which color will win the race? Choose a rainbow color: ")
    players = []
    orig = -130
    should_continue = True
    liner = Turtle()
    liner.penup()
    liner.goto(230, 190)
    liner.setheading(270)
    liner.pendown()
    liner.forward(380)
    liner.hideturtle()
    for i in range(6):
        t = Turtle('turtle')
        t.speed('slowest')
        t.penup()
        t.color(t_colors[i])
        t.goto(-230, orig)
        orig += 50
        players.append(t)
    while should_continue:
        for player in players:
            player.forward(random.randint(0, 10))
            if player.xcor() >= 228:
                result.append(player.pencolor())
                should_continue = False
    winner = result[0]
    if winner == ans:
        print(f"The winner is: {winner}, you win.")
    else:
        print(f"The winner is {winner}, you lose.")


race()
s.exitonclick()
