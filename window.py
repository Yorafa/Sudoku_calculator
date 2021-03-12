# @School: University of Toronto
# @Author: Tianle Wang
# @Time: 2021-03-11 2:56 p.m.
# @File: window.py
# @Interpreter: python 3.9.0
# @IDE: PyCharm
from tkinter import *
from tkinter import messagebox
import tkinter.font as tf
from tkinter import filedialog
import sudoku as su


sudoku = su.Sudoku([])  # define
filename = ''


def about_me():
    """A messagebox that tell user what's the software use for"""
    messagebox.showinfo("欢迎使用", "数独Calculator -power by Yorafa\n"
                                "点击打开读取文本\n点击手动输入打开新窗口输入\n"
                                "点击求解获得解")


def open_file():
    """Open the sudoku file that want"""
    global filename, sudoku

    filename = filedialog.askopenfilename()
    if filename != '':
        file_reminder.config(text='您选择的文件是'+filename)
        filename = open(filename)
        sudoku = su.read_data(filename)
        t.delete('1.0', END)
        t.insert(INSERT, str(sudoku))
    else:
        file_reminder.config(text='您没有选择任何文件')


def go_solve():
    """Recall the solve function from the sudoku.py"""
    global sudoku
    t.delete('1.0', END)
    t.insert(INSERT, sudoku.print_result())


