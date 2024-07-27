from turtle import  *
title('Jai Shri Ram')
pensize(5)
pencolor("white")
bgcolor("black")
untoldcoding = ["Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram","Jai Shree Ram","Jai Shree Ram",
                "Jai Shree Ram","Jai Shree Ram"]

angle = 360/49
penup()
sety(-1)
for i in range(50):
    left(angle)
    forward(260)
    write(untoldcoding[i], align="right", 
    font=('Arial', 12, "bold"))
    backward(260)

penup()
goto(-40,-20)
pendown()
write("|| Ram ||", font=("Arial", 60, "normal"),
    align="center")

hideturtle()
done()