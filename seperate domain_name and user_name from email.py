dict={}
for i in range(0,2):
    str=input("Enter email id")
    length=len(str)
    c=str.find('@')
    d=str[0:c]
    e=str[c+1:length]
    dict[d]=(e)
print(dict)