# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. (6, 1, 30, 6, 2, 10 result 40 sec.)
a=int(input("Enter the hour:"))
b=int(input("Enter the minute:"))
c=int(input("Enter th second"))
x=int(input("Enter the 2 hour:"))
y=int(input("Enter the 2 minute:"))
z=int(input("Enter the 2 second:"))
print((x-a)*3600 + (y-b)*60 + z-c)
# first_in= input("Enter the hour, minute and seconds with ,: ")
# second_in = input("Enter the hour, minute and seconds with ,: ")
# time_1 = first_in.split(',')
# time_2 = second_in.split(',')
# print(time_2, time_1)
