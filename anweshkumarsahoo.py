from tkinter import *
import tkinter as tk
from tkinter import ttk
import turtlefigures
from turtle import RawTurtle, TurtleScreen
import math
import random


'''
# I have restrcutured the code for easier understanding
# This is where I define all my functions. There are two major frames/panels. Canvas to the left and control panel to the right.
# To differentiate functions from variables, all functions are snake_cased, while variables are camelCased.
'''
penColor = "blue"
penThickness = 3
turtleShape = "turtle"
# ^I'm using these variables to initiate their corresponding values, so I can use them for clearing the canvas and resetting the turtle later

def initialize_turtle():
    global pen, penColor, penThickness, turtleShape  # Declaring them as global to access in the outer scope
    if pen:
        pen.hideturtle()  # Hiding the previous turtle
        screen.clear()
    pen = RawTurtle(screen)  # Creating a new turtle instance
    pen.speed(0)
    pen.width(penThickness)  # Setting the pen thickness
    pen.color(penColor)  # Setting the pen color
    pen.shape(turtleShape)  # Setting the turtle shape
    reset_turtle_position()
    pen.penup()
    pen.showturtle()

def reset_turtle_position():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()



'''
# This is an important function, since I'm using the clear button to hide the previous turtle
and initiate a new turtle with the same features (color, width and shape), at position (0,0)
Using this, even when the user has started a drawing, the user can clear the drawing mid-way and start
another fresh fractal.
'''
def clear_canvas():
    screen.clear()
    pen.hideturtle()
    pen.penup()
    global penColor, penThickness, turtleShape
    orderStr.set("")
    lengthStr.set("")
    reset_turtle_position()
    
    # Clear the turtle's drawings
    pen.clear()
    pen.goto(0, 0)
    pen.penup()
    
    penColor = colorVar.get()  # Storing the current pen color
    penThickness = penThickVar.get()  # Storing the current pen thickness
    turtleShape = turtleShapeVar.get()  # Storing the current turtle shape
    
    update_penColor(None)
    update_pen_width(penThickness)
    update_turtleShape()
    
    initialize_turtle()



def draw_fractal():
    
    reset_turtle_position()
    order = int(orderStr.get())
    length = int(lengthStr.get())

    figure_index = figureNames.index(figureStr.get())
    
    if figure_index == 0:
        pen.up()
        pen.backward(w / 2.1)
        pen.down()
        turtlefigures.tree(order, length, pen) #fractal1
       
    elif figure_index == 1:
        pen.up()
        pen.backward(w / 2.1)
        pen.down()
        turtlefigures.d(order, length, pen) #fractal2
        
    elif figure_index == 2:
        pen.up()
        pen.backward(w / 2.1)
        pen.down()
        turtlefigures.f(order, length, pen) #fractal3
        
    elif figure_index == 3:
        #pen.up()
        #pen.backward(w / 2.1)
        #pen.down()
        pen.up()
        pen.backward(w/6)
        pen.right(90)
        pen.forward(w / 5)
        pen.down()
        pen.left(90)
        turtlefigures.hexagon(order, length, pen) #fractal4
        
    elif figure_index == 4:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.antiflake(order, length, pen) #fractal5
        
    elif figure_index == 5:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.flake(order, length, pen) #fractal6
        
    elif figure_index == 6:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.gasket3(order, length, pen) #fractal7

        
    elif figure_index == 7:
        pen.up()
        pen.backward(w / 5)
        pen.down()
        turtlefigures.gasket4(order, length, pen) #fractal8
        
    elif figure_index == 8:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.gasket5(order, length, pen) #fractal9
        
    elif figure_index == 9:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.gasket6(order, length, pen) #fractal10
        
    elif figure_index == 10:
        pen.up()
        pen.backward(w / 6)
        pen.down()
        turtlefigures.gasket7(order, length, pen) #fractal11
        
    elif figure_index == 11:
        pen.up()
        pen.right(90)
        pen.forward(w / 4)
        pen.down()
        pen.left(90)
        turtlefigures.c2(order, length, pen) #fractal12
        
    elif figure_index == 12:
        pen.up()
        pen.right(90)
        pen.forward(w / 4)
        pen.down()
        pen.left(90)
        turtlefigures.circle3(order, length, pen) #fractal13
            
    elif figure_index == 13:
        pen.up()
        pen.right(90)
        pen.forward(w / 4)
        pen.down()
        pen.left(90)
        turtlefigures.circle4(order, length, pen) #fractal14
        
    elif figure_index == 14:
        turtlefigures.annu_mandala(order, length, pen) #fractal15
        
    elif figure_index == 15:
        turtlefigures.square_mandala(order, length, pen) #fractal16
        
    elif figure_index == 16:
        pen.up()
        pen.right(90)
        pen.forward(w / 3)
        pen.down()
        pen.left(90)
        turtlefigures.bindi_stack(order, length, pen) #fractal17
        
    elif figure_index == 17:
        pen.up()
        pen.right(90)
        pen.forward(w / 3)
        pen.down()
        pen.left(90)
        turtlefigures.bindi_stack2(order, length, pen) #fractal18
       




