# 1) wap for find maximum between two numbers.
'''a = int(input('enter the first number: '))
b = int(input('enter the second number: '))
if a > b:
    print('a', 'is greater than', 'b')
else:
    print('b', 'is greater than', 'a')'''

# 2) wap for find maximum between three numbers.
''' a = int(input('enter the first number'))
b = int(input('enter the second number'))
c = int(input('enter the third number'))
print('maximum is', end=' ')
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >=b:
    print(c) '''

# 3) wap to check wheather number is positive, negative or zero.
'''num = int(input('enter the number: '))
if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print('num is negative')'''

# 4) wap number is divisible by 5 or not
''' a = int(input('enter the number'))
if a % 5 == 0:
    print(a, 'is divisible by 5')
else:
    print(a, 'is not divisible by 5') '''

# 5) wap is number is even or odd.
'''b = int(input('enter the number:- '))
if b % 2 == 0:
    print(b, 'is even number')
else:
    print(b, 'is odd number')'''

# 6) wap for check leap year or not.
'''c = int(input('enter the Year'))
if c % 100 == 0 or c % 4 == 0:
    print(c, 'is leap year')
else:
    print(c, 'is not leap year')'''

# 7) wap for check char is alphabate or not
''' char = input('enter any character ')
if char.isalpha():
    print(char, 'is alphabate')
else:
    print(char, 'is not alphabate')'''

# 8) wap for check vowel or constant.
'''a = input('enter the alphabate: ')
b = 'a', 'e', 'i', 'o', 'u'
if a in b:
    print('given alphabate is vowel')
else:
    print('given is constant ')'''

# 9) wap to check character is upper case or lower case.
'''char = input('enter the character')
if char.isupper():
    print('given character is upper case')
elif char.islower():
    print('given character is in lower case')
else:
    print('given character is mix')'''

# 10) wap total number of notes in given amount
'''am = int(input('enter the amount'))
nt = int(input('enter the note to be count'))
print(am//nt)'''

# 11) wap enter the three angles and check it is traingle or not
a = int(input('enter the first angle'))
b = int(input('enter the second angle'))
c = int(input('enter the third angle'))
if a + b + c == 180:
    print('the given angles of triangle')
else:
    print('the given angle is not triangle')




