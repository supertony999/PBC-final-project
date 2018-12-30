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
		
#class寫法half完成
'''
class Page3(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
		# self.scrollbar()
	def createWidgets(self):
		f1 = tkFont.Font(size = 15, family = "微軟正黑體") #字體
		f2 = tkFont.Font(size = 15, family = "微軟正黑體")
		f3 = tkFont.Font(size = 15, family = "微軟正黑體")

		#放圖片
			# 一芳水果茶
		if brandchoose == "一芳水果茶":
			# 頂層品牌logo
			self.imageYifun = tk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶.png")
			self.Label_logo = tk.Label(self, image = self.imageYifun, font = f1, height=400, width=600,)
			self.Label_logo.grid(row = 0, column = 0, columnspan = 6,rowspan = 1, sticky = tk.NE + tk.SW)

			# 推薦飲料
			# Top1
			self.imageYifunTop1 = ImageTk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶Top1.png")
			self.Top1 = tk.Label(self, text = Top_list[0],font = f1,bg="burlywood").grid(row = 1, column = 1, columnspan = 1, sticky = tk.W)
			# Top2
			self.imageYifunTop2 = ImageTk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶Top2.png")
			self.Top2 = tk.Label(self, text = Top_list[1],font = f1,bg="burlywood").grid(row = 1, column = 3, columnspan = 1, sticky = tk.W)
			# Top3
			self.imageYifunTop3 = ImageTk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶Top3.png")
			self.Top3 = tk.Label(self, text = Top_list[2],font = f1,bg="burlywood").grid(row = 1, column = 5, columnspan = 1, sticky = tk.W)
			#distance
			self.distance = tk.Label(self, text = distance,font = f1)
			self.distance.grid(row = 2, column = 1, columnspan = 5, sticky = tk.W)
			#storename
			self.storename = tk.Label(self, text = storename,font = f1)
			self.storename.grid(row = 3, column = 1, columnspan = 5, sticky = tk.W)
			#address
			self.address = tk.Label(self, text = address,font = f1)
			self.address.grid(row = 4, column = 1, columnspan = 5, sticky = tk.W)

			#我要訂購按鈕
			self.btnOrder = tk.Button(self, text = "我要訂購", command = self.clickBtnNums, height = 1, width = 1,font = f2)
			self.btnOrder.grid(row = 5, column = 0, columnspan = 2, sticky = tk.NE + tk.SW)
			
			#Label訂購電話
			global var
			var = StringVar()
			self.telephone = tk.Label(self, textvariable = var, font = f1)
			self.telephone.grid(row = 5, column = 2, columnspan = 3, sticky = tk.NE + tk.SW)
			
			#Menu圖片
			self.imageMenu = ImageTk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\十杯Menu.png")
			self.Label_logo = tk.Label(self,image = self.imageMenu, font = f1)
			self.Label_logo.grid(row = 6, column = 0, columnspan = 6, sticky = tk.NE + tk.SW)
			
			self.Top1_module = tk.Label(self, text = "Top1",font = f1)
			self.Top1_module.grid(row = 1, column = 0, columnspan = 1, sticky = tk.NE + tk.SW)
			self.Top2_module = tk.Label(self, text = "Top2",font = f1)
			self.Top2_module.grid(row = 1, column = 2, columnspan = 1, sticky = tk.NE + tk.SW)
			self.Top3_module = tk.Label(self, text = "Top3",font = f1)
			self.Top3_module.grid(row = 1, column = 4, columnspan = 1, sticky = tk.NE + tk.SW)
			self.distance_module = tk.Label(self, text = "距離：",font = f1)
			self.distance_module.grid(row = 2, column = 0, columnspan = 1, sticky = tk.NE + tk.SW)
			self.storename_module = tk.Label(self, text = "店名：",font = f1)
			self.storename_module.grid(row = 3, column = 0, columnspan = 1, sticky = tk.NE + tk.SW)
			self.address_module = tk.Label(self, text = "地址：",font = f1)
			self.address_module.grid(row = 4, column = 0, columnspan = 1, sticky = tk.NE + tk.SW)

	def clickBtnNums(self): #依照method的選擇，決定要平方或立方，取代原先文字方塊的文字，顯示結果
		var.set(telephone)
cal = Page3()
cal.master.title("Page3")
cal.mainloop()
'''
#網路滾軸示範
'''
canvas=Canvas(width=200,height=180,scrollregion=(0,500,1000,1000)) #创建canvas(left, top, right, bottom)
canvas.place(x = 0, y = 0) #放置canvas的位置
frame=Frame(canvas) #把frame放在canvas里
frame.place(width=180, height=180) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = 180,width=20,height=180)
vbar.configure(command=canvas.yview)

canvas.config(yscrollcommand=vbar.set) #设置  
canvas.create_window((90,240), window=frame)  #create_window
mainloop()
'''

#已完成的陽春版簡易滾軸
'''
#bg顏色參考 https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm 
#預計的input() → 變數 : brandchoose
brandchoose = "一芳水果茶"
distance = "50公尺(步行1分鐘)"
storename = "台大公館店"
address = "台北市大安區羅斯福路三段345號"
telephone = " 02 2368 2266"
Top_list = ["主恩牧奶茶","初鹿牧奶茶","柳營牧奶茶"]

import tkinter as tk # or import tkinter →後續都用tkinter
from tkinter import ttk,Canvas
import tkinter.font as tkFont
import math
from PIL import ImageTk
import os
from tkinter import *

canvas=Canvas(width=200,height=180,scrollregion=(0,0,1000,1000)) #创建canvas(left, top, right, bottom)
canvas.place(x = 0, y = 0) #放置canvas的位置
frame=Frame(canvas) #把frame放在canvas里
frame.place(width=180, height=180) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = 180,width=20,height=180)
vbar.configure(command=canvas.yview)

f2 = tkFont.Font(size = 15, family = "微軟正黑體") #字體
imageYifunTop1 = ImageTk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶Top1.png")
frame.Top1 = tk.Label(frame, text = Top_list[0],font = f2,bg="burlywood").grid(row = 1, column = 1, columnspan = 1, sticky = tk.W)
# 頂層品牌logo
imageYifun = tk.PhotoImage(file="C:\\Users\\User\\Desktop\\Python\\final project\\一芳水果茶.png")
frame.Label_logo = tk.Label(frame, image = imageYifun, font = f2, height=400, width=600,).grid(row = 0, column = 0, columnspan = 6,rowspan = 1, sticky = tk.NE + tk.SW)

canvas.config(yscrollcommand=vbar.set) #设置  
canvas.create_window((90,240), window=frame)  #create_window9
mainloop()
'''