'''
def update_pen_width(value):
    pen.width(value)
'''
# Function to update the pen thickness
def update_pen_width(value):
    global penThickness
    penThickness = value  # Storing the current pen thickness
    pen.width(penThickness)  # Setting the pen thickness

# Using a bunch of event handler functions here
def update_infoText(event): #Takes a single argument 'event'. The function is designed to respond to an event (e.g., a button click or menu selection)
    selectedInfo = infoDict.get(figureStr.get(), "Here is where you find more information on the chosen fractals. Choose a fractal from the tab or the drop down, and click draw to see the magic. :)")
    infoText.delete(1.0, END) 
    infoText.insert(END, selectedInfo)
# The green text is for when an error occurs, or if there's no data associated to a key in the dictionary.
# This is linked to the figureList option menu

def update_infoText_from_tab(event):
    selectedTab = notebook.index(notebook.select())
    selectedOption = figureNames[selectedTab]
    figureStr.set(selectedOption)
    update_infoText(None)

# Function to update the pen color
'''
def update_penColor(event):
    chosenColorName = colorVar.get()
    chosenColorValue = customColorsDict.get(chosenColorName)
    if chosenColorValue:
        pen.color(chosenColorValue)
        chosenColorLabel.config(text=f"Chosen Color: {chosenColorValue}") #for easier user understanding, the color value is shown here.
The following function is a variant of the above method. chosenColorValue is assigned to penColor variable instead.
'''
# Function to store user-selected pen color
def update_penColor(event):
    global penColor
    chosenColorName = colorVar.get()
    chosenColorValue = customColorsDict.get(chosenColorName)
    if chosenColorValue:
        penColor = chosenColorValue  # Storing the current pen color
    pen.color(penColor)  # Setting the pen color
    chosenColorLabel.config(text=f"Chosen Color: {penColor}")  # Updating the label


def update_option_from_tab(event):
    selectedTab = notebook.index(notebook.select())
    selectedOption = figureNames[selectedTab]
    figureStr.set(selectedOption)
    update_infoText(None)  # Calling the update_infoText function to update the information text

'''
def update_option_and_info(event):
    update_option_from_tab(event)  # Calling the function to update the dropdown selection
    update_infoText(event)  # Calling the function to update the information text

'''
# ^Tried working with a logic here that didn't work as planned. Letting this stay here as a future scope of work.




'''____________________________________________________________'''

# Creating a dictionary that maps custom color names to the real color values
customColorsDict = {
    'Blue da House Down Boots': 'blue',
    'Velvet Dream Violet': 'violet',
    'Bubblegum Bliss': 'pink',
    'Tangerine Tango': 'orange',
    'Red like Madonna': 'red', 
    'Yellow? I hardly know huh': 'yellow',
    'Kermit Green': 'green',
    # custom color mappings for a fun interface :)
}


# Extract the custom color names
extractColorKeys = list(customColorsDict.keys())
extractColorValues = list(customColorsDict.values())


# Creating 3 custom fonts
customFont = ("Helvetica", 16)
customFontTwo = ("Helvetica", 15)
customButtonFont = ("Helvetica", 20)



'''____________________________________________________________'''




# Making the interface
# Starting with creating the main window
root = Tk()
root.title("Turtle Fractals Generator")
root.geometry("1500x900+100+100")

