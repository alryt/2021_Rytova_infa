from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
score = 0
a = -3
number_of_targets = int(input("Количество целей = "))

gun = 0


class Ball:
    def __init__(self, x=50, y=500):
        """ Конструктор класса Ball
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """

        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'orange', 'yellow', 'black'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self, event=0):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        """

        Y = 600
        X = 800
        if ((abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) < Y / 2 - self.r)):
            self.x += self.vx
            self.y += self.vy
        elif (abs(self.x + self.vx - X / 2) > X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.vx = -self.vx
        elif (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) > Y / 2 - self.r):
            self.vy = -self.vy
            self.x += self.vx
        else:
            self.vy = -self.vy
            self.vx = -self.vx
        self.vy -= a

        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью
        obj: Обьект, с которым проверяется столкновение.
        """

        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (
                obj.r + self.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420,
                                   width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Происходит выстрел
        """

        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание пушкой"""

        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='red')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='red')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.vx = rnd(0, 5)
        self.vy = rnd(0, 5)
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """ 'не знаю, как исправить эти ошибки'
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = choice(['blue', 'green', 'red', 'brown', 'orange', 'yellow'])
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.vx = 0
        self.vy = 0
        self.x = -100
        self.y = -100
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )
        self.points += points

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        """

        Y = 600
        X = 800
        if ((abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) < Y / 2 - self.r)):
            self.x += self.vx
            self.y += self.vy
        elif (abs(self.x + self.vx - X / 2) > X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.vx = -self.vx
        elif (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (
                abs(self.y + self.vy - Y / 2) > Y / 2 - self.r):
            self.vy = -self.vy
            self.x += self.vx
        else:
            self.vy = -self.vy
            self.vx = -self.vx

        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )


canv.create_rectangle(10, 10, 50, 50, fill="white")
screen1 = canv.create_text(400, 300, text='', font='28')
id_points = canv.create_text(30, 30, text=score, font='28')
g1 = Gun()
bullet = 0
balls = []
targets = []
for i in range(number_of_targets):
    targets.append(Target())


def new_game():
    global gun, screen1, balls, bullet, targets, score
    for i in targets:
        i.new_target()
        i.live = 1
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    f = False
    for i in targets:
        if i.live == 1:
            f = True
    while f or balls:
        for b in balls:
            b.move()
            for i in range(len(targets)):
                if b.hittest(targets[i]) and targets[i].live:
                    targets[i].live = 0
                    targets[i].hit()
                    score += targets[i].points
                    canv.create_rectangle(10, 10, 50, 50, fill="white")
                    canv.create_text(30, 30, text=score, font='28')
                    canv.itemconfig(screen1, text='Вы уничтожили цель ' + str(
                        i + 1) + ' за ' + str(bullet) + ' выстрелов')
        for t in targets:
            t.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

