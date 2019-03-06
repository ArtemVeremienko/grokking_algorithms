def quick_sort(array):
    if len(array) < 2:
        return array # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    else: # Рекурсивный случай
        pivot = array[0] # Опорный элемент
        less = [i for i in array[1:] if i <= pivot] # подмассив всех элементов меньших опорного
        greater = [i for i in array[1:] if i > pivot] # подмассив всех элементов больших опорного
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2, 3, 0, 15, -1])) 