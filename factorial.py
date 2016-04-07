# Factorial
# Write a recursive and iterative solution for a finding the factorial of a number. 
# If you don't remember, the factorial of a non-negative integer n, denoted n! is the 
# product of all positive integers less than . For example, 5! = 5 * 4 * 3 * 2 * 1 

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print fact(5)

# Write a recursive function to compute the factorial of a number.
def fact_rec(n):
    if not n:
        return None
    if n == 1:
        return 1
    return fact_rec(n-1)*n 

print fact_rec(5)



