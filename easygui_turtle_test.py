import easygui as g
# 事件驱动型
# easygui.egdemo()    # 演示程序
# 直到点击ok之后才会执行下一行语句
g.msgbox(msg='Hello World', title='welcome', ok_button='got it', image=None, root=None)

g.choicebox(msg='Pick an item', title='You have to make a choice', choices=['dota','lol','csgo'])
# choices中需用序列(元组/列表)
g.textbox(msg='Hello World',title='wow', text='''please choose your hero''',codebox=0)

g.passwordbox(msg='Enter your password.', title='Don\'t move', default='222', image=None, root=None)
# easygui.enterbox(msg='Enter your password.', title='Don\'t move', default='222', image=None, root=None)

g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
# 返回用户选择的文件名(带完整路径)，default代表默认路径

# 例子
import sys

while 1:
    g.msgbox('欢迎来到dota大陆')
    msg = '你希望玩几号位'
    title = '别瞎选'
    choices = ['1号位','2号位','3号位','4号位','5号位']
    choice = g.choicebox(msg,title,choices)

    g.msgbox('你的选择是' + str(choice),'谢谢参与')
    msg = '你需要重新选择吗'
    title = '你确定吗'
    if g.ccbox(msg,title):
        pass
    else:
        # break
        sys.exit(0)


# 画等边三角形
import turtle       # 导入turtle模块

p = turtle.Pen()   # 创建一支画笔（海龟）
p.pencolor('blue')  # 设置画笔顔色为黑色
p.pensize( 5 )      # 设置画笔的粗细为5
p.forward(100)      # 最初画笔（海龟）朝向正右方，向前画长度为100的直线
p.left(120)         # 画笔（海龟）向左转120度
p.forward(100)      # 向前画长度为100的直线
p.left (120)        # 画笔（海龟）向左转120度
p.forward(100)      # 向前画长度为100的直线
p.left(120)         # 画笔（海龟）向左转120度

# 画直线
import turtle
t = turtle.Turtle()
w = turtle.Screen()
t.forward(100)
turtle.done()

# 画正方形
t = turtle.Turtle()
w = turtle.Screen()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()

# 画五边形
t = turtle.Turtle()
w = turtle.Screen()
for i in range(5):
    t.forward(100)
    t.right(72)
turtle.done()

# 画六边形
t = turtle.Turtle()
w = turtle.Screen()
for i in range(6):
    t.forward(100)
    t.right(60)
turtle.done()

# 画五角星
t = turtle.Turtle()
w = turtle.Screen()
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()

# 画二叉树
def tree(branchLen,t):# 树干长度，海龟
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75,t)
    myWin.exitonclick()
main()