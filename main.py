#Write your code below this row 👇

#total = 0
#number_as_string3 = 3
#number_as_string5 = 5
#number_as_string15 = 15
#total2 = 3
number = 0
for number in range (1,101):
  #total = number + 1
  if (number % 3 == 0 and number % 5 ==0):
      #number_as_string5 = str(number)
      #number_as_string5 = "FizzBuzz"
      print("FizzBuzz")
     
  if (number % 3 == 0):
      #number_as_string3 = str(number)
      #number_as_string3 = "Fizz"
      print("Fizz")
  if (number % 5 == 0):
      #number_as_string5 = str(number)
      #number_as_string5 = "Buzz"
      print("Buzz")
  

  # No need to total as I am not adding the numbers 
  #else:
     # print(number)

      #print(type(number_as_string3)) 

      #print(type(number_as_string5)) 
  #total = number
  #if (total % 3 == 0 and total % 5 ==0):
   # print("FizzBuzz")
  #if (total % 3 == 0):
   # print("Fizz")
  #if (number % 5 == 0):
   # print("Buzz")
  #if (number % 15 == 0):
   #   number_as_string15 = str(number)
     # number_as_string15 = "FizzBuzz"
      #print(type(number_as_string15))  
  #total = (number + 1+ number_as_string3 + number_as_string5 + number_as_string15)
  print(number)




