import turtle
def square(sam):
     for i in range(1,3):
      sam.forward(50)
      sam.right(60)
     sam.forward(50)
def art():
 window=turtle.Screen()
 window.bgcolor("blue")
 sam=turtle.Turtle();
 for i in range(1,36):
   square(sam)
   sam.right(10)
 
 #kani=turtle.Turtle()
 #kani.shape('turtle')
 #while(i<3):
 
    
   # sam.forward(10)
    #sam.right(90)
   
 window.exitonclick()
art()
