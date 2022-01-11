t = int(input())

arr = []
for _ in range(t):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')
    print()

if __name__ == "__main__":
    pass
