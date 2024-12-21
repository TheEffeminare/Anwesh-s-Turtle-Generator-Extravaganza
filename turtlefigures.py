from turtle import *
import random
import math



# binary tree
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end


# quadratic tree
def d(n, l, pen):
     # termination
     if n==0 or l<2:
          return
     # edif
     pen.forward(l)
     pen.left(90)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)
#end d


# fern
def f(n, l, pen):
     # termination
     if n==0 or l<2:
          return
     # edif
     pen.forward(0.3*l)
     pen.right(45);f(n-l, l/2, pen);pen.left(45)
     pen.forward(0.7*l)
     pen.left(30);f(n-l, l/2, pen);pen.right(30)
     pen.forward(l)
     pen.right(10);f(n-l, 0.8*l, pen);pen.left(10)
     pen.backward(2*l)
#end d


def koch(n,l, pen):
    if n==0 or l<2:
       pen.forward(l)
       return

    koch(n-1, l/3, pen)
    pen.left(60); koch(n-1, l/3, pen)
    pen.right(120); koch(n-1, l/3, pen)
    pen.left(60); koch(n-1, l/3, pen)


def antiflake(n,l,pen):
     for i in range (3):
          koch(n,l,pen)
          pen.left(120)
     #endfor
     #endantiflake


def flake(n,l,pen):
     for i in range (3):
          koch(n,l,pen)
          pen.right(120)
     #endfor
     #endflake



def gasket3(n,l,pen):
   #termination
    if n==0 or l<2:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        #end for
        return
    #endif

    gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
    gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
    gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
#end of gasket3



#Georgian flag
def gasket4(n,l,pen):
     #termination
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #end for
          return
     #endif

     #gasket4(n-1,l)
     gasket4(n-1,l/3,pen);pen.forward(l);pen.left(90)
     gasket4(n-1,l/3,pen);pen.forward(l);pen.left(90)
     gasket4(n-1,l/3,pen);pen.forward(l);pen.left(90)
     gasket4(n-1,l/3,pen);pen.forward(l);pen.left(90)
#end of gasket4



def gasket5(n,l,pen):
#termination
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
               #end for
          return
     #endif
     else:
          for i in range(4):
               gasket5(n-1,l/3,pen);pen.forward(l/3)
               gasket5(n-1,l/3,pen);pen.forward(l/3);pen.forward(l/3)
               pen.right(90)
               #endfor

#end of gasket5



#Sierpinski's carpet
def gasket6(n,l,pen):
#termination
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
               #end for
          return
     #endif
     
     gasket6(n-1,l/3,pen);pen.forward(l/3)
     gasket6(n-1,l/3,pen);pen.forward(l/3);pen.forward(l/3)
     pen.left(90)

     gasket6(n-1,l/3,pen);pen.forward(l/3)
     gasket6(n-1,l/3,pen);pen.forward(l/3);pen.forward(l/3)
     pen.left(90)

     gasket6(n-1,l/3,pen);pen.forward(l/3)
     gasket6(n-1,l/3,pen);pen.forward(l/3);pen.forward(l/3)
     pen.left(90)

     gasket6(n-1,l/3,pen);pen.forward(l/3)
     gasket6(n-1,l/3,pen);pen.forward(l/3);pen.forward(l/3)
     pen.left(90)
#end of gasket6



#C-curve with gasket7(10,10)
def gasket7(n,l,pen):
#termination
     if n==0 or l<2:
          for i in range(2):
               pen.forward(l)
               pen.right(90)
               #end for
          return
     #endif
     
     gasket7(n-1,l,pen);pen.right(90)
     gasket7(n-1,l,pen);pen.left(90)
#gasket7 ends



#C-curve with gasket7(10,10)
def c2(n,r,pen):
#termination
     if n==0 or r<2:
          for i in range(2):
               pen.circle(r)
               #pen.left(90)
               #end for
          return
     #endif
     
     c2(n-1,r,pen)
     c2(n-1,r/2,pen);pen.left(90);pen.penup();pen.forward(2*r)
     pen.left(90);pen.pendown();c2(n-1,r/2,pen);pen.left(90)
     pen.penup();pen.forward(2*r);pen.left(90);pen.pendown()

     #screen.update()    
#c2 ends



#c3 starts with c3(2,200)
def c3(n,r,pen):
     #termination
     if n==0 or r<2:
          for i in range(3):
               pen.circle(r)
               #pen.left(90)
               #end for
          return
     #endif


     x = 3*r//(2*math.sqrt(3)+3)
     tan = 3*r*(math.sqrt(3)+1)//(2*math.sqrt(3)+3) #tangent O1M + x

     c3(n-1,r,pen)
     c3(n-1,x,pen);pen.penup();pen.forward(0.922*r)
     pen.left(90);pen.forward(tan);pen.pendown()
     c3(n-1,x,pen)
     pen.left(90);pen.penup();pen.forward(4*x);pen.pendown()
     pen.left(90);c3(n-1,x)
     pen.penup();pen.forward(tan);pen.left(90);pen.forward(0.922*r);pen.pendown()
#c3 ends



def circle3(n,r,pen):
     #termination
     if n==0 or r<2:
          for i in range(3):
               pen.circle(r)
               #end for
          return
     #endif
     
     x = 3*r//(2*math.sqrt(3)+3)
     
     circle3(n-1,r,pen)
     circle3(n-1,x,pen);pen.penup();pen.left(90);pen.forward(x)
     pen.right(30);pen.forward(x);pen.pendown();pen.right(90)
     
     circle3(n-1,x,pen);pen.right(150);pen.penup()
     pen.forward(x);pen.left(30);pen.pendown();pen.right(180)
     
     circle3(n-1,x,pen);

     pen.penup();pen.right(90);pen.forward(x);pen.right(30)
     pen.forward(x);pen.pendown();pen.left(90)
