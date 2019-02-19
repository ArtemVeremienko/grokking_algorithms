def binary_search(list, item): # В переменных low high хранятся границы
    low = 0                    # той части списка, в которой выполняется поиск
    high = len(list) - 1

    while low <= high:          # Пока эта часть не сократиться до одного элемента...
        mid = (low + high) // 2 # ...проверяем средний элемент
        guess = list[mid]
        if guess == item:       # Значение найдено
            return mid
        elif guess > item:      # много
            high = mid -1
        else:                   # Мало
            low = mid + 1
    return None                 # Значение не существует

my_list = [1, 3, 5, 7, 9]       # массив для тестирования функции

print(binary_search(my_list, 3)) # 1 (нумерация элементов начинается с 0)
print(binary_search(my_list, -1)) # None (такого элемента нет в нашем списке)
