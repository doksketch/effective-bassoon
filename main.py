from src.hyperloglog import HyperLogLog
from src.priority_queue import PriorityHeap
from src.count_min_sketch import CountMinSketch


def main():
    data = []

    # узнаём top_k - берём 30 процентов от общего количества уникальных элементов
    buckets = HyperLogLog(size=32)
    for item in data:
        buckets = buckets.fill_buckets(item)
    top_k = int(buckets.get_cardinality(buckets)) * 0.3

    # считаем сам топ
    cms = CountMinSketch(top_k=top_k)
    heap = PriorityHeap()  # объявляем кучу для взятия топа

    for i in range(len(data)):
        # key = data[random.randint(0, random.randint(0, len(data) - 1))]
        cms.increment_value(key=data[i])
        print(cms.get_minimum(0))
        print(cms.get_minimum(1))
        print(cms.get_minimum(2))
        print(cms.get_minimum(3))
        print(cms.get_minimum(4))
        print(cms.get_minimum(5))

    heap.push(cms.get_minimum(5))  # вот тут немного не ясно, как доавлять в кучу из скетча
    top_elements = heap.get_top_k(k=top_k)

    return top_elements


if __name__ == '__main__':
    main()