#circle3 ends
     
     
def c4(n,r,pen):
     #termination
     if n==0 or r<2:
          for i in range(4):
               pen.circle(r)
               #end for
          return
     #endif

     x=math.sqrt(2)*r
     c4(n-1,r,pen)

     c4(n-1,r/2,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     c4(n-1,r/2,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     c4(n-1,r/2,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     c4(n-1,r/2,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
#c4 ends



def circle4(n,r,pen):
     #termination
     if n==0 or r<2:
          for i in range(4):
               pen.circle(r)
               #end for
          return
     #endif

     x=math.sqrt(2)*r
     circle4(n-1,r,pen)

     circle4(n-1,r/2.4,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     circle4(n-1,r/2.4,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     circle4(n-1,r/2.4,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
     circle4(n-1,r/2.4,pen);pen.left(45);pen.penup();pen.forward(x)
     pen.left(45);pen.pendown()
#circle4ends


def hexagon(n,l,pen):
     #termination
     if n==0 or l<2:
          for i in range(6):
               pen.forward(l)
               pen.left(60)
          #end for
          return
     #endif

     #hexagon(n-1,l,pen)
     for i in range(6):
          hexagon(n-1,l/3,pen);pen.forward(2*l/3)
          hexagon(n-1,l/3,pen);pen.forward(l/3);pen.left(60)
#hexagon ends


# PERSONAL FRACTALS BEGIN
# personal fractal_1
def annu_mandala(n,r,pen): #n being the depth and r being the radius
    
    #termination
    if n==0 or r<2:
        return
    #end if

    #pick a random color
    #pen.color(rand_color())
    for i in range(6):
        pen.circle(r)
        annu_mandala(n-1,r/2,pen)
        pen.left(60)
        #screen.update()
    #end for


# personal fractal_2
def square_mandala(n,l,pen): #n being the depth and r being the radius
    
    #termination
    if n==0 or l<2:
        return
    #end if

    #pick a random color
    #pen.color(rand_color())
    for i in range(6):
        pen.forward(l) # Forward turtle by l units
        pen.left(90) # Turn turtle by 90 degree
 
        # drawing second side
        pen.forward(l) # Forward turtle by l units
        pen.left(90) # Turn turtle by 90 degree
 
        # drawing third side
        pen.forward(l) # Forward turtle by l units
        pen.left(90) # Turn turtle by 90 degree
 
        # drawing fourth side
        pen.forward(l) # Forward turtle by l units
        pen.left(90)
        
        square_mandala(n-1,l/2,pen)
        pen.left(60)
    #end for 
# square_mandala ends



# personal fractal_3
def bindi_stack(n,r,pen): #n being the depth and r being the radius
    
    #termination
    #experimenting with fill_color function here
    if n==0 or r<2:
        for i in range(3):
            pen.fillcolor(rand_color()) #pick a random color
            pen.begin_fill()
            pen.circle(r)
            pen.end_fill()
            return
        #endfor
    #end if

    
    #x = 3*r//(2*math.sqrt(3)+3)

    a = r/math.sqrt(2) #length of square formed inside subsequent smaller circles
    #radius of smaller circle is r/2


    bindi_stack(n-1,r,pen);pen.left(45);pen.penup();pen.forward(a);pen.pendown();pen.right(45)
    bindi_stack(n-1,r/2,pen);pen.left(180);pen.penup();pen.forward(r);pen.pendown();pen.right(180)
    bindi_stack(n-1,r/2,pen);pen.penup();pen.left(45);pen.forward(a);pen.left(45);pen.forward(1.1*r/3);pen.pendown();pen.right(90)
    bindi_stack(n-1,r/2,pen);pen.right(90);pen.penup();pen.forward((1.1*r/3)+r);pen.pendown();pen.left(90)
# bindi_stack ends

    

# personal fractal_4, is a variant of the previous fractal
def bindi_stack2(n,r,pen): #n being the depth and r being the radius
    
    #termination
    if n==0 or r<2:
        for i in range(3):
            pen.fillcolor(rand_color()) #pick a random color
            pen.begin_fill()
            pen.circle(r)
            pen.end_fill()
            return
        #endfor
    #end if

    
    #x = 3*r//(2*math.sqrt(3)+3)

    y = math.sqrt(2)*r

    #pick a random color
    #pen.color("black")
    bindi_stack2(n-1,r,pen);pen.left(45);pen.penup();pen.forward(y);pen.pendown();pen.left(45)
    bindi_stack2(n-1,r/2,pen);pen.left(90);pen.penup();pen.forward(r);pen.pendown();pen.right(90)
    bindi_stack2(n-1,r/2,pen);pen.penup();pen.forward(1.1*r/3);pen.pendown();pen.right(90)
    bindi_stack2(n-1,r/2,pen);pen.right(90);pen.penup();pen.forward((1.1*r/3)+r);pen.pendown();pen.left(90)

# bind_stack2 ends


# experimenting with random package, also to observe the turtle changing colors    
def rand_color():
    
    #colors = ["blue", "red", "yellow"] #primary colors only for a Mondrian inspired look
    colors = ["cyan", "magenta", "gray"]
    return random.choice(colors)





         
        



     
     
