result = 1

def factorial(n):
    if n <= 1:
        return 1
    result = n * factorial(n - 1)

    return result


n = int(input())

if __name__ == "__main__":
    print(factorial(n))
