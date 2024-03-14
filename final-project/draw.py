from turtle import * 

speed(0)
#This function will draw a gravestone that have a cross and RIP if you lose the game
def lose():
    #draw the gravestone outline
    penup()
    goto(-50,-50)
    pendown()
    forward(150)
    left(90)
    forward(150)
    circle(100,180)
    forward(150)
    left(90)
    forward(100)

    #draw the cross on the gravestone
    penup()
    goto(-30,140)
    pendown()
    forward(60)
    left(90)
    penup()
    goto(0,110)
    pendown()
    forward(60)

    #Write the RIP on the gravestone
    penup()
    goto(-40,20)
    color('red')
    style = ('Courier',50, 'italic')
    write('RIP', font=style)
    penup()
    goto(-80,-20)
    style = ('Courier',40)
    write('you die',font = style)
    hideturtle()

# This function will draw a sword if you win the game
def win():
    #draw the outline of the upper part of the sword
    penup()
    goto(0,-70)
    pendown()
    forward(40)
    left(90)
    forward(200)
    # draw the two slash on the top
    left(30)
    forward(50)
    left(120)
    forward(50)
    left(30)
    #continue for outline
    forward(200)
    left(90)
    forward(30)

    #draw the rectangle under the upper part
    forward(60)
    right(90)
    forward(20)
    right(90)
    forward(130)
    right(90)
    forward(20)
    right(90)
    forward(50)

    #draw the part for hilt
    penup()
    right(90)
    forward(20)
    pendown()
    forward(100)
    circle(15,180)
    forward(100)

    #write the congratulation 
    penup()
    goto(-50,180)
    color('blue')
    style = ('Courier',40)
    write('You win!',font = style)
    hideturtle()

#This function will draw a shield if you not die but not win

def draw_shield():
    #draw the top base line
    penup()
    goto(-150,200)
    pendown()
    forward(230)

    #draw the right shape for the shield
    right(90)
    circle(90,60)
    right(60)
    forward(130)
    right(180)
    circle(200,-80)
    
    #draw the left shape for the shield
    right(20)
    circle(200,-80)
    right(180)
    forward(130)
    right(60)
    circle(90,60)

    #connect to the base line
    right(90)
    forward(30)
    
    #show the ending on the shield
    penup()
    goto(-150,100)
    color('green')
    style = ('Courier',40)
    write('You escape',font = style)
    penup()
    goto(-150,0)
    write("without",font = style)
    goto(-150,-50)
    write("grandma",font = style)
    hideturtle()

