#How do you print a Fibonacci sequence using recursion?

def fibonacci_recursive(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    
n_terms = 10
sequence = [fibonacci_recursive(i) for i in range(n_terms)]

print("Fibonacci sequence:", sequence)