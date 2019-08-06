

from turtle import*


color('red','green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break


while True:
    forward(200)
    left(300)
    if abs(pos()) < 1:
        break



end_fill()
exitonclick()


