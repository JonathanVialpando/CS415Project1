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

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def reduceFraction(p,q)

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
#def isEqual(p1, q1, p2, q2)

# Input:
# Output:
# Pre-condition of input:
# Pseudo Code:
#def isLess(p1, q1, p2, q2)

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
    gcd = gcd(1035,759)
    print(gcd)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
