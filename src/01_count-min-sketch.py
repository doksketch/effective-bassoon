# Count-Min Sketch - вероятностная структура данных для быстрого примерного подсчёта частоты встречаемости элементов
import random
from collections import Counter


class CountMinSketch:

    def __init__(self, top_k):
        self.total_hashes = top_k
        self.min_sketch = [[0] * self.total_hashes ** 2] * self.total_hashes

    def get_hash(self, key):
        return [hash(key)
                for _ in range(self.total_hashes)]

    def increment_value(self, key):
        for i, hash_value in enumerate(self.get_hash(key)):
            self.min_sketch[i][hash_value] += 1
        return self

    def get_minimum(self, key):
        minimum = min([self.min_sketch[i][hash_value] for i, hash_value in enumerate(self.get_hash(key))])
        key_min = key, minimum
        return key_min

    def crc_hash(self, polynomial):
        pass


# polynomial=x ** 4 + x ** 3 + 1
# получение хэша - представление элемента как результата деления двоичного представления элемента на двоичное
# представление полинома
def crc_hash(item, polynomial):
    table = dict(zip([str(i) for i in range(2)], [j for j in range(2)]))  # таблица соотвествий строки целому числу
    polynomial = str(polynomial)  # чтобы итерироваться
    item = str(item) + '0000'
    # item = ' '.join(format(ord(i), 'b') for i in item) + '0000'
    # получаем двоичное представление элемента. Добавлено 4 нуля - старшая степень многочлена

    # проводим побитовое деление - исключающее или слева направо
    count = len(polynomial)
    result = item[0: count]  # итоговый результат

    while count <= len(item):
        res = str()  # промежуточные значения деления

        for n in range(len(result)):  # нужно продолжать делить до тех пор, пока не получим количество чисел,
            # на одну степень больше, чем степень старшего многочлена
            ones = 0

            n1 = table.get(result[n])  # получаем целые числа в таблице соответствий
            n2 = table.get(polynomial[n])
            spam = n1 ^ n2  # побитовое исключающее или

            if spam == 1 and ones == 0:
                ones += 1
            elif (spam == 0 or spam == 1) and ones != 0:  # до первой полученной единицы на нули не обращаем внимания
                res += str(spam)

        balance = len(polynomial) - len(res)
        # смещаемся на столько, сколько элементов добавили на одной суб-итерации деления
        if len(res) < len(polynomial):  # нужно, чтобы промежуточный результат был равен  длине полинома
            res += item[count + 1:count + balance + 1]

        result = item[count + 1:count + balance + 1]
        count += balance

    return result


if __name__ == '__main__':
    # print(crc_hash(item=10011101, polynomial=11001))
    data = [random.randint(0, 5) for i in range(100)]
    print(Counter(data))
    cms = CountMinSketch(top_k=3)

    for i in range(len(data)):
        # key = data[random.randint(0, random.randint(0, len(data) - 1))]
        cms.increment_value(key=data[i])
        print(cms.get_minimum(0))
        print(cms.get_minimum(1))
        print(cms.get_minimum(2))
        print(cms.get_minimum(3))
        print(cms.get_minimum(4))
        print(cms.get_minimum(5))
    # for value in data:
    # print(value, cms.get_minimum(key=value))
