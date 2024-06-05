# stack =[]
# stack.append("a")
# stack.append("b")
# stack.append("c")
# print("initial stack")
# print(stack)
# print("\n elements poped from stack")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print("\n stack after elements are poped: ")
# print(stack)

# factrial
# num = int(input())
# s = 1
# i = 1
# while i<num+1:
#     s = s*i
#     i+=1
#     if i== num+1:
#         break
# print(s)

# factorial
# num = int(input())
# n1,n2 = 0,1
# count=0
# if num<=0:
#     print("fibonacci not possible please enter positive integer")
#
# elif num==1:
#     print(n1)
# else:
#     while count< num :
#         print(n1)
#         nth = n1+n2
#         n1 = n2
#         n2 = nth
#         count+=1

# armstrong number
# num = int(input("enter number: "))
# #initialize sum
# sum =0
# # finding sum of cube of digits of the number
# temp=num
# while temp>0:
#     digit = temp%10
#     sum += digit**3
#     temp//=10
# if num==sum:
#     print("num is armstrong number")
# else:
#     print("num is not an armstrong number")

# perfect number
# num = int(input())
# sum = 0
# # finding sum of proper divisors of num
# for i in range(1,num):
#     if num%i==0:
#         sum = sum+i
# if sum==num:
#     print("the number is perfect number")
# else:
#     print("not perfect")

# counting nuber of vowels

# def vowel_count(str):
#     count = 0
#     vowel = set("aeiouAEIOU")
#     for alphabets in str:
#         if alphabets in vowel:
#             count+=1
#     print("no. of vowels:",count)
# str = "dvddhdsu kjhvdibnfewoi kvjhdxhsion hvoinvsdoiih kjjsdkjjcnbewosh"
# vowel_count(str)

# dice
import random
while True:
    print("1. to roll the dice     2. to exist")
    user = int(input("what u want to do?\n"))
    if user==1:
        number = random.randint(1,7)
        print(number)
    else:
        break
