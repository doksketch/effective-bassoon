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


if __name__ == '__main__':
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