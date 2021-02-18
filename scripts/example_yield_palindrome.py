#!/usr/bin/env python

def is_palindrome(num2):
    # Skip single-digit inputs
    if num2 // 10 == 0:
        return False
    temp = num2
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num2 == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
                print(i)
        num += 1


pal_gen = infinite_palindromes()
for j in pal_gen:
    digits = len(str(j))
    pal_gen.send(10 ** digits)



