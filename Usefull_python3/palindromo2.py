

new=[]
result={}
def numMostpopular(in_lst):
  temp=set(in_lst)
  for i in temp:
      result[i]=lst.count(i)
  maximum = max(result.values())

  for key, value in result.items():
    if value==maximum:
      new.append(key)
  new.sort()
  return new


if __name__ == "__main__":
  lst = [1,2,2,2,3,3,3,4,5]
  
  print(numMostpopular(lst))


        
    