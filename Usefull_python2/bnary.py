lst = ["a", "b", "a", "c", "c", "a", "c"]
temp=set(lst)
result={}
for i in temp:
    result[i]=lst.count(i)


for key, value in result.items():
    valor=int(value)
    print (key,": ",valor * '*')