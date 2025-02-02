import turtle

def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.right(90)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.left(45)
    turtle.backward(branch_length)

def main():
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.left(90)  # Початкова позиція черепахи (вверх)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    branch_length = 100
    level = int(input("Введіть рівень рекурсії: "))
    draw_pythagoras_tree(branch_length, level)
    turtle.done()

if __name__ == "__main__":
    main()
