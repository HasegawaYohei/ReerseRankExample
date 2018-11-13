import random
import numpy as np
from baseclass import BaseClass

class User(BaseClass):
    def __init__(self, id, d, vec=None):
        self.id  = id
        self.d   = d
        self.vec_value_total = 1
        self.vec = np.array(vec) if vec is not None else self.init_vec(d, self.generate_random_value)


    def init_vec(self, d, cb):
        arr = []
        for i in range(d):
            if i == (d - 1):
                arr.append(self.vec_value_total)
            else:
                arr.append(self.generate_random_value())

        return np.array(arr)


    def generate_random_value(self):
        v = random.uniform(0, self.vec_value_total)
        self.vec_value_total -= v
        return v


    def export_json_format(self):
        return {
            "id": self.id,
            "d": self.d,
            "vec": self.vec.tolist()
        }



