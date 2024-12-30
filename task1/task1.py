def circular_array_path(n, m):
    circular_array = [i for i in range(1, n + 1)]
    current_index = 0
    path = []

    while True:
        path.append(circular_array[current_index])
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            break

    print("".join(map(str, path)))


n = int(input("Введите n: "))
m = int(input("Введите m: "))
circular_array_path(n, m)
