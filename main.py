# Project 1
# Jonathan Vialpando and Arturo Nunez Gomez
import random
import sys


# Problem 1.

# Input: Two integers p and q with p >= q >= 0
# Output: gcd(p,q)
# Pre-condition of input: p >= q >= 0
# Pseudo Code:
#   if q is equal to 0
#       return p
#   else
#       return gcd (q, p mod q)
def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)


# Input: Two integers p and q which represent the numerator and denominator in a fraction
# Output: Two integers p and q which represent the reduced numerator and denominator in a fraction
# Pre-condition of input: Denominator does not already = 0
# Pseudo Code:
#   new gcd equals gcd(p,q)
#   newP equals p floor newGcd
#   newQ equals q floor newGcd
#   return newP and newQ
def reduceFraction(p, q):
    newGcd = gcd(p, q)
    newP = p // newGcd
    newQ = q // newGcd
    return newP, newQ


# Input: 4 integers p1, q1, p2 and q2 which represent the numerators and denominators in a fraction(p1/q1 and p2/q2)
# Output: Two integers p and q that represent the sum of (p1,q1) + (p2,q2)
# Pre-condition of input: Denominators do not already = 0
# Pseudo Code:
#   denominator equals q1 * q2
#   numerator equals (p1 * q2) + (p2 * q1)
#   reduced equals reduceFraction(numerator,denominator)
#   return reduced
def add(p1, q1, p2, q2):
    denominator = q1 * q2
    numerator = (p1 * q2) + (p2 * q1)
    reduced = reduceFraction(numerator, denominator)
    return reduced


# Input: 4 integers p1, q1, p2 and q2 which represent the numerators and denominators in a fraction(p1/q1 and p2/q2)
# Output: Two integers p and q that represent the difference of (p1,q1) - (p2,q2)
# Pre-condition of input: Denominators do not already = 0
# Pseudo Code:
#   denominator equals q1 * q2
#   numerator equals (p1 * q2) - (p2 * q1)
#   reduced equals reduceFraction(numerator, denominator)
#   return reduced
def subtract(p1, q1, p2, q2):
    denominator = q1 * q2
    numerator = (p1 * q2) - (p2 * q1)
    reduced = reduceFraction(numerator, denominator)
    return reduced


# Input: 4 integers p1, q1, p2 and q2 which represent the numerators and denominators in a fraction(p1/q1 and p2/q2)
# Output: Two integers p and q that represent the product of (p1,q1) * (p2,q2)
# Pre-condition of input: Denominators do not already = 0
# Pseudo Code:
#   denominator equals q1 * q2
#   numerator equals p1 * p2
#   reduced equals reduceFraction(numerator,denominator)
#   return reduced
def multiply(p1, q1, p2, q2):
    denominator = q1 * q2
    numerator = p1 * p2
    reduced = reduceFraction(numerator, denominator)
    return reduced


# Input: 4 integers p1, q1, p2 and q2 which represent the numerators and denominators in a fraction(p1/q1 and p2/q2)
# Output: Two integers p and q that represent the quotient of (p1,q1) / (p2,q2)
# Pre-condition of input: Denominators do not already = 0
# Pseudo Code:
#   denominator equals q1 * p2
#   numerator equals q2 * p1
#   reduced equals reduceFraction(numerator,denominator)
#   return reduced
def divide(p1, q1, p2, q2):
    denominator = q1 * p2
    numerator = q2 * p1
    reduced = reduceFraction(numerator, denominator)
    return reduced


# Input: Two fractions represented by (p1/p2) and (q1/q2)
# Output: True if (p1/q1) = (p2/q2), and False if not
# Pre-condition of input: q1 and q2 are not equal to 0
# Pseudo Code:
#   reduce equals reduceFraction(p1,q1)
#   reduce2 equals reduceFraction(p2,q2)
#   if reduce is equal to reduce 2
#       return true
#   else
#       return false
def isEqual(p1, q1, p2, q2):
    reduce = reduceFraction(p1, q1)
    reduce2 = reduceFraction(p2, q2)
    if reduce == reduce2:
        return True
    else:
        return False


# Input: Two fractions represented by (p1/p2) and (q1/q2)
# Output: True if (p1/q1) < (p2/q2), and False if not
# Pre-condition of input: q1 and q2 are not equal to 0
# Pseudo Code:
#   if p1 * q2 < p2 * q1
#       return true
#   else
#       return false

