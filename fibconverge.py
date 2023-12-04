# fib frac to compute convergence of ratio
# (Continued fraction)
def frac(n,k):
    #print(n,k)
    # This needs computed until a base case is reached
    if n-(k+1) == 1:
        return 1/1  # f1/f2
    
    return 1/(1+frac(n,k+1))
    
def start(n):
    return 1/(2+frac(n, 2))

print('fib convergence')
for i in range(5,200):
    print(i, start(i))

# Continued fraction 1/1+(R) -- interestingly sums to 1-phi
# Well, if you start with 1 + ... then you do get phi.
def frac2(n):
    if n == 1:
        return 1
    
    return 1/(1+frac2(n-1))

# Very close to the golden ratio..
print('1-phi convergence')
for i in range(1,200):
    print(i, frac2(i))

def even(n):
    '''
    A demonstration (if accuracy was better) of generating just the even fib
    numbers using the fib ratio for progressing.
    '''
    phi = 1.6180339887498948

    # Pick the two odd number directly before an even (starting with even number F_40)
    # Before F_40 accuracy is very poor -- namely because the starting points are _not_
    # accurately predicted with this approach.
    # Reduces iterations by 2/3s -- 1 out of every 3 numbers is odd.
    first = 102334155
    second = 165580141

    results = []

    while n > 0:
        print(first, second)
        even = int(first+second)
        results.append(even)
        first = int(second*(1+phi))
        second = int(even*(1+phi))
        n -= 1

    return results


print(even(10))