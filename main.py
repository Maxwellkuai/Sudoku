#GUi获取数据
import pickle
from tkinter import *
from tkinter import messagebox
import time

#------------------------------------幕布
root =Tk()
root.geometry("500x700+500+500")
#-------------------------------------------背景
photo=PhotoImage(file="/Users/maxwellsmbp/sudoku2/lib/u=2108388162,2472497653m=26p=0.png")
photo2=PhotoImage(file='/Users/maxwellsmbp/sudoku2/lib/u=4167379140,1632183289m=26p=0.png')

imglabel=Label(root,image=photo)
imglabel.place(x=250,y=480)
imglabel2=Label(root,image=photo2)
imglabel2.place(x=-210,y=390)
#------------------------------------数据
global sudoku  #定义全局变量不可以赋值 #初始的数据
global gong
global sudokurow #以行读取
global sudokucol #以列读取
global ans  #存放结果

gong=[]
sudoku=[]
sudokurow=[]
sudokucol=[]
sudokux=[]
isempty=[[]for i in range(0,81)]   #
#GUI数据变量
datainput=[0 for i in range(81)]
ans=[]
timeans=0
process=[]
data=[0 for i in range(0,81)]
isstart=1
isfirstshow=0#第一次是否出错
isfirst=0
isans=0
#------------------------------------标签
def label():
    #标签一
    L_titile = Label(root, text='数独游戏', )#调整字体
    L_titile.config(font='Helvetica -30 bold', fg='lightblue')
    L_titile.place(x=250, y=20, anchor="center")
    #标签二
    L_titile2 = Label(root, text='请输  入数字：', )#调整字体
    L_titile2.config(font='Helvetica -14 bold', fg='green')
    L_titile2.place(x=41, y=40, anchor="center")
    #正确答案为
    L_titile3 = Label(root, text='正确答案：', )#调整字体
    L_titile3.config(font='Helvetica -14 bold', fg='green')
    L_titile3.place(x=40, y=380, anchor="center")
    #用时
    Label1 = Label(root, text='用时(秒):')
    Label1.config(font='Helvetica -14 bold', fg='green')
    Label1.place(x=304, y=63, anchor="center")
    #文本框
label()

#------------------------------------输入框1
v = [[] for i in range(81)]  # v=StringVar（）输入框的格式
e = [[] for i in range(81)]  # e【i】
v2=[[] for i in range(81)]  #v=StringVar（）输入框的格式
e2=[[] for i in range(81)]  #e【i】
vtime=StringVar()
etime=Entry(root, width=20,insertbackground = 'blue',insertontime =50,relief = 'sunken',textvariable=vtime)
#文本框
text = Text(root, width=30, height=20, fg='blue')
text.place(x=380, y=230, anchor="center")
data = [0 for i in range(81)]
for i in range(0, 81):
    v[i] = StringVar()
for i in range(0, 9):
    for j in range(0, 9):
        location = i * 9 + j
        e[location] = Entry(root, textvariable=v[location], width=2, insertbackground='blue', insertontime=50,
                            relief='ridge',highlightcolor='red',highlightthickness=1,
                            foreground='red')  # 一些参数
        e[location].place(x=30 * j + 0, y=30 * i + 50)  # 如何消除文本框的外部间隔,如何调整位置
#---------------------------------一些函数
def xianshijieguo():
    global isans
    for i in range(0,81):
         v2[i]=StringVar()

    for i in range(0,9):
        for j in range(0,9):
            location1=i*9+j
            e2[location1]= Entry(root, width=2,insertbackground = 'blue',insertontime =50,relief = 'ridge',
                                             textvariable=v2[location1],highlightcolor='red',highlightthickness=1,
                                             )#一些参数
            v2[location1].set(ans[location1])
            e2[location1].place(x=30*j+0,y=30*i+400)  #如何消除文本框的外部间隔,如何调整位置
                    #e2[location1]['state'] = 'readonly'#定义为不可以修改
def showtime():
    global etime
    global vtime
    vtime.set(timeans)
    etime.place(x=330,y=50)
    #etime['state']='readonly'
def Process():
    global text
    global isans
    if isans==0:
        text.insert(0.0,'抱歉能力有限，解不出来\n请检测输入是否正确')
    if isans==1:
        while len(process)!=0:
            text.insert(1.0, '%s '%(process.pop()))
            text.insert(1.0, '\n')
