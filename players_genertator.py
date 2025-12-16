import turtle
import time

def go_to(t,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
def number_check(player_number):
  if player_number == 2:
    return 690
  if player_number == 3:
    return 360
  if player_number == 4:
    return 240
  if player_number == 5:
    return 180
  if player_number == 6:
    return 140
  if player_number == 7:
    return 110
  if player_number == 8:
    return 100
  if player_number == 9:
    return 90
  if player_number == 10:
    return 80

def player_generator(color,y):
  t = turtle.Turtle()
  t.hideturtle()
  t.color(color)
  t.shape('turtle')
  go_to(t, -760, y)
  return t

def player_orderer(player_number,turtles):
  colorss = [[],["red","green","orange","yellow","peru","lime green","cyan","medium blue","dim gray","teal"]]
  ys = {'y':-360,"vy":0}
  ys["vy"] = number_check(player_number)
  for i in colorss[1]:
    if player_number >= colorss[1].index(i)+1:
      colorss[0].append(i)
  for i in colorss[0]:
    turtles.append(player_generator(i,ys['y']))
    ys['y'] += ys["vy"]
  return turtles