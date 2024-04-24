import random
import turtle
import time 

WIDTH,HEIGHT = 500,500
COLORS = ["red","black","pink","blue","yellow","orange","purple","violet"]

def get_racers():
    racers = 0
    while True:
        racers = input("Enter number of turtle racers(2-8): ")
        if racers.isdigit():
           racers = int(racers)
        else:
            print("\nEnter a valid number")
            continue 
        if 2 <= racers <= 10:
            return racers
        else:
            print("\nNot in range of players (2-8).")

def race(colors):
  turtles = create_turtle(colors)

  while True:
      for racer in turtles:
          distance = random.randrange(1,10)
          racer.forward(distance)

          x,y = racer.pos()
          if y >= HEIGHT // 2 - 20:
              return colors[turtles.index(racer)]


def create_turtle(colors):
  turtles = []
  spacingx = WIDTH // (len(colors)+ 1)
  for i, color in enumerate(colors):
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.left(90)
    racer.penup()
    racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
    racer.pendown()
    turtles.append(racer)
  return turtles


def call_turtles():
  screen = turtle.Screen()
  screen.setup(WIDTH,HEIGHT)
  screen.title("Turtle Racing")

racers = get_racers()
call_turtles()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is:", winner)
time.sleep(5)