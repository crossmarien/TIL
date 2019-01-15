import turtle 
import turtle as t

class MagicBrush:
    turtle.color('black')
    def draw_square(self):
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)

    def draw_triangle(self):
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    
    def draw_star(self):
        for i in range (5):
            turtle.forward(300)
            turtle.right(144)

    def go(self):
        turtle.forward(200)

    def turn(self):
        turtle.right(90)

m1=MagicBrush()  
m2=MagicBrush()
m3=MagicBrush()
# brad = turtle.Turtle()
# brad.shape('turtle')
# brad.forward(200)
# brad.speed(0.5)
# brad.right(90)
# brad.forward(200)
# m1.draw_star()

while True:
    t.bgcolor('white')
    t.color=('green')
    t.speed=(10)
    t.circle(80)
    t.left(360/30)






# while n < 12:
#     turtle.forward(100)
#     turtle.right(30)
#     n+=1


# n=0
# while n < 12:
#     turtle.forward(200)
#     turtle.right(160)
#     n+=1
# turtle.mainloop()