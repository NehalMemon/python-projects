# # calculate the area of rectangle
def area(length,breath):
    print(length*breath)
area(5,3)
   
# # check if number is odd or even
def checker(number):
    if number % 2 ==0:
        print(number ,"is even number")
    else:
        print( number , "is odd number")  
checker(29)
  
# reversing the  string
string="hello"
reversed_string= string[-1:-6:-1]
print(reversed_string)

# find the factorial of number
def factorial(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return x
n=int(input("Enter number..."))  
result=factorial(n)  
print(result)  


# check if string is palindrome
def palindrome_checker():    
    string="radar"
    reverse_string=string[-1:-6:-1]
    if string==reverse_string:
        print("String is palindrome")
    else:
        print("string is not palindrome")    
palindrome_checker()

 # creating fibonacci series upto n terms
def fibonacci_series(n):
    n1=0
    n2=1
    list=[n1,n2]
    for i in range(n-2):
        i=n1+n2
        n1=n2
        n2=i
        list.append(i)
    return list
n=6
fs=fibonacci_series(n)    
print(fs)

#finding the largest number
def largest_number():
    numbers="10 25 5"
    lst=numbers.split()
    l_num=max(lst)
    return l_num
l_num=largest_number()
print(f"The largest number is{l_num}")

# # calculation of simple interest
def simple_interest(principal_amount,R_O_T,time):
    x=principal_amount*R_O_T*time
    simple_interest =x/100
    print(simple_interest)
simple_interest(1000,5,2)



# # temperature converter
def temperature(c):
    x=(9/5*c)
    F=x +32
    print(f"temperature in Fahrenheit is{F}")
temp=temperature(37) 
print(temp)

# # leap year checker
def year(year):
    if year % 4==0:
        print("the year",year,"is leap year" )
    else:
        print("the year",year ,"is not leap year" ) 
year(2024)        

# # Finding the median of given numbers
import numpy as np
def median():
    numbers=input("Enter numbers...")
    num=numbers.split()
    list=[]
    for i in num:
        list.append(int(i)) 
    arr=np.array(list)
    median=np.median(arr)
    return median
median_=median()
print(f"the median of givin numbers is..{median_}")    
       



#number of words in string
def string_length():
    string="the quick brown fox jumps over the lazy dog"
    x=string.split()
    print(len(x))
string_length()    



# sum of digits entered as string
def sum_of_string():
    number=("12345")
    sum=0
    for i in number:
        sum += int(i)
    print(sum) 
sum_of_string()    

# # longest common string
string = "flower flow flight"
common_string = ""
list_ = string.split()
list_.sort()

f_word = list_[0]
l_word = list_[-1]

for i in range(min(len(f_word), len(l_word))):
    if f_word[i] == l_word[i]:
        common_string = common_string + f_word[i]
    else:
        break  
print(common_string)
# I found it too hard and complete it with the help of chat gpt


# # checking whether number is prime or not
def prime_number():
      num=(input("Enter number..."))
      sum=0
      for i in num:
          sum += int(i)
      if sum%3==0:
          print(f"{num} is not a prime number")  
      else:
          print(f"{num} is  a prime number") 
prime_number()          
          
                 

    
    
    

# # consecutive sequence    
list=[100,4,200,1,3,2] 
list.sort()
r=[]
for i in  list:
    if i+1  in list:  
        r.append(i)
    elif i-1 in list: 
        r.append(i)      
    else:
        break   
print(r) 
  
   