def show():
    global data
    global isstart
    global false
    global isinput
    global datainput
    global isfirstshow
    global isfirst
    if isstart==0:
        messagebox.askokcancel('错误提示', '请你先按重新玩游戏再输入！！！')
    else:
        false = 0
        isstart=0
        isinput = 0
        isfirst+=1
        #print('未获取的ans')
        #print('未获取的data')
        #print(ans)
        #print(data)
        for i in range(0,81):
            a = e[i].get()  # 获取数据
            if a.isdigit():
                digitala = int(a)

                if 1 <= digitala <= 9:
                    data[i] = digitala
                    isinput = 1
                else:
                    messagebox.askokcancel('错误提示', '请输入数字1-9\n请将错误输入删除并正确操作！！！')
                    false = 1
                    isinput=1
                    isfirstshow=1
            else:
                if a.isalpha():#    全字母
                    messagebox.askokcancel('错误提示', '请输入阿拉伯数字\n请将错误输入删除并正确操作！！！')
                    isinput=1
                    false = 1
                    isfirstshow=1
                else:
                    if  a!='':#空格也算其他字符，会弹出81-n次
                        messagebox.askokcancel('错误提示', '请输入正整数\n请将错误输入删除并正确操作！！！')
                        isinput = 1
                        false = 1
                        isfirstshow=1

        #print('获取后第一次的data')
        #print(data)
        #print('获取后第一次ans')
        #print(ans)

        if isinput == 0:
            messagebox.askokcancel('错误提示', '您还未输入数字\n请输入！！！')
            isfirstshow = 1

        else:
            if (false == 0):

                datainput = data
                # 调用各个窗口
                Processdata()
                check=1
                core()
                xianshijieguo()
                showtime()
                Process()


def restart():
    global e
    global e2
    global etime
    global vtime
    global text
    global  isempty
    global  sudoku
    global  sudokurow
    global sudokucol
    global sudokux
    global gong
    global ans
    global timeans
    global data
    global isstart
    global isfirstshow
    global isfirst
    isstart=1
    data=[0 for i in range(0,81)]
    timeans=0
    ans=[]
    isempty = [[]for i in range(0,81)]
    sudoku = []
    sudokux = []
    sudokurow = []
    sudokucol=[]
    print('restart里的col有没有更新？')
    print(sudokucol)
    gong = []
    #print('resart的ans：')
    #print(ans)
    #清除输入框
    for i in range(0,81):
        e[i].delete(0,END)
        if isfirstshow==0: #如果不是第一次的第一次出错
            e2[i].delete(0,END) #如果用上面e2[location1]['state'] = 'readonly'#定义为不可以修改。无法清除
    etime.delete(0,END)
    text.delete(0.0, END)#SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常
                                     #SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异
    isfirstshow=0