def isLess(p1, q1, p2, q2):
    if p1 * q2 < p2 * q1:
        return True
    else:
        return False


# Input: Single fraction represented by (p/q) and n represents the n-th digit to be returned
# Output: n-th digit after the decimal point
# Pre-condition of input: n > 0, p >= q >= 0
# Pseudo Code:
#   remainder = p mod q
#   while loop
#       remainder = remainder * 10
#       digit = floor of remainder divided by q
#       remainder = remainder mod q
#   end of while loop
#   return digit
def digitOfFraction(p, q, n):
    remainder = p % q
    count = 0
    while count < n:
        remainder = remainder * 10
        digit = remainder // q
        remainder = remainder % q
        count = count + 1
    return digit


# Input: Two integers n and m
# Output: m-th digit in the decimal expansion of the fraction Hn
# Pre-condition of input: n and m are positive integers
# Pseudo Code:
#   sum = (0,1)
#   while loop
#       sum = add(sum[0],sum[1],1,count)
#   end of while loop
#   p = sum[0]
#   q = sum[1]
#   return digit_of_fraction(p,q,m)
def hsum(n, m):
    sum = (0, 1)
    count = 0
    while count < n:
        sum = add(sum[0], sum[1], 1, count + 1)
        count = count + 1
    p = sum[0]
    q = sum[1]
    return digitOfFraction(p, q, m)



# Problem 2.

# Input: Positive integer N and k
# Output: True if N is a likely prime number and False if N is definitely not
# Pre-condition of input: N is a positive integer
# Pseudo Code:
#   Loop for k times
#       randInt = random number between 1 and N - 1
#       if randInt to the power of (N-1) mod N does not equal 1
#           return false
#   return True
def primality2(N,k):
    for i in range(k):
        randInt = random.randint(1,N - 1)
        if (randInt ** (N - 1) % N) != 1:
            return False
    return True

# Input: Positive integer N and k
# Output: True if N is a likely prime number and False if N is definitely not
# Pre-condition of input: N is a positive integer
# Pseudo Code:
#   if N is divisible by 3,5,7 or 11
#       return false
#   else
#       return primality2(N,k)
def primality3(N,k):
    if ((N % 3 == 0) and (N != 3)) or ((N % 5 == 0) and (N != 5)) or ((N % 7 == 0) and (N != 7)) or ((N % 11 == 0) and (N != 11)):
        return False
    else:
        return primality2(N,k)

# Problem 3.
# Input: Positive integer N and k
# Output: A random prime number with N bits
# Pre-condition of input: N and k are both positive integers
# Pseudo Code:
#   generate n random numbers between 0 and 1 to store in binaryNum
#   add 1s at the start and end of binaryNum
#   Keep calling primality3 with binaryNum, and K until it returns true
#   return binaryNum
def primeNumGenerator(N,K):
    binaryNum = ''.join(random.choices('01', k = N - 2))
    newBinaryNum = '1' + binaryNum
    binaryNum = newBinaryNum + '1'
    decimal = int(binaryNum, 2)
    while not primality3(decimal, K):
        binaryNum = ''.join(random.choices('01', k = N -2))
        newBinaryNum = '1' + binaryNum
        binaryNum = newBinaryNum + '1'
        decimal = int(binaryNum, 2)
    return decimal

# Problem 4.
# Input: Positive integer N and K
# Output: p and q are both prime number with n bits, N is p * q, E is gcd(E,(p-1)(q-1)), and D where 2 <= D <= N - 1
# Pre-condition of input: N and K are both positive integers
# Pseudo code:
#   p = primeNumGenerator(N,K)
#   q = primeNumGenerator(N,K)
#   N = p * q
#   E = gcd(Random 10 bit integer, (p-1)(q-1)) until gcd() returns 1
#   D = egcd(E, (p-1)(q-1))
#   return p, q, N, E, D
def RSAGenerator(N,K):
    p = primeNumGenerator(N,K)
    q = primeNumGenerator(N,K)
    while p == q:
        q = primeNumGenerator(N, K)
    N = p * q
    ET = (p - 1) * (q - 1)

    Egen = ''.join(random.choices('01', k = 10))
    E = int(Egen,2)
    while gcd(E, ET) != 1:
        Egen = ''.join(random.choices('01', k = 10))
        E = int(Egen,2)
    if E > ET:
        eGCDResult = egcd(E, ET)
        D = eGCDResult[0]
        if D < 0:
            D = ET - abs(D)
    else:
        eGCDResult = egcd(ET, E)
        D = eGCDResult[1]
        if D < 0:
            D = ET - abs(D)
    return p, q, N, E, D

