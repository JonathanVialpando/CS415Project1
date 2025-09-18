# Project 1
# Jonathan Vialpando and Arturo Nunez Gomez

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

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def add(p1, q1, p2, q2)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def subtract(p1, q1, p2, q2)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def multiply(p1, q1, p2, q2)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def divide(p1, q1, p2, q2)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def isEqual(p1, q1, p2, q2):

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
# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def digitOfFraction(p, q, n)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def hsum(n ,m)





if __name__ == '__main__':
    print("gcd")
    reduced = reduceFraction(14,32)
    print (reduced)
    is_less = isLess(3,4,1,2)
    print (is_less)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
