num=98457
sum=0
while num>0:
    digit= num % 10
    sum= sum + digit
    num= num//10
print("The sum of the digits =", sum)