def is_prime(n):
    # Prime number is greater than 1 and divisible only by 1 and itself
    if n <= 1:
        return False

    # Check divisors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True  # Return True if no divisors are found

# Test the function
n = int(input("What is your number? "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
