import sys
import os
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter
from tkinter import Toplevel

换行符 = '\n'
空 = None
真 = True
假 = False
警告图标 = 48
错误图标 = 16
信息图标 = 64
确定取消钮 = 1


print("\033[93m易语言基础语法python模块已加载完成\n此版本为测试版暂未发行v1.0.0\n公告:仅添加了基础语法\n作者:daijunning,yanmo,f[QQ:2971302216]\033[0m")
print("———————————————————————————————————DeBug输出栏————————————————————————————————————")



def 调试输出(欲输出值_通用数组or非数组):
    print(欲输出值_通用数组or非数组)



def 标准输出(输出方向_整数型,欲输出内容_通用型):
    if 输出方向_整数型 == 空:
        if 欲输出内容_通用型.endswith('\n'):
            print(欲输出内容_通用型)
        else:
            print(欲输出内容_通用型,end="")
    elif 输出方向_整数型 * 0 == 0:
        if 欲输出内容_通用型.endswith('\n'):
            print(欲输出内容_通用型)
        else:
            print(欲输出内容_通用型,end="")
    else:
        print("\033[31m函数调用发生错误: \n     第一个形参(输出方向_整数型)应该输入数值 因为: \n         错误(10044): 不能将“文本型”数据转换到“整数型”数据。\033[0m")
        sys.exit(1)




def 标准输入(是否回显_逻辑型):
    if 是否回显_逻辑型 == True or 是否回显_逻辑型 == None:
        return input()
    elif 是否回显_逻辑型 == False:
        sys.exit(0)
    else:
        print(
            "\033[31m函数调用发生错误: \n     第一个形参(是否回显_逻辑型)应该输入逻辑 因为: \n         错误(10044): 不能将“整数型”数据转换到“逻辑型”数据。\033[0m")
        sys.exit(1)


def 判断(条件_逻辑型):
    if 条件_逻辑型 == 真:
        return 真
    else:
        return 假



def 如果(条件_逻辑型):
    if 条件_逻辑型 == 真:
        return 真
    else:
        return 假



def 返回(返回到调用方的值_通用型):
        return 返回到调用方的值_通用型


def 信息框(提示信息_通用型,图标_整数型,窗口标题_文本型):#https://blog.csdn.net/qq_34745941/article/details/116995050
    if 图标_整数型 == 警告图标:
        result = showwarning(窗口标题_文本型, 提示信息_通用型)
    elif 图标_整数型 == 错误图标:
        result = showerror(窗口标题_文本型, 提示信息_通用型)
    elif 图标_整数型 == 信息图标:
        result = showinfo(窗口标题_文本型, 提示信息_通用型)
    elif 图标_整数型 == 确定取消钮:
        messagebox.showinfo(提示信息_通用型, 窗口标题_文本型)


def 取运行目录():
    return os.getcwd()


def 取用户帐号(拔号网络索引_整数型):
    return os.getenv("USERNAME")


def 到文本(待转述的数据_通用型数组_或者_非数组):
    return str(待转述的数据_通用型数组_或者_非数组)

def 到数值(待转换的文本或数值_通用型):
    return float(待转换的文本或数值_通用型)

def 到整数(待转换的文本或数值_通用型):
    return int(待转换的文本或数值_通用型)

def 到字节集(待转述的数据_通用型数组_或者_非数组):
    return str(待转述的数据_通用型数组_或者_非数组)

def 结束():
    sys.exit(0)

