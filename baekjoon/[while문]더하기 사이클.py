ab = int(input())
B = ab % 10
cnt = 0
result = ab

while True:
    tmp = int(result / 10) + result % 10
    result = B * 10 + tmp % 10
    B = tmp % 10
    cnt += 1
    if result == ab:
        break

print(cnt)

if __name__ == "__main__":
    pass
