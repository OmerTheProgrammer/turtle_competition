# 1. --- GET PLAYER INPUT FIRST (NO IMPORTS YET) ---
# Get player number input before any graphics initialization
try:
  player_number_str = input("how many players?:")
  player_number = int(player_number_str)
except ValueError:
  print("Invalid input. Defaulting to 2 players.")
  player_number = 2

if player_number > 10:
  print("too much. Limiting to 10 players.")
  player_number = 10
elif player_number <= 1:
  print("too little. Setting to 2 players.")
  player_number = 2

# 2. --- NOW IMPORT MODULES (WHICH INCLUDES TURTLE) ---
import turtle
import random
import time

# Import board and players_genertator (these depend on turtle)
import board
import players_genertator


# 3. --- Screen Setup ---
# Initialize the screen immediately after the input is done
# If the window appeared earlier, this command ensures it is correctly configured now.
screen = turtle.Screen()
screen.setup(width=1600, height=800)
screen.title("Python Turtle Race")
screen.colormode(255) # Good practice for more color control
# --- End Screen Setup ---


# Initialize the turtle used for text display
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
turtles = [] # Initialize list for player turtles

#צריך לסדר את הצבעים - class turtle - פיתרון אפשרי
#t.color() - בהדפסה זה הצב
def text_screen(text, color):
  """Displays a message in the center of the screen."""
  text_turtle.hideturtle()
  players_genertator.go_to(text_turtle, 0, -20)
  text_turtle.color(color)
  # Write the text
  text_turtle.write(text, False, "center", ("Arial", 30, "normal"))
  print(text)
  time.sleep(1)
  text_turtle.clear() # Clear the text after the delay for the next message/race

# Game start sequence
board.draw_board()
text_screen("Ready?", "brown")
turtles = players_genertator.player_orderer(player_number, turtles)
text_screen("Set!", "brown")
for i in turtles:
  i.showturtle()
  i.speed(3)
time.sleep(1)
text_screen("Go!", "brown")


# --- Fixed Race Logic ---
is_running = True
winner_turtle = None
finish_line_x = 745 # The finish line coordinate

while is_running:
  for turn in turtles:
    # Move the turtle forward by a random distance (1 to 12)
    turn.forward(random.randint(1, 12))
    
    # Check if the current turtle crossed the finish line
    if turn.pos()[0] > finish_line_x:
      winner_turtle = turn
      is_running = False # Stop the main while loop
      break # Stop the inner for loop (no need to move other turtles)

# Display the winner outside the main race loop
if winner_turtle:
  # The color() method returns a tuple (pencolor, fillcolor). We use index 0.
  winner_color = winner_turtle.color()[0]
  text_screen(winner_color + " won!", winner_color)

# Wait a moment, then close the window gracefully
time.sleep(1) 

# --- Keep the window open ---
# This command keeps the turtle graphics window open until the user closes it.
turtle.done()