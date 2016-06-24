######################################################
#FILE: HelloTurtle.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex1 2014-2015
#DESCRIPTION:
#A program that draws some simple geometric shapes on the screen
# and prints "HelloTurtle!", using Turtle graphics.
#######################################################
import turtle

#title for the display window
turtle.title("Fun with Turtle Graphics and Python")
turtle.up()              #lift pen up, no drawing
turtle.goto(-100, -100)  #Move turtle to the absolute position (-100,-100)
turtle.down()            #pen is down, drawing now


turtle.color("red")        #Makes the squre's color red
turtle.goto(-100,-100)     #starting point at the left bottom corner 
turtle.down()              #starts drawing now
turtle.goto(100,-100)      #go to the right bottom corner
turtle.goto(100,100)       #go up to the right upper corner
turtle.goto(-100, 100)     #go to the left upper corner
turtle.goto(-100, -100)    #finish at the start point.
turtle.up()                #lift pen, stop drawing
turtle.goto(0,-100)        #go to this point
turtle.color("orange")     #Make it in the color orange
turtle.down()              #starts drawing now
turtle.circle(100)         #makes a round within radius 100
turtle.up()                #lift pen, stop drawing
turtle.goto(0,-200)        #go to this point
turtle.color("blue")       #Make it in the color blue
turtle.down()              #starts drawing now
turtle.goto(200,0)         #go up to the right
turtle.goto(0,200)         #go up to the left
turtle.goto(-200,0)        #go down to the left
turtle.goto(0,-200)        #go down to the right, to the starting point
turtle.up()                #lift pen, stop drawing
turtle.goto(-70,-5)        #go to the strating point
turtle.color("green")      #write in the color green
#write "Hello World! in this font and size
turtle.write("Hello Turtle!", font=("Arial", 20, "normal"))  
turtle.done()               #finish 

