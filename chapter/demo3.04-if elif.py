name=input('your name:')
if name.startswith("Bill"):    #第一个if---start
    if name.endswith("Gates"):   #第二个if---start
        print("Hello Mr. Bill Gates ")
    elif name.endswith("Clinton"):
        print("hello Mr. Clinton")
    else:
        print("none -name")       #第二个if -----end
elif name.startswith("li"):
    if name.endswith("ning"):
        print("hello Lining")
    else:
        print("none")
else:
    print("none name")       #第一个if -----end

