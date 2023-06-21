from  turtle import *

speed('fastest')


distance = 100
sides =6
for i in  range(sides):
     pencolor('red')
     fd(distance)
     rt(360/sides)
     circle(distance/2)
     for i in range(sides):
         pencolor('blue')
         fd(distance/2)
         rt(360/sides)
         dot(10)
         write(i)
         for i in range(sides):
             pencolor('green')
             fd(distance/4)
             rt(360/sides)
         
         
hideturtle()
mainloop()