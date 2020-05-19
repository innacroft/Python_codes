lst = [1,2,3,4,5]
temp=set(lst)
result={}
for i in temp:
    result[i]=lst.count(i)

current_val=0
for key, value in result.items():
    valor=int(value)
    if value > current_val:
        value= current_val
        print (key,": ",valor * '*')
    else:
        current_val
        print (key,": ",valor * '*')
    