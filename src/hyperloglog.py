from sklearn.utils import murmurhash3_32

print(murmurhash3_32(b'khbjhvjh'))
data = ['kjvjkhvt87kjbkjbklhg', 'lhvjh', 'hgchgchjgc', 'ljhvhjghv', 'mgvmjv']
buckets = [0] * 32


class HyperLogLog:

    def __init__(self, size):  # size=32
        self.buckets = [0] * size

    def fill_buckets(self, item):
        hashed = self.hash_value(item)
        print(hashed)
        buckets_index = int(hashed[3:7])  # берём первые 4 элемента хэша и переводим её в десятичное счисление
        print(buckets_index)
        total_zeros = self.count_zeros(hashed)

        if total_zeros > self.buckets[buckets_index]: # если количество нулей с конца больше,
            # чем то, что лежит в бакете по индексу, полученному от перевода части хэша в дестичную систему
            self.buckets[buckets_index] = total_zeros # заполняем бакет по индексу

        return self

    # получаем хэш в бинарном виде
    @classmethod
    def hash_value(cls, item):
        hashed = bin(int(item.hexdigest(), 16))
        return hashed

    # считаем количество нулей в хэшэ с конца до тех пор, пока не встретится единица
    @classmethod
    def count_zeros(cls, hashed):
        total_zeros = 0

        for i in range(len(hashed), -1, -1):
            if i == 0:
                total_zeros += 1
            else:
                total_zeros = 0
                break

        return total_zeros

    # считаем количество уникальных элементов - гармоническое среднее с поправкой на смещение
    @staticmethod
    def get_cardinality(buckets):
        bias = 0.7942
        amount = 0

        for value in buckets:
            amount += 1 / 2 ** -value

        cardinality = bias * len(buckets) * (len(buckets) / amount)

        return cardinality
