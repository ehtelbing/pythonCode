oddnum=int(input('please input number (must odd number):'))
i=1

# while i<=oddnum:
#     a=[i for i in range(oddnum+1)]
#     print(a[i])
#     i+=1
"""
输出结果为：
please input number (must odd number):3
1
2
3

"""

# while i <= oddnum:
#     b=[i for i in range(oddnum)]
#     print(b)
#     i+=1
"""
out value：
please input number (must odd number):3
[0, 1, 2]
[0, 1, 2]
[0, 1, 2]
"""
c=[]
for i in range(oddnum):
    c.insert(i,i+1)
    #此时循环体里输出-会依次输出
    # print(c)
   #  """
   #  out print:
   #  please input number (must odd number):3
   # [1]
   # [1, 2]
   # [1, 2, 3]
   #  """

    # 循环体里输出加判断：用if
    # if i+1==oddnum:
    #     print(c)
    #     """
    #     out print:
    #     please input number (must odd number):3
    #     [1, 2, 3]
    #     """

#assert 需要放在 i=i+1 放在循环体内 第一种判断：
#     i+=1
# assert oddnum==i
# print(c)
# """
# out print :
# please input number (must odd number):3
# [1, 2, 3]
#
# """

print(c)
"""
out print :
please input number (must odd number):3
[1, 2, 3]

"""
# j=1
# k=1
# for j in (oddnum+1)/2:
#     for k in (oddnum-1)/2:
#         print(" ")
#     for t in t+2
d=[]
j=1
for i in range(oddnum):
    if i==0 :
        d.insert(i, j)
    else:
        d.insert(i, j)
    j=j+2


print(d)

"""
out print :
please input number (must odd number):5
[1, 2, 3, 4, 5]  # c[]
[1, 3, 5, 7, 9]  # d[]
"""

p=0
k=0
a=0
e=[]
f=[]
temp=[]
"""
>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
10 输出不能到10
"""
row=int((oddnum+1)/2)
column=oddnum  #int(oddnum - 1)
half_column=int((oddnum-1)/2)
for a in range(oddnum):
    print(a)
for p in range(row):
    # print(p)
    """
    out print value:
    0
    1
    2
    """
    for k in range(column):
        if k<=half_column:
            if p + k >= column:
                print("*", end="")
            else:
                print(" ", end="")
        if k>half_column:
            if k-p<=int(column/2):
                print("*", end="")
            else:
                print(" ", end="")
        if k==half_column:
            print("\n")




