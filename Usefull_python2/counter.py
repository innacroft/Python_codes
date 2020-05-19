myArray = [1,2,2,4,5,6,7,8,8,8]
counter = 0
num = myArray 
      
for i in myArray:
  curr_frequency = myArray.count(i) 
  if(curr_frequency> counter):
    counter = curr_frequency 
    num = i
print("Counter" ,counter)
print("Number", num)
