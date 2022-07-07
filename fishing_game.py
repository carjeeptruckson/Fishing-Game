import random as rd
from tkinter import W
import turtle as t

print('-------------------------------------------------------------------------')
print('Created with Python turtle graphics')
print('                                 __________')
print('Created by CarJeepTruckson   ___|___|______|___')
print('                               O           O   ')
print('Made in 2022')
print('-------------------------------------------------------------------------')


random_num = 2

t.bgcolor('blue')
caterpillar = t.Turtle()
caterpillar.shape('circle')
caterpillar.color('brown')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()


leaf = t.Turtle()
leaf_shape = ((0, 0), (1, 2), (18, 25), (20, 20), \
              (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('orange')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

tres = t.Turtle()
tres.shape('square')
tres.color('sienna3')
tres.shapesize(1, 2, 1)
tres.penup()
tres.hideturtle()
tres.speed(0)

wall = t.Turtle()
wall.shape('circle')
wall.color('gray')
wall.penup()
wall.speed(0)
wall.setx(rd.randint(-300,300))
wall.sety(rd.randint(-300,300))

wall1 = t.Turtle()
wall1.shape('circle')
wall1.color('gray')
wall1.penup()
wall1.speed(0)
wall1.setx(rd.randint(-300,300))
wall1.sety(rd.randint(-300,300))

wall2 = t.Turtle()
wall2.shape('circle')
wall2.color('gray')
wall2.penup()
wall2.speed(0)
wall2.setx(rd.randint(-300,300))
wall2.sety(rd.randint(-300,300))

wall3 = t.Turtle()
wall3.shape('circle')
wall3.color('gray')
wall3.penup()
wall3.speed(0)
wall3.setx(rd.randint(-300,300))
wall3.sety(rd.randint(-300,300))

wall4 = t.Turtle()
wall4.shape('circle')
wall4.color('gray')
wall4.penup()
wall4.speed(0)
wall4.setx(rd.randint(-300,300))
wall4.sety(rd.randint(-300,300))

wall5 = t.Turtle()
wall5.shape('circle')
wall5.color('gray')
wall5.penup()
wall5.speed(0)
wall5.setx(rd.randint(-300,300))
wall5.sety(rd.randint(-300,300))

wall6 = t.Turtle()
wall6.shape('circle')
wall6.color('gray')
wall6.penup()
wall6.speed(0)
wall6.setx(rd.randint(-300,300))
wall6.sety(rd.randint(-300,300))

wall7 = t.Turtle()
wall7.shape('circle')
wall7.color('gray')
wall7.penup()
wall7.speed(0)
wall7.setx(rd.randint(-300,300))
wall7.sety(rd.randint(-300,300))

wall8 = t.Turtle()
wall8.shape('circle')
wall8.color('gray')
wall8.penup()
wall8.speed(0)
wall8.setx(rd.randint(-300,300))
wall8.sety(rd.randint(-300,300))

wall9 = t.Turtle()
wall9.shape('circle')
wall9.color('gray')
wall9.penup()
wall9.speed(0)
wall9.setx(rd.randint(-300,300))
wall9.sety(rd.randint(-300,300))

wall10 = t.Turtle()
wall10.shape('circle')
wall10.color('gray')
wall10.penup()
wall10.speed(0)
wall10.setx(rd.randint(-300,300))
wall10.sety(rd.randint(-300,300))

wall11 = t.Turtle()
wall11.shape('circle')
wall11.color('gray')
wall11.penup()
wall11.speed(0)
wall11.setx(rd.randint(-300,300))
wall11.sety(rd.randint(-300,300))

wall12 = t.Turtle()
wall12.shape('circle')
wall12.color('gray')
wall12.penup()
wall12.speed(0)
wall12.setx(rd.randint(-300,300))
wall12.sety(rd.randint(-300,300))

wall13 = t.Turtle()
wall13.shape('circle')
wall13.color('gray')
wall13.penup()
wall13.speed(0)
wall13.setx(rd.randint(-300,300))
wall13.sety(rd.randint(-300,300))

inclose_turtle= t.Turtle()
inclose_turtle.hideturtle()
inclose_turtle.speed(10)
inclose_turtle.color('red')
inclose_turtle.penup()
inclose_turtle.setx(400)
inclose_turtle.sety(-400)
inclose_turtle.pendown()
inclose_turtle.sety(400)
inclose_turtle.setx(-400)
inclose_turtle.sety(-400)
inclose_turtle.setx(400)
inclose_turtle.penup()
inclose_turtle.hideturtle()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Welcome to the fishing game. ', align='center',\
                 font=('Arial', 16, 'bold'))
text_turtle.sety(-20)
text_turtle.write('Avoid boulders and catch fish to earn points. ', align='center',\
                 font=('Arial', 16, 'bold'))
text_turtle.sety(-40)
text_turtle.write('You can also pick up treasure chests, but beware they are somtimes DANGEROUS!', align='center',\
                 font=('Arial', 15, 'bold'))
text_turtle.sety(-60)
text_turtle.write('Stay inside the inclosed area. ', align='center',\
                 font=('Arial', 16, 'bold'))
text_turtle.sety(-80)
text_turtle.write('Press SPACE to start', align='center',\
                 font=('Arial', 16, 'bold'))
text_turtle.penup()
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    (x,y) = caterpillar.pos()
    outside = \
            x< -400 or \
            x> 400 or \
            y< -400 or \
            y> 400
    return outside

def game_over(): 
    caterpillar.hideturtle()
    leaf.hideturtle()
    tres.hideturtle()
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = 425
    y = 425
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))



def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-300,300))
    leaf.sety(rd.randint(-300,300))
    leaf.showturtle()


def place_tres():
    tres.setx(rd.randint(-300,300))
    tres.sety(rd.randint(-300,300))
    tres.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()


    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar.sety(350)
    display_score(score)
    place_leaf()
    place_tres()



    while True:
        tres.pencolor('sienna3')
        caterpillar.speed(7)

        caterpillar.forward(7)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar.shapesize(1, caterpillar_length, 1)
            score = score + 10
            display_score(score)
            
        if tres.distance(caterpillar)<20:
            place_tres()
            random_num = rd.randint(1, 6)
            if random_num == 1:
                score = score + 30
                display_score(score)
            if random_num == 2:
                score = score + 50
                display_score(score)
            if random_num == 3:
                score = score + 30
                display_score(score)
            if random_num == 4:
                score = score + 50
                display_score(score)
            if random_num == 5:
                game_over()
            if random_num == 6:
                score = score -50
                display_score(score)
            


        if wall.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall1.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall2.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall3.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall4.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall5.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall6.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall7.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall8.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall9.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall10.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall11.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall12.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if wall13.distance(caterpillar) < 20:
            score = score-3
            display_score(score)

        if outside_window():
            game_over()
            break

        if score<0:
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
