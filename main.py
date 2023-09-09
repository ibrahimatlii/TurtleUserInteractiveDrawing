import turtle

drawing_board=turtle.Screen()

drawing_board.bgcolor("light blue")
drawing_board.title("python turtle")

turtle_instance=turtle.Turtle()

def ileri():
    turtle_instance.forward(100)
def yukari():
    turtle_instance.left(180)
def asagi():

    turtle_instance.right(-180)
def saga():
    #turtle_instance.right(90) bunun yerine aşaığdaki de kullanılabilir
    turtle_instance.setheading(turtle_instance.heading()-90)
def sola():
    #turtle_instance.left(90)
    turtle_instance.setheading(turtle_instance.heading()+90)

def temizle():
    turtle_instance.clear()

def basa_don():
    turtle_instance.home()


def turtle_kaleminucunu_kaldir():
    turtle_instance.penup()

def turtle_kaleminucunu_indir():
    turtle_instance.pendown()




drawing_board.listen()
drawing_board.onkey(yukari,"Up")
drawing_board.onkey(asagi,"Down")
drawing_board.onkey(saga,"Right")
drawing_board.onkey(sola,"Left")
drawing_board.onkey(fun=ileri,key="space")#istersen değişkenleri yaz isterseen yukardaki gibi değer yaz
drawing_board.onkey(temizle,"c")
drawing_board.onkey(basa_don,"g") #burada geri dönmek istediği noktaya gelir ama bir sorunla dönerken de çizer
drawing_board.onkey(turtle_kaleminucunu_indir,"w")
drawing_board.onkey(turtle_kaleminucunu_kaldir,"q")
turtle.done()