import turtle

def draw_board():
  """Draws the racetrack and number markings."""
  # Create a dedicated turtle for drawing the board
  t = turtle.Turtle()
  t.hideturtle()
  t.penup()
  t.goto(-760,380) # Start top left
  t.speed(50)

  # Draw the track markings
  for i in range(76):
    t.write(i)
    t.rt(90)
    t.fd(5)
    t.pd()
    t.fd(760) # Draw the line down
    t.pu()
    t.bk(765) # Return to the start marker
    t.lt(90)
    t.fd(20) # Move to the next column position