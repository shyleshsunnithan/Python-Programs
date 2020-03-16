lower=int(input("Enter The Lower Limt : ")) # read the lower limit
upper=int(input("Enter The Upper Limit : ")) # read the upper limit
print("Prime numbers between",lower,"and",upper,"are:") #print numbers b/w lower and upper limit

for num in range(lower,upper + 1):

   if num > 1:
       for i in range(2,num): #for loop initialized
           if (num % i) == 0: #checkin for prime
               break
       else:
           print(num) #print prime number
