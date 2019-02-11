
#coding:utf-8

from tkinter import *

import random

import time

 

 

class Ball:

    #创建一个球类

    def __init__(self, canvas, color):

        self.canvas = canvas

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        #返回刚好划小球的id，create_oval创建一个椭圆

        self.canvas.move(self.id, 245, 100)

        #把椭圆移动到画布

        starts = [-3, -2, -1, 1, 2, 3]

        random.shuffle(starts)

        #随机排列

        self.x = starts[0]

        self.y = -3

        self.canvas_height = self.canvas.winfo_height()

        #获取画布当前高度

        self.canvas_width = self.canvas.winfo_width()

        #获取画布当前宽度

    def draw(self):

        self.canvas.move(self.id, self.x, self.y)

        #让小球水平和垂直移动

        pos = self.canvas.coords(self.id)

        #coords返回画布上画好的x和y坐标

 

        #判断小球是否撞到画布顶部或者底部，保证小球反弹回去，不消失

        if pos[1] <= 0:

            self.y = 3

        if pos[3] >= self.canvas_height:

            self.y = -3

        if pos[0] <= 0:

            self.x = 3

        if pos[2] >= self.canvas_width:

            self.x = -3

 

tk = Tk()

tk.title("Game")

 

tk.resizable(0, 0)

#窗口大小不可调整

tk.wm_attributes("-topmost", 1)

#使画布窗口置于所有窗口之前

canvas = Canvas(tk,width=500, height=400, bd=0, highlightthickness=0)

#bd和highlighttthickness是为了保证画布没有边框

canvas.pack()

tk.update()

#动画初始化

 

ball = Ball(canvas, 'red')

 

while 1:

    #画布一出现会马上消失，为了防止画布消失，用tkinter一直重画

    ball.draw()

    tk.update_idletasks()

    tk.update()

    time.sleep(0.01)