titleText = "Welcome to Anwesh's Turtle Generator Extravaganza!\n"\
            "Get ready to embark on an artistic adventure, where math and imagination collide.\n"\
            "And where every click is a stroke of YAASSified tech genius. FAAAAAB no?" \


titleLabel = Label(root, text=titleText, font=customFont, wraplength=600, justify="left")
titleLabel.grid(row=0, column=0, rowspan=1, sticky="w", padx=15, pady=5) # stick to 'w'est

# pack and grid being two different geometry managers, and a 'Frame' being a container widget
# Canvas
canvasFrame = LabelFrame(root, text = "Canvas New", font=customFontTwo)
canvasFrame.grid(row=1, column=0, rowspan=7, padx=15, pady=5, sticky="n") # stick to 'n'orth
canvas = Canvas(canvasFrame, width=680, height=680)
canvas.pack()

screen = TurtleScreen(canvas)
screen.bgcolor("white")
w, h = screen.screensize()

pen = RawTurtle(screen)
pen.speed(0)
pen.width(3)
pen.color("blue")
reset_turtle_position()


# Control Panel
controlFrame = LabelFrame(root, text = "Control Panel", font=customFontTwo)
# controlFrame = LabelFrame(root, text="Control Panel", borderwidth=2, relief="raised")
# ^I could experiment with flat, groove, raised, ridge, solid, or sunken as values for relief
controlFrame.grid(row=1, column=1, rowspan=7, padx=15, pady=5, sticky="NW") #stick to 'n'orth 'w'est

orderLabel = Label(controlFrame, text="Order : ", font=customFontTwo)
orderLabel.grid(row=1, column=0, padx=5, pady=5, sticky="NW")

orderStr = StringVar()
orderEntry = Entry(controlFrame, textvariable=orderStr)
orderEntry.grid(row=1, column=1, columnspan=2, padx=15, pady=5, sticky="NW")

lengthLabel = Label(controlFrame, text="Length : ", font=customFontTwo)
lengthLabel.grid(row=2, column=0, padx=5, pady=5, sticky="NW")

lengthStr = StringVar()
lengthEntry = Entry(controlFrame, textvariable=lengthStr)
lengthEntry.grid(row=2, column=1, columnspan=2, padx=15, pady=5, sticky="NW")

dropdownLabel = Label(controlFrame, text="Choose your Fractal : ", font=customFontTwo)
dropdownLabel.grid(row=3, column=0, padx=5, pady=5, sticky="NW")

figureNames = ["Binary Tree", "Dandelion", "Fern", "Honeycomb-STAR", "AntiFlake", "Snowflake", "Gasket3", "Georgian Flag", "MazeMorph", "Sierpinski's Carpet", "C-Curve", "Twice The Circle", "Thrice The Circle", "Quadruply Circle", "Circular Mandala", "Square Mandala", "Bindi Pyramid", "Bindi Pyramid Variant"]
figureStr = StringVar()
figureList = OptionMenu(controlFrame, figureStr, *figureNames, command=update_infoText)
figureList.grid(row=3, column=1, columnspan=6, padx=15, pady=5, sticky="NW")


# Pen Thickness
penThickLabel = Label(controlFrame, text="Pen Thickness : ", font=customFontTwo)
penThickLabel.grid(row=4, column=0, padx=5, pady=20, sticky="NW")

penThickVar = IntVar()
penThickScale = Scale(controlFrame, from_=1, to=10, orient=HORIZONTAL, variable=penThickVar,
                            command=lambda val=penThickVar: update_pen_width(val)) #creating the scroller widget
penThickScale.grid(row=4, column=1, columnspan=5, padx=15, pady=5, sticky="NW")
penThickScale.set(2)  # Initial thickness



# Choose a Pen Color
# Color Label
colorLabel = Label(controlFrame, text="Pen Color : ", font=customFontTwo)
colorLabel.grid(row=5, column=0, padx=5, pady=5, sticky="NW")

# Color Dropdown with custom color names
colorVar = StringVar()
colorDropdown = OptionMenu(controlFrame, colorVar, *extractColorKeys, command=update_penColor)
colorDropdown.grid(row=5, column=1, columnspan=3, padx=12, pady=5, sticky="NW")
colorVar.set(extractColorKeys[0])  # Setting an initial custom color

