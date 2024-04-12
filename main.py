import turtle
#called Turtle library
drawing_board=turtle.Screen()
#Turtle's Screen name ==drawing_board
drawing_board.bgcolor("light blue")
#drawing_board's background color is light blue
drawing_board.title("Python Turtle")
#drawing_board's title is "Python Turtle"
turtle_instance=turtle.Turtle()
#Turtle's mouse ==turtle_instance
mylist = ["blue", "red", "green", "white","yellow","black","pink"]
#creat a list which you want your project's colours

def eight_pointed_star():
    for i in range(8):
        turtle_instance.forward(10)
        turtle_instance.left(225)
#creat a function for eight pointed star ,Note:eight pointed star angle is 112.5
def turtle_forward():
    turtle_instance.forward(100)
#creat a function for Turtle'mouse go forward 100 picsel
def turtle_forward2():
    turtle_instance.forward(10)
#creat a function for Turtle'mouse go forward 10 picsel
def turtle_forward3():
    b=mylist[0]
    turtle_instance.color(b)
#change your turtle's mouse's colour is blue
def turtle_forward4():
    b = mylist[1]
    turtle_instance.color(b)
#change your turtle's mouse's colour is red

def turlte_undo():
    turtle_instance.undo()
#if you turtle'mouse went wrong and you want go back this function help you
def turtle_forward5():
    b = mylist[2]
    turtle_instance.color(b)
#change your turtle's mouse's colour is green

def turtle_forward6():
    b=mylist[3]
    turtle_instance.color(b)
#change your turtle's mouse's colour is white

def turtle_forward7():
    b = mylist[4]
    turtle_instance.color(b)
#change your turtle's mouse's colour is yellow

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
#turtle's mouse changed toward right 10 picsel
    #turtle_instance.right(10)
def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
#turtle's mouse changed toward left 10 picsel
 #turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()
#if you want delete your project this code help you
def turtlereturnhome():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
#tis code turtle'mouse pen up and go (0,0) coordinant and again pen down
def turtle_forward8():
    b = mylist[5]
    turtle_instance.color(b)
#change your turtle's mouse's colour is black

def turtle_forward9():
    b = mylist[6]
    turtle_instance.color(b)
#change your turtle's mouse's colour is pink

def turtle_size():
    turtle_instance.pensize(10)
#if you changed pen size  middle thick you used this function
def turtle_size2():
    turtle_instance.pensize(2)
#if you  changed pen size litle thick you used this function
def Star_for():
    for i in range(5):
        turtle_instance.forward(10)
        turtle_instance.left(144)
##creat a function for   star ,Note: star angle is 72



def turtlepenup():
        turtle_instance.penup()
#if you want pen up example you don't want pendown contiune you used penup func

def turtlepenDOWN():
    turtle_instance.pendown()
# if you want pen down example you don't want penup contiune  you used pendown func

drawing_board.listen()
#if you want  sets focus on the turtle screen to capture events you used listen method
drawing_board.onkey(fun=clear_screen,key="c")
#if you click c on keyboard clear_screen func started
drawing_board.onkey(fun=rotate_angle_right,key="Down")
#if you click Down on keyboard  rotate_angle_right func started

drawing_board.onkey(fun=rotate_angle_left,key="Up")
#if you click Up on keyboard  rotate_angle_left func started

drawing_board.onkey(fun=turtle_forward,key="space")
#if you click space on keyboard  turtle_forward func started

drawing_board.onkey(fun=turtlereturnhome,key="h")
#if you click h on keyboard  turtlereturnhome func started

drawing_board.onkey(fun=turtlepenup,key="p")
#if you click p on keyboard  turtlepenup func started

drawing_board.onkey(fun=turtlepenDOWN,key="d")
#if you click d on keyboard turtlepenDOWN  func started

drawing_board.onkey(fun=turtle_forward2,key="Tab")
#if you click Tab on keyboard turtle_forward2  func started

drawing_board.onkey(fun=turtle_forward3,key="b")
#if you click b on keyboard turtle_forward3  func started

drawing_board.onkey(fun=turtle_forward4,key="r")
#if you click r on keyboard turtle_forward4  func started

drawing_board.onkey(fun=turtle_forward5,key="g")
#if you click g on keyboard turtle_forward5  func started

drawing_board.onkey(fun=turtle_forward6,key="w")
#if you click w on keyboard turtle_forward6  func started

drawing_board.onkey(fun=turlte_undo,key="u")
#if you click u on keyboard turlte_undo  func started

drawing_board.onkey(fun=turtle_forward7,key="y")
#if you click y on keyboard turtle_forward7  func started

drawing_board.onkey(fun=turtle_forward8,key="B")
#if you click B on keyboard turtle_forward8  func started

drawing_board.onkey(fun=turtle_forward9,key="P")
#if you click P on keyboard turtle_forward9  func started

drawing_board.onkey(fun=turtle_size,key="e")
#if you click e on keyboard turtle_size  func started

drawing_board.onkey(fun=turtle_size2,key="E")
#if you click E on keyboard turtle_size2  func started

drawing_board.onkey(fun=Star_for,key="*")
#if you click * on keyboard Star_for  func started

drawing_board.onkey(fun=eight_pointed_star,key="8")
#if you click 8 on keyboard eight_pointed_star  func started

"""def hilal():
    turtle_instance.color("white")
    turtle_instance.up()
    turtle_instance.goto(0,-20)
    turtle_instance.begin_fill()
    turtle_instance.circle(20)
    turtle_instance.end_fill()
    turtle_instance.up()
    turtle_instance.color("red")
    turtle_instance.goto(5,-20)
    turtle_instance.begin_fill()
    turtle_instance.circle(20)
    turtle_instance.end_fill()"""
#if you want write crescent moon you active this code
#drawing_board.onkey(fun=hilal,key="C")
def pensizeu():
    turtle_instance.pensize(30)
#if you  changed pen size litle thick you used this function
drawing_board.onkey(fun=pensizeu,key="3")
#if you click 3 on keyboard pensizeu  func started

def circle():
    turtle_instance.circle(10)
#this func-code creat circle
drawing_board.onkey(fun=circle,key="o")
#if you click o on keyboard circle  func started

def dort():
    for i in range(4):
        turtle_instance.forward(100)
        turtle_instance.left(90)
#this code creat kv becouse kv's angle is 90
drawing_board.onkey(fun=dort,key="4")
#if you click 4 on keyboard dort  func started







turtle.mainloop()
#this code keep screen