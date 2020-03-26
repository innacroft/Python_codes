def rec_add(num):
    if num == 0:
        return 0
    else:
        return num + rec_add(num-1)
        
if __name__ == "__main__":
    number=int(raw_input("Please enter number : "))
    result=rec_add(number)
    print("Result of Recursive addition is: {} " .format(result))