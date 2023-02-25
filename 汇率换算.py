import sys, os
import tkinter
from tkinter import ttk
from subprocess import Popen,PIPE
sys.path.append(os.getcwd())
# 这是新建文件汇率换算.py
import tkinter
from tkinter import ttk
tk=tkinter.Tk()
tk.maxsize(300,430)
tk.minsize(300,430)
tk.title('汇率转换工具')
def goto01py():
    tk.destroy()
    p = Popen('python 计算器.py', shell=False, stdout=PIPE)

retr = tkinter.Button(tk,bg = 'red',text = '返回',command = goto01py).pack()

#hxxknmjskj
tkinter.Label(tk,text='--------------需要转换的币种--------------').place(x=10,y=10)
tkinter.Label(tk,text="请输入金额:").place(x=10,y=40)
tkinter.Label(tk,text='请选择币种:').place(x=10,y=70)
#输入框
entert=tkinter.Entry(tk,width=20,textvariable=tkinter.StringVar())
entert.place(x=100,y=40)
#选择
combo=ttk.Combobox(tk,width=18,textvariable=tkinter.StringVar(),state='readonly')
combo["values"]=('人民币','美元','韩币','日元','欧元','泰铢','英镑','港元','妙金币')
combo.current(0)
combo.place(x=100,y=70)

#文本框
tkinter.Label(tk,text='--------------转换对应的币种--------------').place(x=10,y=100)
a1=tkinter.Label(tk,text="人民币: 0")
a1.place(x=10,y=130)
b2=tkinter.Label(tk,text="美    元: 0")
b2.place(x=10,y=160)
c3=tkinter.Label(tk,text="韩    币: 0")
c3.place(x=10,y=190)
d4=tkinter.Label(tk,text="日    元: 0")
d4.place(x=10,y=220)
e5=tkinter.Label(tk,text="欧    元: 0")
e5.place(x=10,y=250)
f6=tkinter.Label(tk,text="泰    铢: 0")
f6.place(x=10,y=280)
g7=tkinter.Label(tk,text="英    镑: 0")
g7.place(x=10,y=310)
h8=tkinter.Label(tk,text="港    元: 0")
h8.place(x=10,y=340)
i9=tkinter.Label(tk,text="妙金币: 0")
i9.place(x=10,y=370)
tkinter.Label(tk,text="-----备注：2020-10-20 的综合汇率------").place(x=10,y=400)
#1人民币等于N其他货币
CNYtoOther=(1,0.1497,170.5298,15.7972,0.1272,4.6704,0.1156,1.1601,0.15015)
#1其他货币等于N人民币
OthertoCNY=(1,6.6803,0.005864,0.0633,7.8634,0.2141,8.6523,0.862,6.66)
#汇率转换
def ercmoney(*arg):
    money=entert.get()
    isok=True
    for i in money:
        if i<'0' or i>'9':
            isok=False
    if len(money)<1:
        isok=False
    if isok:
        money=float(money)*OthertoCNY[combo.current()]
    else:
        money=0
    a1["text"]='人民币: '+ str(money/OthertoCNY[0]) if combo.current()==0 else '人民币: '+str(round(money*CNYtoOther[0],4))
    b2["text"] = '美    元: ' + str(money/OthertoCNY[1]) if combo.current()==1 else '美    元: '+str(round(money * CNYtoOther[1],4))
    c3["text"] = '韩    币: ' + str(money/OthertoCNY[2]) if combo.current()==2 else '韩    币: '+str(round(money * CNYtoOther[2],4))
    d4["text"] = '日    元: ' + str(money/OthertoCNY[3]) if combo.current()==3 else '日    元: '+str(round(money * CNYtoOther[3],4))
    e5["text"] = '欧    元: ' + str(money/OthertoCNY[4]) if combo.current()==4 else '欧    元: '+str(round(money * CNYtoOther[4],4))
    f6["text"] = '泰    铢: ' + str(money/OthertoCNY[5]) if combo.current()==5 else '泰    铢: '+str(round(money * CNYtoOther[5],4))
    g7["text"] = '英    镑: ' + str(money/OthertoCNY[7]) if combo.current()==6 else '英    镑: '+str(round(money * CNYtoOther[6],4))
    h8["text"] = '港    元: ' + str(money/OthertoCNY[7]) if combo.current()==7 else '港    元: '+str(round(money * CNYtoOther[7],4))
    i9["text"] = '妙金币: ' + str(money/OthertoCNY[8]) if combo.current()==8 else '妙金币: '+str(round(money * CNYtoOther[8],4))

entert.bind("<KeyRelease>",ercmoney)
combo.bind("<<ComboboxSelected>>",ercmoney)
l = tkinter.Label(tk,text = '红色按钮时返回，橙色按钮时单位换算')
tk.mainloop()
