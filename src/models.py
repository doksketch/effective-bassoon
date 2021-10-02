import numpy as np
import pandas as pd
import faiss


# добавить перед фаиссом эмбеддинги из свд, описать как всё работает
class ItemSimilarity:

    def __init__(self, data, C: str):
        self.item_user = self._prepare_matrix(data, C)
        self.index = self._fit(self.item_user)

    @staticmethod
    def _prepare_matrix(data, C):
        item_user = pd.pivot_table(data,
                                   index='resp_seat_bid_bid_ad_id', columns='req_user_id',
                                   values=C,
                                   aggfunc=np.sum,
                                   fill_value=0)

        item_user = item_user.values.astype(np.float32)
        item_user = item_user.copy(order='C')

        return item_user

    @staticmethod
    def _fit(item_user):
        metric = faiss.METRIC_L2

        index = faiss.index_factory(item_user.shape[1], 'IVF2,Flat', metric)
        index.train(item_user)
        index.add(item_user)

        return index

    def get_similar_items(self, K):
        return self.index.search(self.item_user, K)[1]
