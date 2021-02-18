def SumSquares(n):
    s=0
    for i in range(0,n):
        s+=i**2
    return s
def SumSquaresTwo(n):
    return sum(i**2 for i in range (0,n))
def SumSquaresOdd(n):
    s = 0
    for i in range(0, n):
        if(i%2==1):
            s += i ** 2
    return s
def SumSquaresOddTwo(n):
    return sum(i**2 for i in range(0,n) if i%2==1)
