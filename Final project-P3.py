#bg顏色參考 https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm 
import math
import tkinter as tk
from tkinter import ttk,Canvas
import tkinter.font as tkFont

from PIL import Image, ImageTk, ImageEnhance
from tkinter import *

#建立canvas視窗
canvas = Canvas(width=900, height=2000, bg='white',scrollregion=(0,0,1000,2000))
canvas.place(x = 0, y = 0) #放置canvas的位置
canvas.pack(expand=YES, fill=BOTH)

########## Page2結果 #########################
brandchoose = "甘蔗媽媽"
distance = "50公尺(步行1分鐘)"
##############################################

########## 不同品牌########## 品牌logo import(height=320)########## 品牌menu(Width=800) import
#波囍 墾丁蛋蛋ㄉㄨㄞ奶 Comebuy Comebuy公館店 康青龍 迷客夏 日日裝茶 陳三鼎 Coco 甘蔗媽媽 北門口綠豆沙牛奶 春陽茶室 幸福堂 十杯
if brandchoose == "波囍":
	storename = "台大公館店"
	address = "100台北市中正區羅斯福路三段316巷2號"
	telephone = "02 2364 1599"
	time="11:00-23:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\波囍.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\波囍menu.jpg')
if brandchoose == "墾丁蛋蛋ㄉㄨㄞ奶": 
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段165號"
	telephone = " 02 2368 5550"
	time="11:30-23:30"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\墾丁蛋蛋ㄉㄨㄞ奶.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\墾丁蛋蛋ㄉㄨㄞ奶menu.jpg')
if brandchoose == "Comebuy": 
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段195號"
	telephone = "02 2362 1969"
	time="10:00-23:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Comebuy.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Comebuymenu.jpg')
if brandchoose == "Comebuy公館店":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段195號"
	telephone = "02 2362 1969"
	time="10:00-23:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Comebuy.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Comebuymenu.jpg')
if brandchoose == "康青龍":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段160巷4之1號"
	telephone = "02 2368 8608"
	time="11:00-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\康青龍.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\康青龍Menu.jpg')
if brandchoose == "迷客夏":
	storename = "台大公館店"
	address = "100台北市羅斯福路四段132號"
	telephone = "02 2368 1890"
	time="10:30-22:30"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\迷客夏.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\迷客夏menu.jpg')
if brandchoose == "日日裝茶":
	storename = "台大公館店"
	address = "106台北市大安區新生南路三段96-4號"
	telephone = "02 2368 8200"
	time="10:00-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\日日裝茶.JPG')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\日日裝茶menu.jpg')
if brandchoose == "陳三鼎":
	storename = "台大公館店"
	address = "100台北市中正區羅斯福路三段316巷8弄2號"
	telephone = "02 2367 7781"
	time="11:00-21:30"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\陳三鼎.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\陳三鼎menu.jpg')
if brandchoose == "Coco":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段179號"
	telephone = "02 2368 1311"
	time="11:00-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Coco.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\Cocomenu.jpg')
if brandchoose == "甘蔗媽媽":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段130號"
	telephone = "02 2365 5075"
	time="11:00-22:30"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\甘蔗媽媽.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\甘蔗媽媽menu.jpg')
if brandchoose == "北門口綠豆沙牛奶":
	storename = "台大公館店"
	address = "100台北市中正區羅斯福路三段316巷4號"
	telephone = "02 2368 1999"
	time="10:30-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\北門口綠豆沙牛奶.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\北門口綠豆沙牛奶menu.jpg')
if brandchoose == "春陽茶室":
	storename = "台大公館店"
	address = "100台北市中正區羅斯福路三段316巷10-2號"
	telephone = "02 2368 9923"
	time="11:00-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\春陽茶室.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\春陽茶室menu.jpg')
if brandchoose == "幸福堂":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段185號"
	telephone = "02 2367 9097"
	time="11:00-22:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\幸福堂.png')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\幸福堂menu.jpg')
if brandchoose == "十杯":
	storename = "台大公館店"
	address = "100台北市中正區汀州路三段277號"
	telephone = "02 2369 0900"
	time="11:00-23:00"
	Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]
	logopic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\十杯.jpg')
	menupic = ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\十杯menu.png')
# 品牌Logo顯示
canvas.create_image(450, 0, image=logopic, anchor=N)

#字體
f1 = tkFont.Font(size = 15, family = "微軟正黑體") 
a=120 #讓所有Window下移的距離
b=110  #讓所有Window左移的距離
#TOP系列
widget = Label(canvas, text='Top1', fg='black', bg='white',font=f1)
canvas.create_window(50+a, 240+b, window=widget)

widget = Label(canvas, text='Top2', fg='black', bg='white',font=f1)
canvas.create_window(270+a, 240+b, window=widget)

widget = Label(canvas, text='Top3', fg='black', bg='white',font=f1)
canvas.create_window(490+a, 240+b, window=widget)

#飲料系列
widget = Label(canvas, text=Top_list[0], fg='black', bg='burlywood',font=f1)
canvas.create_window(130+a, 240+b, window=widget)

widget = Label(canvas, text=Top_list[1], fg='black', bg='burlywood',font=f1)
canvas.create_window(350+a, 240+b, window=widget)

widget = Label(canvas, text=Top_list[2], fg='black', bg='burlywood',font=f1)
canvas.create_window(570+a, 240+b, window=widget)

#店家資訊框架
widget = Label(canvas, text="距離：", fg='black',font=f1,anchor=W)
canvas.create_window(80+a, 300+b, window=widget)

widget = Label(canvas, text="店名：", fg='black',font=f1)
canvas.create_window(80+a, 330+b, window=widget)

widget = Label(canvas, text="營業時間：", fg='black',font=f1)
canvas.create_window(80+a, 360+b, window=widget)

widget = Label(canvas, text="地址：", fg='black',font=f1)
canvas.create_window(80+a, 390+b, window=widget)

#店家資訊
	#距離
widget = Label(canvas, text=distance, fg='black',font=f1,anchor=W)
canvas.create_window(350+a, 300+b, window=widget)
	#營業時間
widget = Label(canvas, text=time, fg='black',font=f1,anchor=W)
canvas.create_window(350+a, 330+b, window=widget)
	#店名
widget = Label(canvas, text=storename, fg='black',font=f1,anchor=W)
canvas.create_window(350+a, 360+b, window=widget)
	#地址
widget = Label(canvas, text=address, fg='black',font=f1,anchor=W)
canvas.create_window(350+a, 390+b, window=widget)

#Label電話顯示
var = StringVar()
def clickBtnNums():
	var.set(telephone)
showtelephone = tk.Label(canvas, textvariable = var, font = f1)
canvas.create_window(340+a, 440+b, window=showtelephone)

# 我要訂購button
orderimage = PhotoImage(file='C:\\Users\\User\\Desktop\\Python\\final project\\order.png')
orderimagelb = Button(canvas, width=120, height=34,image=orderimage,command = clickBtnNums)
canvas.create_window(150+a, 440+b, window=orderimagelb)

# 品牌menu顯示
canvas.create_image(350+a, 480+b, image=menupic, anchor=N)

#Scrollbar
vbar=Scrollbar(canvas,orient=VERTICAL) #垂直滾軸
vbar.place(x = 880,width=20,height=800)
vbar.configure(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set) #设置  

mainloop()
