lower=int(input("Enter The Lower Limt : "))
upper=int(input("Enter The Upper Limit : "))
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):

   if num > 1:
       for i in range(2,num): #for loop initialized
           if (num % i) == 0:
               break
       else:
           print(num)