def new_window():
    def forward():
        """Forward all the value to calculator"""
        global sudoku
        lst = [[t11.get(), t12.get(), t13.get(), t14.get(), t15.get(),
                t16.get(), t17.get(), t18.get(), t19.get()],
               [t21.get(), t22.get(), t23.get(), t24.get(), t25.get(),
                t26.get(), t27.get(), t28.get(), t29.get()],
               [t31.get(), t32.get(), t33.get(), t34.get(), t35.get(),
                t36.get(), t37.get(), t38.get(), t39.get()],
               [t41.get(), t42.get(), t43.get(), t44.get(), t45.get(),
                t46.get(), t47.get(), t48.get(), t49.get()],
               [t51.get(), t52.get(), t53.get(), t54.get(), t55.get(),
                t56.get(), t57.get(), t58.get(), t59.get()],
               [t61.get(), t62.get(), t63.get(), t64.get(), t65.get(),
                t66.get(), t67.get(), t68.get(), t69.get()],
               [t71.get(), t72.get(), t73.get(), t74.get(), t75.get(),
                t76.get(), t77.get(), t78.get(), t79.get()],
               [t81.get(), t82.get(), t83.get(), t84.get(), t85.get(),
                t86.get(), t87.get(), t88.get(), t89.get()],
               [t91.get(), t92.get(), t93.get(), t94.get(), t95.get(),
                t96.get(), t97.get(), t98.get(), t99.get()]]
        t.delete('1.0', END)
        condition = True
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                lst[i][j] = lst[i][j].strip()
                if not lst[i][j].isnumeric() and lst[i][j] != '':
                    condition = condition and False
                elif lst[i][j] == '':
                    lst[i][j] = '0'
                    condition = condition and True
                elif int(lst[i][j]) > 9:
                    condition = condition and False
        if condition:
            sudoku = su.Sudoku(lst)
            if sudoku.can_solve():
                t.delete('1.0', END)
                t.insert(INSERT, str(sudoku))
                new_win.destroy()
            else:
                messagebox.showinfo("警告", '您输入的数可能有重复')
        else:
            messagebox.showinfo("警告", '您所输入的值超出最大限度或不是数字1-9')

    new_win = Toplevel(window)
    new_win.geometry('500x600+800+400')
    new_win.title('请手动输入数独')
    # 关闭按钮
    btn_close_new = Button(new_win, text='关闭该页面', command=new_win.destroy)
    btn_close_new.place(relx=0.7, rely=0.8)
    btn_get_new = Button(new_win, text='将值代入并关闭窗口', command=forward)
    btn_get_new.place(relx=1/13, rely=60/78)
    # 81格
    ft = tf.Font(family='Times New Roman', size=18)
    # 第一行9格
    t11 = Entry(new_win, font=ft)
    t11.place(relx=1/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t12 = Entry(new_win, font=ft)
    t12.place(relx=2/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t13 = Entry(new_win, font=ft)
    t13.place(relx=3/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t14 = Entry(new_win, font=ft)
    t14.place(relx=5/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t15 = Entry(new_win, font=ft)
    t15.place(relx=6/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t16 = Entry(new_win, font=ft)
    t16.place(relx=7/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t17 = Entry(new_win, font=ft)
    t17.place(relx=9/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t18 = Entry(new_win, font=ft)
    t18.place(relx=10/13, rely=5/78, relwidth=1/13, relheight=5/78)
    t19 = Entry(new_win, font=ft)
    t19.place(relx=11/13, rely=5/78, relwidth=1/13, relheight=5/78)
    # 第二行9格
    t21 = Entry(new_win, font=ft)
    t21.place(relx=1/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t22 = Entry(new_win, font=ft)
    t22.place(relx=2/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t23 = Entry(new_win, font=ft)
    t23.place(relx=3/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t24 = Entry(new_win, font=ft)
    t24.place(relx=5/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t25 = Entry(new_win, font=ft)
    t25.place(relx=6/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t26 = Entry(new_win, font=ft)
    t26.place(relx=7/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t27 = Entry(new_win, font=ft)
    t27.place(relx=9/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t28 = Entry(new_win, font=ft)
    t28.place(relx=10/13, rely=10/78, relwidth=1/13, relheight=5/78)
    t29 = Entry(new_win, font=ft)
    t29.place(relx=11/13, rely=10/78, relwidth=1/13, relheight=5/78)
    # 第三行9格
    t31 = Entry(new_win, font=ft)
    t31.place(relx=1/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t32 = Entry(new_win, font=ft)
    t32.place(relx=2/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t33 = Entry(new_win, font=ft)
    t33.place(relx=3/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t34 = Entry(new_win, font=ft)
    t34.place(relx=5/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t35 = Entry(new_win, font=ft)
    t35.place(relx=6/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t36 = Entry(new_win, font=ft)
    t36.place(relx=7/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t37 = Entry(new_win, font=ft)
    t37.place(relx=9/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t38 = Entry(new_win, font=ft)
    t38.place(relx=10/13, rely=15/78, relwidth=1/13, relheight=5/78)
    t39 = Entry(new_win, font=ft)
    t39.place(relx=11/13, rely=15/78, relwidth=1/13, relheight=5/78)
    # 第四行9格
    t41 = Entry(new_win, font=ft)
    t41.place(relx=1/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t42 = Entry(new_win, font=ft)
    t42.place(relx=2/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t43 = Entry(new_win, font=ft)
    t43.place(relx=3/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t44 = Entry(new_win, font=ft)
    t44.place(relx=5/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t45 = Entry(new_win, font=ft)
    t45.place(relx=6/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t46 = Entry(new_win, font=ft)
    t46.place(relx=7/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t47 = Entry(new_win, font=ft)
    t47.place(relx=9/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t48 = Entry(new_win, font=ft)
    t48.place(relx=10/13, rely=25/78, relwidth=1/13, relheight=5/78)
    t49 = Entry(new_win, font=ft)
    t49.place(relx=11/13, rely=25/78, relwidth=1/13, relheight=5/78)
    # 第五行9格
    t51 = Entry(new_win, font=ft)
    t51.place(relx=1/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t52 = Entry(new_win, font=ft)
    t52.place(relx=2/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t53 = Entry(new_win, font=ft)
    t53.place(relx=3/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t54 = Entry(new_win, font=ft)
    t54.place(relx=5/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t55 = Entry(new_win, font=ft)
    t55.place(relx=6/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t56 = Entry(new_win, font=ft)
    t56.place(relx=7/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t57 = Entry(new_win, font=ft)
    t57.place(relx=9/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t58 = Entry(new_win, font=ft)
    t58.place(relx=10/13, rely=30/78, relwidth=1/13, relheight=5/78)
    t59 = Entry(new_win, font=ft)
    t59.place(relx=11/13, rely=30/78, relwidth=1/13, relheight=5/78)
    # 第六行9格
    t61 = Entry(new_win, font=ft)
    t61.place(relx=1/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t62 = Entry(new_win, font=ft)
    t62.place(relx=2/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t63 = Entry(new_win, font=ft)
    t63.place(relx=3/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t64 = Entry(new_win, font=ft)
    t64.place(relx=5/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t65 = Entry(new_win, font=ft)
    t65.place(relx=6/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t66 = Entry(new_win, font=ft)
    t66.place(relx=7/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t67 = Entry(new_win, font=ft)
    t67.place(relx=9/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t68 = Entry(new_win, font=ft)
    t68.place(relx=10/13, rely=35/78, relwidth=1/13, relheight=5/78)
    t69 = Entry(new_win, font=ft)
    t69.place(relx=11/13, rely=35/78, relwidth=1/13, relheight=5/78)
    # 第七行9格
    t71 = Entry(new_win, font=ft)
    t71.place(relx=1/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t72 = Entry(new_win, font=ft)
    t72.place(relx=2/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t73 = Entry(new_win, font=ft)
    t73.place(relx=3/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t74 = Entry(new_win, font=ft)
    t74.place(relx=5/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t75 = Entry(new_win, font=ft)
    t75.place(relx=6/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t76 = Entry(new_win, font=ft)
    t76.place(relx=7/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t77 = Entry(new_win, font=ft)
    t77.place(relx=9/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t78 = Entry(new_win, font=ft)
    t78.place(relx=10/13, rely=45/78, relwidth=1/13, relheight=5/78)
    t79 = Entry(new_win, font=ft)
    t79.place(relx=11/13, rely=45/78, relwidth=1/13, relheight=5/78)
    # 第八行9格
    t81 = Entry(new_win, font=ft)
    t81.place(relx=1/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t82 = Entry(new_win, font=ft)
    t82.place(relx=2/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t83 = Entry(new_win, font=ft)
    t83.place(relx=3/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t84 = Entry(new_win, font=ft)
    t84.place(relx=5/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t85 = Entry(new_win, font=ft)
    t85.place(relx=6/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t86 = Entry(new_win, font=ft)
    t86.place(relx=7/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t87 = Entry(new_win, font=ft)
    t87.place(relx=9/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t88 = Entry(new_win, font=ft)
    t88.place(relx=10/13, rely=50/78, relwidth=1/13, relheight=5/78)
    t89 = Entry(new_win, font=ft)
    t89.place(relx=11/13, rely=50/78, relwidth=1/13, relheight=5/78)
    # 第九行9格
    t91 = Entry(new_win, font=ft)
    t91.place(relx=1/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t92 = Entry(new_win, font=ft)
    t92.place(relx=2/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t93 = Entry(new_win, font=ft)
    t93.place(relx=3/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t94 = Entry(new_win, font=ft)
    t94.place(relx=5/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t95 = Entry(new_win, font=ft)
    t95.place(relx=6/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t96 = Entry(new_win, font=ft)
    t96.place(relx=7/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t97 = Entry(new_win, font=ft)
    t97.place(relx=9/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t98 = Entry(new_win, font=ft)
    t98.place(relx=10/13, rely=55/78, relwidth=1/13, relheight=5/78)
    t99 = Entry(new_win, font=ft)
    t99.place(relx=11/13, rely=55/78, relwidth=1/13, relheight=5/78)


window = Tk()
window.title('数独Calculator')
window.geometry('250x200+800+400')
# 界面布置, 区分框架
# title = Label(window, text='数独Calculator -power by Yorafa',
#               fg='black', width=80, height=2, relief=SUNKEN)
# title.pack()

# 工具栏
menu = Menu(window)

# 菜单栏
# m1 = Menu(menu)
# 给工具栏上名字
# menu.add_cascade(label="文件", menu=m1)

# 给工具栏上功能
menu.add_command(label='打开', command=open_file)
menu.add_command(label='手动输入', command=new_window)
menu.add_command(label="解", command=go_solve)
menu.add_command(label="关于此软件", command=about_me)
menu.add_command(label="退出", command=window.destroy)

# 显示菜单栏
window.config(menu=menu)


# 按钮
# btn01 = Button(window)
# btn01['text'] = "解数独"
# btn01.bind("<Button-1>", go_solve)
# btn01.pack()

t = Text(window, height=50)
t.pack()
file_reminder = Label(window, text='')
file_reminder.pack()

window.mainloop()
