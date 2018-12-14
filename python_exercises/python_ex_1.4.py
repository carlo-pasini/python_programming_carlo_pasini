#script to evaluate a Bernstain basis polynomial
def factorial(n): #define a fubnction that returns the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) #the function is able to call itsel

def binomial_coeff(n,k): #define the binomial coefficient
    return factorial(n) / (factorial(k) * factorial(n-k))

def Bernstein_basis(i,n,t):
    result = binomial_coeff(n,i) * math.pow(t,i) * math.pow((1-t),(n-i))
    return result
