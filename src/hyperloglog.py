# HyperLogLog - вероятностная структура данных для подсчёта количества уникальных элементов
class HyperLogLog:

    def __init__(self, size):  # size=32
        self.buckets = [0] * size

    def fill_buckets(self, item):
        bin_hash = self.hash_value(item, length=32)
        buckets_index = int(str(bin_hash[:5]),
                            10)  # берём первые 5 элементов хэша и переводим её в десятичное счисление
        total_zeros = self.count_zeros(bin_hash)

        if total_zeros > self.buckets[buckets_index]:  # если количество нулей с конца больше,
            # чем то, что лежит в бакете по индексу, полученному от перевода части хэша в дестичную систему
            self.buckets[buckets_index] = total_zeros  # заполняем бакет по индексу

        return self.buckets

    # получаем хэш в бинарном виде заданной длины при помощи ASCII кодов
    @classmethod
    def hash_value(cls, item, length):
        hashed = 0

        for i, s in enumerate(item):
            encoded = (i + 1) * ord(s)
            hashed += encoded

        max_number = 2 ** length - 1
        hashed = hashed % max_number

        bin_hash = bin(hashed)[2:]
        bin_hash = '0' * (length - len(bin_hash)) + bin_hash

        return bin_hash

    # считаем количество нулей в хэшэ с конца до тех пор, пока не встретится единица
    @classmethod
    def count_zeros(cls, bin_hash):
        total_zeros = 0

        for i in range(len(bin_hash) - 1, -1, -1):
            if bin_hash[i] == 0:
                total_zeros += 1
            else:
                break

        return total_zeros

    # считаем количество уникальных элементов - гармоническое среднее с поправкой на смещение
    @staticmethod
    def get_cardinality(buckets_filled):
        bias = 0.7942
        amount = 0

        for value in buckets_filled:
            amount += 1 / 2 ** -value

        cardinality = bias * len(buckets_filled) * (len(buckets_filled) / amount)

        return cardinality
