import turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-760,380)
t.speed(50)

for i in range(76):
  t.write(i)
  t.rt(90)
  t.fd(5)
  t.pd()
  t.fd(760)
  t.pu()
  t.bk(765)
  t.lt(90)
  t.fd(20)