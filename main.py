# Project 1
# Jonathan Vialpando and Arturo Nunez Gomez

# Problem 1.

# Input: Two integers p and q with p >= q >= 0
# Output: gcd(p,q)
# Pre-condition of input: p >= q >= 0
# Pseudo Code:
#   if q is equal to 0
#       return p
#   else
#       return gcd (q, p mod q)
def gcd(p,q):
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
def reduceFraction(p,q):
    newGcd = gcd(p,q)
    newP =  p // newGcd
    newQ = q // newGcd
    return newP,newQ

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
    reduced = reduceFraction(numerator,denominator)
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
    reduced = reduceFraction(numerator,denominator)
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
    reduced = reduceFraction(numerator,denominator)
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
    reduce = reduceFraction(p1,q1)
    reduce2 = reduceFraction(p2,q2)
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
#   for loop with n reducing by 1
#   remainder = remainder * 10
#   digit = floor of remainder divided by q
#   remainder = remainder mod q
#   end of for loop
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

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def hsum(n ,m)





if __name__ == '__main__':
    print("gcd")
    added = add(1,2,1,3)
    print(added)
    subed = subtract(1,2,1,3)
    print(subed)
    mult = multiply(1,2,1,3)
    print(mult)
    div = divide(1, 2, 1, 3)
    print(div)
    n_thDigit = digitOfFraction(1,7,6)
    print(n_thDigit)