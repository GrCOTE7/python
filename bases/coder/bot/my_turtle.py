import turtle

def draw_isosceles_triangle(length):
    t = turtle.Turtle()
    turtle.Screen().bgcolor("white")
    t.speed(1)
    t.color("blue")

    for _ in range(3):
        t.forward(length)
        t.right(120)

    turtle.done()


# Appeler la fonction avec la longueur souhaitée
draw_isosceles_triangle(100)
 