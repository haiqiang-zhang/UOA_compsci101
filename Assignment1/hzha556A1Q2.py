"""
Name: Haiqiang Zhang
Username: hzha556
ID number: 237994789
Description: Q2   A program that generates a University of Auckland username.
"""
import random
print("*********************************************")
print("  University of Auckland Username Generator")
print("*********************************************")
print()
prompt = input("Please enter your name: ")
first = prompt[0].lower()
sur_num = prompt.find(" ")
sur = prompt[sur_num+1:sur_num+4].lower()
random_num = str(random.randrange(1,999))
random_num = "00"+random_num
random_num = random_num[-3:]
print()
print("Your username is ",first,sur,random_num,sep = "")
