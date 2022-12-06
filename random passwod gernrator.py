import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSUVWXYZ"
number = "0123456789"
string = lower_case + upper_case + number
length = 8

password = "". join(random.sample(string, length))

print("your new password is :" + password)
