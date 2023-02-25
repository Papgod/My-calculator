import tkinter as tk
import os
from tkinter import ttk

'''选择类型，触发事件内容为后面单位为对应的单位'''
def choose_unit(envet):
    choose = box1.get()
    list=[]
    print(choose)
    if choose == '体积':
        list = ['立方厘米','立方米']
    elif choose == '长度':
        list = ['厘米', '分米', '米', '千米', '毫米']
    elif choose == '面积':
        list = ['平方厘米','平方米', '公顷']
    box2['value'] = list
    box3['value'] = list

'''选择单位后的触发事件，计算的结果出现在如下情况：选择了正确的单位，或者输入数字后回车'''
def convert(envet):
    global data
    global data_out
    unit_class = box1.get()
    if unit_class == '体积':
        data_out.set(convert_V(data, box2.get(),box3.get()))
    elif unit_class =='长度':
        data_out.set(convert_L(data, box2.get(), box3.get()))
    elif unit_class =='面积':
        data_out.set(convert_S(data, box2.get(), box3.get()))
    label4.update()

'''体积单位换算'''
def convert_V(n,unit1,unit2):
    c = [1, 0.000001]
    l = ['立方厘米', '立方米']
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num=int(n.get())
        result = num/c[unit1_index]*c[unit2_index]
    return result
'''面积单位换算'''
def convert_S(n,unit1,unit2):
    c = [10000, 1, 0.0001]
    l = ['平方厘米', '平方米','公顷']
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num = int(n.get())
        result = num / c[unit1_index] * c[unit2_index]
    return result
'''长度单位换算'''
def convert_L(n,unit1,unit2):
    c = [1000, 100, 10, 1, 0.001]
    l = ['毫米','厘米', '分米', '米', '千米' ]
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num = int(n.get())
        result = num / c[unit1_index] * c[unit2_index]
    return result


root = tk.Tk()
root.title("单位换算")
root.geometry('250x400')
'''页面布局'''
label1 = tk.Label(root, text='选择要转换的单位类型',)
label1.grid(row=0,column=0, sticky='nw')

box1 = ttk.Combobox(root)
box1['value'] = ('体积', '长度', '面积')
box1.current(0)
box1.bind("<<ComboboxSelected>>", choose_unit)
box1.grid(row=1,column=0, sticky='nw',ipadx=35)

label2 = tk.Label(root, text='输入',justify='left')
label2.grid(row=2,column=0, sticky='nw')

data = tk.StringVar()
entry1 = tk.Entry(root, textvariable=data)
entry1.insert(6,'输入值（清除‘输入值’后再输入,按下ESC键返回计算器）')
entry1.bind('<Return>',convert)
entry1.grid(row=3,column=0, sticky='nw',ipadx=35)

box2 = ttk.Combobox(root)
box2.bind("<<ComboboxSelected>>", convert)
box2.grid(row=4,column=0, sticky='nw',ipadx=35)

label3 = tk.Label(root, text='等于')
label3.grid(row=5,column=0, sticky='nw')

data_out = tk.StringVar()
data_out.set('0')
label4 = tk.Label(root,textvariable=data_out)
label4.grid(row=6,column=0, sticky='nw')

box3 = ttk.Combobox(root)
box3.bind("<<ComboboxSelected>>", convert)
box3.grid(row=7,column=0, sticky='nw', ipadx=35)
def retru(Evevt):
    root.destroy()
    os.system('python 计算器.py')
   
root.bind("<Escape>",retru)
root.mainloop()
