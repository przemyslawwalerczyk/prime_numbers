a = None
while a != 0:
  number = int(input("Provide a number [2-1000]: "))
  prime = True
  
  if number > 1 and number <=1000:
    for i in range(2, number-1):
      if number % i == 0:
        prime = False
        break
    if prime == True:
      print(number, 'is prime number\n')
    else:
      print(number, 'is NOT prime number\n')
  else:
    print('Incorrect number!\n')





