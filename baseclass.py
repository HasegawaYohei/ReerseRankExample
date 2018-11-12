import numpy as np

class BaseClass:
    def __init__(self, id, d):
        self.id = id
        self.id = d
        self.vec = []

    def init_vec(self, d, cb):
        arr = []
        for i in range(d):
            arr.append(cb())

        return np.array(arr)
