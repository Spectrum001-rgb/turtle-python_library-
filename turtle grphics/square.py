import turtle

bob=turtle.Turtle()

bob.color("blue","cyan") #makes the cursor color red


bob.begin_fill() #begin_fill should be included in the start and end_fil in the last to color
#the whole object .

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

#bob.end_fill()

bob.penup()  #this function acts like ink remover
bob.forward(150)
bob.pendown() #this acts like the pen is downon the gui again

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.end_fill()

turtle.done()