import turtle
TEXTFILE = 'line-data.txt'
print('Turtle Draw Starting...')

turtleDraw = turtle.Turtle()
turtleDraw.speed(0)
turtleDraw.penup()

print ()
lineDataTextfile = open(TEXTFILENAME, "r")
line = lineDataTextfile.readline()
while line:
    print(line, end=' ')
    parts = line.split(' ')

    if len(parts) == 3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.pencolor(color)
        turtleDraw.goto(x, y)
        turtleDraw.pendown()

    if len(parts) == 1:
        turtleDraw.penup()

line = lineDataTextfile.readline()

turtle.done()
turtleDraw.txtfile.close()
print("\nEnd")      