chosenColorLabel = Label(controlFrame, text="Chosen Color: " + extractColorValues[0], font=customFontTwo)
chosenColorLabel.grid(row=5, column=2, columnspan=3, padx=50, pady=5, sticky="NW")




# Create a list of available turtle shapes + apply button
turtleShapesList = ["turtle", "classic", "arrow", "square", "triangle"]

turtleShapeLabel = Label(controlFrame, text="Turtle Shape : ", font=customFontTwo)
turtleShapeLabel.grid(row=6, column=0, padx=5, pady=5, sticky="NW")

turtleShapeVar = StringVar()
turtleShapeDropdown = OptionMenu(controlFrame, turtleShapeVar, *turtleShapesList)
turtleShapeDropdown.grid(row=6, column=1, columnspan=2, padx=12, pady=5, sticky="NW")
turtleShapeVar.set("turtle")  # Set an initial turtle shape

# Function to update the turtle shape
'''
def update_turtleShape():
    selectedTurtleShape = turtleShapeVar.get()
    pen.shape(selectedTurtleShape)
Again, reworked this function below to initiate with a turtleShape variable instead.
'''
# Function to update the turtle shape
def update_turtleShape():
    global turtleShape
    turtleShape = turtleShapeVar.get()
    pen.shape(turtleShape)
update_turtleShape()  # Set the initial turtle shape

# Creating the Apply Button
turtleShapeButton = Button(controlFrame, text="Apply", command=update_turtleShape)
turtleShapeButton.grid(row=6, column=1, columnspan=3, padx=125, pady=1, sticky="NW")


'''____________________________________________________________'''


# Reference from what was done in the class
# Clear and Draw buttons
#clearButton = Button(controlFrame, text="Clear", command=clear_canvas)
#clearButton.grid(row=13, column=0, columnspan=3)

#drawButton = Button(controlFrame, text="Draw", command=draw_fractal)
#drawButton.grid(row=13, column=3, columnspan=3)


# Creating the "Draw" button with a larger font size and a different color
drawButton = Button(
    controlFrame,
    text="DRAW",
    command=draw_fractal,
    font=customButtonFont,  # Apply the custom font
    #bg='#fff',
    width=10,  # Adjust the width
    height=2,  # Adjust the height
    fg="green",  # Change the text color
)

drawButton.grid(row=7, column=1, columnspan=3, padx=0, pady=30)

clearButton = Button(
    controlFrame,
    text="CLEAR",
    command=clear_canvas,
    font=customButtonFont,  # Apply the custom font
    width=10,  # Adjust the width
    height=2,  # Adjust the height
    fg="magenta",  # Change the text color
)

clearButton.grid(row=7, column=0, columnspan=3, padx=170, pady=30, sticky="w")
#clearButton.grid(row=7, column=1, columnspan=3, padx=0, pady=30)

'''____________________________________________________________'''



# Info Dialog Box
infoLabel = Label(controlFrame, text="More on the Fractal :", relief="flat", font=customFontTwo)
infoLabel.grid(row=11, column=0, padx=5, pady=10, sticky="NW")

infoText = Text(controlFrame, height=9, width=58, font=customFontTwo, padx=10, pady=5)
infoText.grid(row=11, column=1, columnspan=3, padx=10, pady=10, sticky=W)

