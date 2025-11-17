import turtle

TEXTFILE = 'line-data.txt'
print('Turtle Draw Lite Starting...')
'''
edTheTurtle = turtle.Turtle ()
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
'''
turtleDraw = turtle.Turtle()
turtleDraw.speed(5)
turtleDraw.penup()
'''
for i in range (40):
    turtleDraw.forward(i * 10)
    turtleDraw.right(144)
'''
print("")
print("Turtle Draw -Part 2")

lineDataTextfile = open(TEXTFILENAME,"r")
line = lineDataTextfile.readline()
   
    while line:
    print(line, end=' ')
    line = lineDataText.file.redline()
    parts = line.split(' ')

    if len(parts) ==3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.pencolor(color)
        turtleDraw.goto(x, y)
        turtleDraw.pendown()

    if len(parts) ==1:
        turtle.Draw.penup()

turtle.done
print("\nEnd")        

