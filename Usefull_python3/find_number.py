
def findNumber(lst, numb):
  counter=0
  for i in lst:
    if numb == i:
      counter+=1
  return counter



if __name__ == "__main__":
  lst = [1,2,2,2,2,2,2,3,3,3,4,5]
  numb=2
  print(findNumber(lst, numb))


        