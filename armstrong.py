num = int(input("Enter ant positive integer:"))
def check_armstrong(num):
     if num in range(1,10):
         return true
     order = len(str(num))
     sum = 0
     original = num
     while num>0:
        digit = num % 10
        sum += digit ** order
        num = num // 10
     if sum == original:
        return true
        return false
     if check_armstrong(number):
        print("number is armstrong")