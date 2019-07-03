

def recur_sum(n):                                     #  recursive function

   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)


num=int(input("Enter The Number: "))                  #  read limit




if num < 0:                                           #  check whether the number is positive
   print("Enter a positive number")
else:
   print("The sum is: ",recur_sum(num))               #  print sum
