if __name__ == "__main__":
    N = int(input())
    add = 0
    new_num = N
    count = 0

    while 1:
        add = new_num // 10 + new_num % 10
        new_num = new_num % 10 * 10 + add % 10
        count += 1
        if new_num == N:
            print(count)
            break