# Information for the tabs
infoDict = {
    "Binary Tree": "Here's all about Binary Tree fractal. It's a fascinating fractal with many interesting properties."
                  " You can explore its intricate patterns and self-similarity in more detail by updating its order and length.\n\n"
                    "For best results you could try with order set to 10 and length set to 250.",
    
    "Dandelion": "Here's all about Dandelion fractal.The Dandelion fractal is known for its delicate and intricate structure."
                  " You can delve deep into its beauty and intricacy, by analysing its mathematical characteristics or by simply changing its length and order.\n\n"
                    "For best results you could try with order set to 6 and length set to 250.",
    
    "Fern": "Here's all about Fern fractal. The Fern fractal is a classic example of self-replicating patterns in nature."
                  " Explore the elegance behind its formation and discover its aesthetic appeal by updating its order and length.\n\n"
                    "For best results you could try with order set to 6 and length set to 250.",
    
    "Honeycomb-STAR": "Here's all about Honeycomb-STAR fractal. This super interesting fractal is achieved by creating a bunch of hexagons."
                    " You can always have fun with this fractal by changing the pen color mid-way in fact. :)\n\n"
                    "For fastest results you could try with order set to 2 and length set to 200.",
    
    "AntiFlake": "Here's all about he Antiflake fractal. A variant inspired by the Koch-curve."
                    " Also known as the Koch snowflake, the Koch-curve is a fascinating and beautiful fractal pattern named after the Swedish mathematician Helge von Koch.\n\n"
                    "It is constructed by recursively dividing a line segment into smaller segments and replacing the middle portion with an equilateral triangle."
                    "This is just a triangular variant of the same. Use order 3 and length 200 for a pretty and quick fractal.",
    
    "Snowflake": "Here's all about the Snowflake fractal, which is essentially a variant of the Koch Curve."
                " Also known as the Koch snowflake, the Koch-curve is a fascinating and beautiful fractal pattern named after "
                    "the Swedish mathematician Helge von Koch.\n\n"
                    "It is constructed by recursively dividing a line segment into smaller segments and replacing the middle portion"
                    " with an equilateral triangle."
                    " This one's in the shape of a snowflake. Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Gasket3": "Here's all about Gasket Three or the Sierpinski Triangle. It's the *fractal snack* of the math world!"
                " Like nibbling away at a giant triangle-shaped cracker, the Sierpinski Triangle is a quirky math muncher."
                " Start with a triangle, take a bite out of the middle, and repeat. Voilà!"
                " Triangles inside triangles, inside triangles, inside triangles, it's like an endless food attack on you...."
                " Well, you get the point! 😋🔺\n\n"
                "Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Georgian Flag": "Imagine a fractal that dances like the vibrant stripes of the 'Georgian flag'."
                    " It's a geometric fiesta, where triangles multiply and twirl in a patriotic parade.\n\n"
                    "This fractal is like a math-powered carnival of red and white, celebrating the spirit of Georgia!"
                    " Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "MazeMorph": "Here's all about MazeMorph, Gasket Five or the Labyrinth inspired fractal. Picture a whimsical fractal that's like an ever-twisting maze of mathematical mirth."
                " It's a journey through geometric wonderland, where corridors of complexity lead to laughter."
                " This fractal is your very own mathematical adventure, where every twist and turn unravels a riddle of fun!\n\n"
                "Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Sierpinski's Carpet": "Picture a never-ending magic carpet ride for your imagination."
                    " Our fractal, inspired by Sierpinski's Carpet, is like a whimsical, infinitely detailed rug."
                    " Just keep zooming in, and you'll discover a tiny universe hiding in every fiber, a true fractal wonderland!\n\n"
                "Use order 3 and length 200 for a quick yet beautiful fractal.",

    
    "C-Curve": "Here's all about the C-Curve fractal."
                " Imagine a doodle gone wild! Our C-curve-inspired fractal is like a rollercoaster for your pencil. It starts with a single squiggle,"
                " then spirals into an intricate, twisty adventure that leaves you wondering which way is up. You'll be lost in its scribbly charm!\n\n"
                "Use order 10 and length 10 for a quick yet beautiful fractal.",

    
    "Twice The Circle": "Here's all about 'Twice the Circle' Fractal."
                        " Meet the 'Circles in Harmony' fractal, where circles unite in a mesmerizing dance within a bigger circle."
                        " Like synchronized swimmers, these concentric circles gracefully twirl and twinkle,"
                        " creating a hypnotic spectacle that's both soothing and enchanting."
                        " It's the art of geometry in motion!\n\n"
                        "Use order 3 and length 200 for a quick yet beautiful fractal.",

    
    "Thrice The Circle": "Here's all about the Apollonian Gasket. Step into the 'Infinite Mirror Realm'"
                        " fractal, where circles forever reflect and refract, like an optical illusion that plays tricks on your eyes. "
                        "In this kaleidoscopic wonderland,"
                        " each circle nestles snugly within others, creating an endless cascade of patterns, "
                        "just waiting for your imagination to dive in and explore.\n\n"
                        "Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Quadruply Circle": "Here's all about Quadruply Circular Fractal. Behold the 'Quadruple Enigma' fractal, "
                        "a mesmerizing dance of circles within circles, like a puzzle only the universe can solve. Four enigmatic "
                        "circles snugly embrace a central mystery, creating a symphony of shapes that'll leave you "
                        "pondering the secrets of geometry and infinity.\n\n"
                        "Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Circular Mandala": "Here's all about my Circular Floral Mandala."
                        " Introducing the 'Blossom Rangoli' fractal, where mathematics meets nature in a"
                        " splendid display of petal-like patterns. Observe as elaborate floral designs blossom and merge, transforming into a captivating garden that never fades.."
                        " It's a beauty worth thousand roses, carved by the hand of fractal artistry.\n\n"
                        "Use order 4 and length 170 for a quick yet beautiful Circular Mandala fractal.",
    
    "Square Mandala": "Welcome to my Mandala Universe."
                        " Here comes the 'Square Petal Symphony' fractal, where squares become delicate petals, "
                        "dancing in harmonious patterns. Nature's geometry emerges in a floral masterpiece with each iteration, "
                        "as if a garden of mathematical blooms have sprung to life.\n\n"
                        "It's a whimsical fusion of art and mathematics, where symmetry meets botanical elegance. 🌸🌻🌼"
                        " Use order 4 and length 190 for a quick yet beautiful Circular Mandala fractal.",
    
    "Bindi Pyramid": "Here's all about Bindi Pyramid."
                    " Introducing the 'Bindi Pyramid' fractal, a mesmerizing blend of ancient tradition and geometric artistry. "
                    "Like a pyramid adorned with vibrant Indian bindis, each iteration unveils a kaleidoscope of colors and patterns, "
                    "paying homage to the beauty of my cultural heritage. \n\n"
                    "It's a captivating journey where the mystical allure of *tikili* or bindis meets the precision of fractal geometry, "
                    "creating a visual tapestry of mesmerizing beauty. 👁️🔺💠"
                    " Use order 3 and length 200 for a quick yet beautiful fractal.",
    
    "Bindi Pyramid Variant": "Here's more on Bindi Pyramid Variant fractal."
                            " Behold the 'Bindi Cascade,' a radiant variant of the pyramid-inspired fractal adorned with the "
                            "spirit of Indian bindis. As the bindis gracefully tumble down the geometric steps, "
                            "they create an enchanting dance of colors and culture, reminiscent of my mother's timeless elegance. This fractal "
                            "is a unique blend of tradition and innovation, offering a delightful visual symphony that pays homage "
                            "to the beauty of my heritage with a modern twist.\n\n"
                            "Use order 3 and length 200 for a quick yet beautiful fractal.",
}


