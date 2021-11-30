import turtle

def print(n):
    if(n==0):
        return 0
    bob.left(170)
    bob.forward(200)
    print(n-1)
        
    
if __name__=='__main__':
    
    bob=turtle.Turtle()
    bob.color("red","yellow")
    bob.speed(10)
    
    bob.begin_fill()
    bob.forward(200)
    bob.left(170)
    bob.forward(200)


    print(50)
    bob.end_fill()


turtle.done()
