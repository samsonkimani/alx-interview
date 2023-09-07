#!/usr/bin/python3

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def multiples(element, newSet):
    newArray = []
    for i in range(len(newSet)):
        if newSet[i] % element == 0:
            newArray.append(newSet[i])
    if len(newArray) >= 1:
        return newArray
    else:
        return None


def isWinner(x, nums):
    winner = {
            "Maria": 0,
            "Ben": 0
            }

    for num in nums:

        newSet = []
        for i in range(num):
            newSet.append(i)
        
        primes = []
        for element in newSet:
            isprime = isPrime(element)
            if isprime == True:
                primes.append(element)
        if len(primes) % 2 == 0:
            winner["Maria"] += 1
        winner["Ben"] += 1

        print(winner)
        if winner['Maria'] > winner['Ben']:
            return "Maria"
        elif winner['Maria'] == winner['Ben']:
            return None
        else:
            return "Ben"
