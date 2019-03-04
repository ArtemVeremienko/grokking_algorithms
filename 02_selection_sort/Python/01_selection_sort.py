def find_Smallest(arr):
    smallest = arr[0] # Для хранения наименьшего значения
    smallest_index = 0 # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_Sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr) # находим наименьший элемент в массиве
        newArr.append(arr.pop(smallest)) # и добавляем его в новый массив
    return newArr

print(selection_Sort([-4, 5, 3, -2, 6, 2, 10, -1]))