# Input: Two positive integers a and b with a >= b >= 0
# Output: Integers x,y,d, such that d = gcd(a,b) and ax + by = d
# Pre-condition of input: a and b are positive integers
# Pseudo code:
#   if b = 0: return (1,0,a)
#   (x,y,d) = egcd(b, a mod b)
#   return (y, x - [a/b] * y, d)
def egcd(a,b):
    if b == 0:
        return (1, 0, a)
    result = egcd(b, a % b)
    return (result[1], result[0] - a // b * result[1], result[2])

# Problem 5.
# Input: Three positive integers M, N, K
# Output: Encrypted version and decrypted version of M, p, q, N , E, and D where calculated from RSAGenerator(N, K)
# Pre-condition of input: N and K are both positive integers and M < N
# Pseudo code:
#   if M > N:
#       exit code and say M is bigger than N
#   RSAValues = RSAGenerator(N,K)
#   EncryptedMessage = modexp(M, E, N)
#   DecryptedMessage = modext(EncryptedMessage, D, N)
#   return RSAValues, M, EncryptedMessage, DecryptedMessage
def EncryptionDecryption(M, N, K):
    RSAValues = RSAGenerator(N, K)
    RSA_N = RSAValues[2]
    if M > RSA_N:
        print (M, " is larger than ", RSA_N)
        sys.exit(1)    
    E = RSAValues[3]
    D = RSAValues[4]
    EncryptedMessage = modexp(M, E, RSA_N)
    DecryptedMessage = modexp(EncryptedMessage, D, RSA_N)
    print("p: " + str(RSAValues[0]))
    print("q: " + str(RSAValues[1]))
    print("n: " + str(RSA_N))
    print("E: " + str(E))
    print("D: " + str(D))
    print("Plain-text message, m: " + str(M))
    print("Encrypted Message: " + str(EncryptedMessage))
    print("Decrypted Message: " + str(DecryptedMessage))
    if M == DecryptedMessage:
        print("Compare D and M result: yes")
    else:
        print("Compare D and M result: no")

# Input: Two n-bit integers x and N, an integer exponent y
# Output: x^y mod N
# Pre-condition of input: z, N and y are all positive integers
# Pseudo code:
#   if y = 0: return 1
#   z = modexp(x, [y/2], N)
#   if y is even:
#       return z^2 mod N
#   else:
#       return x * x^2 mod N
def modexp(x,y,N):
    if y == 0:
        return 1
    z = modexp(x, y // 2, N)
    if y % 2 == 0:
        return z ** 2 % N
    else:
        return x * z ** 2 % N

if __name__ == '__main__':
    choices = "CHOICES: \n1. Problem 1 \n2. Problem 2\n3. Problem 5\n4. Quit"
    print (choices)
    answer = input("Which one would like to test(1,2,3 or 4)?")
    while answer != "4":
        if answer == "1":
            print("PROBLEM 1: ")
            n = int(input("Please enter a positive integer, n: "))
            m = int(input("Please enter a positive integer, m: "))
            answer = hsum(n, m)
            print ("The " + str(m) + "-th digit in the decimal expansion of the fraction H(n) is: " + str(answer))
        elif answer == "2":
            print("PROBLEM 2: ")
            n = int(input("Please enter a positive integer, N: "))
            k = int(input("Please enter a positive integer, k: "))
            answer = primality3(n,k)
            if answer == True:
                print(str(n) + ", is likely a prime number")
            else:
                print(str(n) + ", is not a prime number")
        elif answer == "3":
            print("PROBLEM 5: ")
            m = int(input("Please enter a message integer, M: "))
            n = int(input("Please enter the number of bits for primes, n: "))
            k = int(input("Please enter the confidence parameter for primality3, k: "))
            EncryptionDecryption(m,n,k)
        else:
            print("Please enter 1,2,5 or quit")
        print(choices)
        answer = input("Which one would like to test(1,2,3 or 4)?")
    print("Exited")