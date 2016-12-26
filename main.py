# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(150)

# Draw Romb
n = 20
fill_color = { 
  1 : "red",
  2 : "darkblue",
  3 : "green",
  4 : "yellow",
  5 : "blue",
  6 : "cyan",
  7 : "pink",
  8 : "orange",
  9 : "violet" ,
  0 : "red"
}

def list_gen(*args):
  a = args[::-1]
  return args+a
  
step = list_gen(2, 1, 1, 1, 1, 9, 8, 4)
step1 = []

tommy.goto(0, 0)
tommy.setheading(0)

k = len(step)
tommy.penup()
tommy.backward(k*n)
while k >=1:
  for i in range(1,k):
    draw_romb(tommy, fill_color[step[i-1]], 180, n)
    run(tommy, 108, 108, n)
  
  draw_romb(tommy, fill_color[step[-1]], 180, n)
  
  for i in range(1,k):
    draw_romb(tommy, fill_color[step[i-1]], 108, n)
    run(tommy, 36, 108, n)
    
  draw_romb(tommy, fill_color[step[-1]], 108, n)
  
  for i in range(1,k):
    draw_romb(tommy, fill_color[step[i-1]], 36, n)
    run(tommy, 324, 108, n)
    
  draw_romb(tommy, fill_color[step[-1]], 36, n)
  
  for i in range(1,k):
    draw_romb(tommy, fill_color[step[i-1]], 324, n)
    run(tommy, 252, 108, n)
    
  draw_romb(tommy, fill_color[step[-1]], 324, n)
  
  for i in range(1,k):
    draw_romb(tommy, fill_color[step[i-1]], 252, n)
    run(tommy, 180, 108, n)
    
  draw_romb(tommy, fill_color[step[-1]], 252, n)
  
  k -= 1
  for i in range(len(step)-1):
    step1.append(step[i]+step[i+1])
    if step1[-1] >= 10:
      a = str(step1[-1])
      a = int(a[0])+int(a[1])
      step1[-1] = a
  step = step1
  step1 = []
  tommy.penup()
  tommy.forward(n)

tommy.penup()
tommy.goto(0, 0)
tommy.ht()
input()