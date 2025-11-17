import turtle

TEXTFILE = 'line-data.txt'

print('Turtle Draw Starting...')
screen =turtle.Screen()
screen.setup(450,450)
screen.title("Turtle Draw")

turtleDraw = turtle.Turtle()
turtleDraw.speed(0)
turtleDraw.penup()

filename = input ("Enter the name of the input file:")

try:
    lineDataTextfile = open(filename, "r")
except FileNotFoundError:
    print("Error: File not found.")
    quit()

print ("")
lineDataTextfile = open(TEXTFILENAME, "r")
line = lineDataTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if len(parts) == 3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.pencolor(color)
        turtleDraw.penup()
        turtleDraw.goto(x, y)
        turtleDraw.pendown()

    if len(parts) == 1:
        turtleDraw.penup()

    line = lineDataTextfile.readline()

turtle.done()
turtleDraw.txtfile.close()
print("\nEnd")      
