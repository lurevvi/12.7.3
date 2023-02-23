entered_array = input("Введите числа, через пробел: ").split()
array = [int(i) for i in entered_array]
print("Введены следующие числа: ", array)

while True:
    try:
        element = int(input("Введите целое число от 1 до 99: "))
        if element < 0 or element > 99:
            raise Exception
        break
    except ValueError:
        print("Введите число цифрами")
    except Exception:
        print("Введенное число выходит за пределы заданного диапазона")

array.append(element)

count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1
    array[idx] = x

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if element == array[middle + 1]:
        return middle
    elif element < array[middle + 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

a = array.index(element)
b_search = binary_search(array, element, 0, len(array))

print("Список после сортировки и дополнения: ", array)
print("Номер позиции добавленного в список элемента: ID = ", a)

if b_search > 0:
    print("Ответ: № элемента, который меньше введенного числа: ID = ",
          binary_search(array, element, 0, len(array)))
else:
    print("Перед введенным числом элементы в списке отсутствуют!")