# Using Notebook for (Tabs)
# Create a list of numbers from 1 to 18 as strings
tabNumbers = [str(i) for i in range(1, 19)]

# Update the figureStr variable to initially select the first tab (number 1)
figureStr.set(tabNumbers[0])

# Tab Label
tabLabel1 = Label(controlFrame, text="TAB Away! :)", font=customFontTwo)
tabLabel1.grid(row=9, column=0, columnspan=1, padx=5, pady=15, sticky="NW")

tabLabel2 = Label(controlFrame, text="Use the tabs from 1 through 18, to know more about its corresponding Fractal! :)", font=customFontTwo)
tabLabel2.grid(row=9, column=1, columnspan=6, padx=0, pady=15, sticky="W")

# Notebook (Tabs)
notebook = ttk.Notebook(controlFrame)
notebook.grid(row=10, column=0, columnspan=6, padx=10, pady=10, sticky="W")

# Create tabs with numbered labels
for number in tabNumbers:
    tab = Frame(notebook)
    notebook.add(tab, text=number)

# Bind the event to update the info text when the tab selection changes
notebook.bind("<<NotebookTabChanged>>", update_infoText_from_tab)
notebook.bind("<<NotebookTabChanged>>", update_option_from_tab)

# Set the initial info text based on the initial dropdown selection
initial_selectedInfo = infoDict.get(figureStr.get(), "Here is where you find more information on the chosen fractals. Choose a fractal from the tab or the drop down, and click draw to see the magic! :)")
infoText.insert(END, initial_selectedInfo)

mainloop()
