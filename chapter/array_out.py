
#三种方法输出数组
i=0;
arr=[1,2,3,5,3,2]

for item in arr:
    print(item)


for index in range(len(arr)):
    #此处arr本身为int型数组，因此需要arr[index]需要转换str(arr[index])
    #如果arr为str型数组 则表达式ret=str(index)+"..."+arr[index]
    ret=str(index)+"..."+str(arr[index])
    print(ret)


for index,val in enumerate(arr):
    print(str(index) + "--" + str(val));