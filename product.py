import random
import numpy as np
from baseclass import BaseClass


class Product(BaseClass):
    def __init__(self, id, d):
        self.id = id
        self.vec = self.init_vec(d, self.generate_random_value)
        self.score_list = []


    def generate_random_value(self):
        return random.randint(0, 10)
