import random
import numpy as np
from baseclass import BaseClass


class Product(BaseClass):
    def __init__(self, id, d, vec=None, score_list=None):
        self.id  = id
        self.d   = d
        self.vec = np.array(vec) if vec is not None else self.init_vec(d, self.generate_random_value)
        self.score_list = score_list if score_list is not None else []
        self.reverse_rank = []


    def generate_random_value(self):
        return random.randint(0, 10)


    def export_json_format(self):
        return {
            "id": self.id,
            "d": self.d,
            "vec": self.vec.tolist(),
            "score_list": self.score_list,
            "reverse_rank": self.reverse_rank
        }
