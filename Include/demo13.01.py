#在F盘下面有一个文件ABC.txt。
#open()
with open(r'F:\\ABC.txt') as demo:
    for line in demo:
        print(line)
#写入文档（会清空之前文档中的内容）&&读取绝对路径
f=open('../venv/file_source/test.txt','w')
print(f.write('I love'))
f.close()
f=open('../venv/file_source/test.txt','r')
print(f.read())

#读取文件
ftxt=open('../venv/file_source/txt2.txt','r')
print(ftxt.read())

#读取文档字符数量（此处截取六个字符）
ftxt=open('../venv/file_source/txt2.txt','r')
print(ftxt.read(6))


