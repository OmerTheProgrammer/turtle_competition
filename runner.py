import turtle
import random
import time

import board
import players_genertator
#צריך לסדר את הצבעים - class turtle - פיתרון אפשרי
#t.color() - בהדפסה זה הצב
def text_screen(text,color):
  text_turtle.hideturtle()
  players_genertator.go_to(text_turtle,0,-20)
  text_turtle.color(color)
  text_turtle.write(text,False,"center",("Arial", 30, "normal"))
  print(text)
  time.sleep(1)

global turtles
global player_number
global text_turtle
turtles = []
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
player_number = int(input("how many players?:"))
if player_number > 10:
  print("too much")
  player_number = 10
elif player_number <= 1:
  print("too little")
  player_number = 2

text_screen("Ready?", "brown")
turtles = players_genertator.player_orderer(player_number,turtles)
text_turtle.clear()
text_screen("Set!", "brown")
for i in turtles:
  i.showturtle()
  i.speed(3)
time.sleep(1)
text_turtle.clear()
text_screen("Go!", "brown")
text_turtle.clear()

turn = turtles[0]
while turn.pos()[0] < 745:
  for turn in turtles:
    turn.forward(random.randint(1,12))
    if turn.pos()[0] > 745:
      text_screen(turn.color()[0] + " won!", turn.color()[0])
      break
time.sleep(4.8)
