# 1 Palindrome

from xmlrpc.client import Boolean

text = input("word ")


def isPalindrome(word):
    return Boolean(word == word[::-1])


print(isPalindrome(text))


# 2 exerice
totalamount = input("number ")


def minSplit(amount, coins=(50, 10, 5, 20, 10, 1)):
    quantities = dict()
    for coin in coins:
        quantities[coin], amount = divmod(amount, coin)
    return quantities


fun = minSplit(int(totalamount))
print(fun)



