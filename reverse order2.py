def converttobinary(n):
   if n>1:
       converttobinary(n//2)
   print(n % 2,end = '')
dec = int(input("enter a number: "))
converttobinary(dec)
print()