Button(root, text='确定输入', width=10, command=show).place(x=30, y=320)
Button(root,text='重新玩游戏',width=10,command=restart).place(x=150,y=320)
#-----------------------------------------------------------------------------------------------对数据进行相关处理
def Processdata():
    global sudoku
    global sudokucol
    global sudokurow
    global sudokux
    global isempty
    global gong
    sudoku = datainput
    #print(sudoku)
    #print('为获取数据的isempty')
    #print(isempty)
    #读取行
    for i in range(0,81,9):
        sudokurow.append(sudoku[i:i+9])
    #获取每列的数据
    for i in range(0,9):
        sudokucol.append(sudoku[i:81:9])           #以列表切片的方法获取列
    #获取每个宫
    gong1=[]                               #定义一个列表暂时存储变量
    for j in range(0,9,3):
        for i in range(0,9):
            gong1.extend(sudokurow[i][j:j+3])          #以九宫格的顺序单独添加到列表中

    for i in range(0,81,9):
        gong.append(gong1[i:i+9])
    #判断改格子是否填入数字
    for i in range(0,81):  #in range(0,81)和in sudoku是2种不同情况

        if sudoku[i]==0:
            isempty[i].append(0)
        else:
            isempty[i].append(1)   #若为0，则标志为0
    #print("新的isempty")
    #print(isempty)

    #把每一个格子都定义为一个对象
    class Object(object):
        #定义行、列、宫，空的属性
        def __init__(self,n,flag,value):
            self.row=(n//9)     #行坐标
            self.col=(n%9)      #列坐标
            self.gong=int(self.row//3+(self.col//3)*3)   #宫坐标
            self.flag=flag
            if self.flag==[0]:
                self.value=[1,2,3,4,5,6,7,8,9]
            else:
                self.value=[value]
    for i in range(0,81):
        sudokux.append(Object(i,isempty[i],sudoku[i]))
#-------------------------------------------------------------------------------------------------------调用核心代码

def core():
    global ans
    global timeans
    global process
    global sudoku
    global gong
    global sudokux
    global sudokurow
    global sudokucol
    global isans

    ans=sudoku
    print('新的传给coreans：')
    print(ans)
    print('新的传给coreisempty：')
    print(isempty)
    print('新的core sudurow')
    print(sudokurow)
    print('新的core suducol')
    print(sudokucol)
    print('新的core sudugong')
    print(gong)
    print("新的core sudux是否更新")
    for i in range(81):

        print(sudokux[i].value)
        print(sudokux[i].flag)

    set1=set()
    index=[]
    count=1
    flag2=0
    #计时
    since = time.time()
    count=0
    #开始遍历，当只要有一个未填入就循环
    while([0] in isempty):

        # 判断没有解
        if count>1000 or flag2==1:
            flag2=1
            break
        for i in range(0,81):
            set1 = []
            print('是否执行')
            #判断该格子是否有元素
            if sudokux[i].flag==[1]:
                continue
            else:
                 #获取宫，列，行的元素
                set1=(set(gong[sudokux[i].gong])| set(sudokurow[sudokux[i].row])| set(sudokucol[sudokux[i].col]))
                #删除0
                set1.remove(0)
                #排除该格子里的元素
                for j in set1:           #不能整体删
                    if j in sudokux[i].value:   #判断该格子有这个元素，否则删除一个没有的元素是非法的
                        sudokux[i].value.remove(j)

                #查看是否只有一个元素
                if len(set(sudokux[i].value))==1:
                    #修改数独答案值

                    ans[i]=sudokux[i].value[0]
                    #修改isempty值
                    isempty[i]=[1]
                    #修改对象的flag
                    sudokux[i].flag=[1]

                    #同时更新行，列,宫
                    sudokucol[sudokux[i].col].append(sudoku[i])
                    sudokurow[sudokux[i].row].append(sudoku[i])
                    gong[sudokux[i].gong].append(sudoku[i])



                    #提示已经解出来
                    print("排除法：第[%d]行第[%d]列的值是[%d]"%(sudokux[i].row+1,sudokux[i].col+1,sudoku[i]))
                    process.append("排除法：第[%d]行第[%d]列的值是[%d]"%(sudokux[i].row+1,sudokux[i].col+1,sudoku[i]))

                if len(set(sudokux[i].value))==0:
                    flag2=1
                    break
        print("检验排除法是否执行")
        print(ans)
        print(sudoku)
        #方法二    for i in range(1, 10):  # 表示数字1～9
        for i in range(1, 10):  # 表示数字1～9
            for j in range(0, 9):  # j表示宫
                index = []
                counti = 0
                for k in range(0, 9):  # k表示宫中位置
                    t = ((j % 3) * 3 + k // 3) * 9 + ((j // 3) * 3 + k % 3)
                    if i not in gong[j] and i in sudokux[t].value and sudokux[t].flag == [0]:
                        # 计数
                        counti += 1
                        # 记录位置
                        index.append(t)

                # 修改
                if counti == 1:
                    sudokux[index[0]].value = [i]

                    sudokux[index[0]].flag = [1]
                    isempty[index[0]] = [1]

                    ans[index[0]] = sudokux[index[0]].value[0]
                    sudokucol[sudokux[index[0]].col].append(i)

                    sudokurow[sudokux[index[0]].row].append(i)

                    gong[j].append(i)
                    print("宫内法：第[%d]行第[%d]列的值是[%d]" % (sudokux[index[0]].row + 1, sudokux[index[0]].col + 1, ans[index[0]]))
                    process.append("宫内法：第[%d]行第[%d]列的值是[%d]" % (sudokux[i].row + 1, sudokux[i].col + 1, sudoku[i]))
                # 判断是否在统一行并进行相关操作
                if counti == 2:
                    if sudokux[index[0]].row == sudokux[index[1]].row :
                        # 对这一行都删去i

                        for k in range(0,9):
                            if sudokux[sudokux[index[0]].row*9+k].gong!=j and sudokux[sudokux[index[0]].row*9+k].flag==[0]:
                                if i in  sudokux[sudokux[index[0]].row*9+k].value:
                                    sudokux[sudokux[index[0]].row*9+k].value.remove(i)

                        # 判断是否在同一列并进行相关操作
                    if sudokux[index[0]].col == sudokux[index[1]].col:
                        # 对这一行都删去i
                        for k in range(0,9):
                            if sudokux[sudokux[index[0]].col+9*k].gong!=j and sudokux[sudokux[index[0]].col+9*k].flag==[0]:
                                if i in sudokux[sudokux[index[0]].col+9*k].value:
                                    sudokux[sudokux[index[0]].col+9*k].value.remove(i)
                if counti == 3:
                    if sudokux[index[0]].row == sudokux[index[1]].row == sudokux[index[2]].row:
                        # 对这一行都删去i
                        for k in range(0,9):
                            if sudokux[sudokux[index[0]].row*9+k].gong!=j and sudokux[sudokux[index[0]].row*9+k].flag==[0]:
                                if i in sudokux[sudokux[index[0]].row * 9 + k].value:
                                    sudokux[sudokux[index[0]].row*9+k].value.remove(i)
                        # 判断是否在同一列并进行相关操作
                    if sudokux[index[0]].col == sudokux[index[1]].col == sudokux[index[2]].col:
                        # 对这一行都删去i
                        for k in range(0, 9):
                            if sudokux[sudokux[index[0]].col+9*k].gong != j and sudokux[sudokux[index[0]].col+9*k].flag==[0]:
                                if i in sudokux[sudokux[index[0]].col+9*k].value:
                                    sudokux[sudokux[index[0]].col +9*k].value.remove(i)
        #方法三，行排除法
        for i in range(1, 10):  # 表示数字1～9
            for j in range(0, 9):  # j表示行
                index = []
                counti = 0
                for k in range(0, 9):  # k表示行中列位置
                    t=j*9+k
                    if i not in sudokurow[j] and i in sudokux[t].value and sudokux[t].flag == [0]:
                        # 计数
                        counti += 1
                        # 记录位置
                        index.append(t)

                # 修改
                if counti == 1:
                    sudokux[index[0]].value = [i]

                    sudokux[index[0]].flag = [1]
                    isempty[index[0]] = [1]

                    ans[index[0]] = sudokux[index[0]].value[0]
                    sudokucol[sudokux[index[0]].col].append(i)

                    sudokurow[sudokux[index[0]].row].append(i)

                    gong[sudokux[index[0]].gong].append(i)
                    print("行排除法：第[%d]行第[%d]列的值是[%d]" % (sudokux[index[0]].row + 1, sudokux[index[0]].col + 1, ans[index[0]]))
                    process.append("行排除法：第[%d]行第[%d]列的值是[%d]" % (sudokux[i].row + 1, sudokux[i].col + 1, sudoku[i]))
        #方法四：列排除法
        for i in range(1, 10):  # 表示数字1～9
            for j in range(0, 9):  # j表示列
                index = []
                counti = 0
                for k in range(0, 9):  # k表示行中行位置
                    t=k*9+j
                    if i not in sudokucol[j] and i in sudokux[t].value and sudokux[t].flag == [0]:
                        # 计数
                        counti += 1
                        # 记录位置
                        index.append(t)

                # 修改
                if counti == 1:
                    sudokux[index[0]].value = [i]

                    sudokux[index[0]].flag = [1]
                    isempty[index[0]] = [1]

                    ans[index[0]] = sudokux[index[0]].value[0]
                    sudokucol[sudokux[index[0]].col].append(i)

                    sudokurow[sudokux[index[0]].row].append(i)

                    gong[sudokux[index[0]].gong].append(i)
                    print("列排除法：第[%d]行第[%d]列的值是[%d]" % (sudokux[index[0]].row + 1, sudokux[index[0]].col + 1, ans[index[0]]))
                    process.append("列排除法：第[%d]行第[%d]列的值是[%d]" % (sudokux[i].row + 1, sudokux[i].col + 1, sudoku[i]))



        count+=1
    if [0] in isempty:
        isans=0
    else: isans=1
    #计时结束
    time_elapsed = time.time() - since
    timeans=time_elapsed % 60
    check2=2
    print('结果：')
    print(ans)
#--------------------------------------------------------------------------------------------------------GUi输出


mainloop()