

#1-10 循环输出
x=1
while x<=10:
    print(x)
    x+=1

#求1-10 总和
x=1
t=1
while x<=10:
    x=x+1
    t=x+t         #当前值之前的总和+当前值
    if x==10:
        print(t)   #输出求和数

#1-10 求和分步查看
x=1
t=1
while x<=3:
    print(x)  #当前循环的数值
    x=x+1
    print(x)  #下一个数值
    t=t+x
    print(t)  #之前的sum值+当前值



array=["bill","mary","john"]
i=0
j=1
print(len(array))
while i<=len(array):
    for arr in array[i]:
        i=i+1
        print(arr, end="")
    print("\n")
while j<len(array):
    print(array[j],end=" ")
    j=j+1
