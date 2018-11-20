import random
import click
import time
import numpy as np
from file_manager import import_json, export_json_list


class S():
    def __init__(self, d, beta):
        self.d = d
        self.beta = beta
        self.vec_value_total = beta
        self.vec = self.init_vec(d)


    def init_vec(self, d):
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


def create_s(d, beta):
    s = S(d, beta)
    return s


def import_user_list(path):
    user_list = import_json(f"./data/user_{path}.json")
    return user_list


def import_product(path, product_id):
    product_list = import_json(f"./data/product_{path}.json")
    return list(filter(lambda p: p["id"] == product_id, product_list))[0]


def calculate_score(user_list, improved_vec):
    score_list = []
    for u in user_list:
        score = np.dot(improved_vec, u["vec"])
        score_list.append(score)

    return score_list


def improvement(p, s):
    improved_vec = []
    for i in range(len(p["vec"])):
        v = p["vec"][i]
        improved_vec.append(v + s.vec[i])

    return improved_vec


def top_k(vec, k):
    count = 0
    for v in vec:
        if v > k:
            count += 1

    return count

@click.command()
@click.option('--product_id', '-p', default=0)
@click.option('--file_name', '-fn')
@click.option('--beta', '-b', default=10)
@click.option('--k', '-k', default=5)
def main(product_id, file_name, beta, k):
    product = import_product(file_name, product_id)
    user_list = import_user_list(file_name)
    d = product["d"]

    result_list = []
    for i in range(10):
        s = create_s(d, beta)
        improved_vec = improvement(product, s)
        score_list = calculate_score(user_list, improved_vec)
        rr = sorted(score_list, key=lambda x: -x)
        top_k_count = top_k(score_list, k)
        result = {
            "score_list": score_list,
            "top_k_count": top_k_count,
            "s": s
        }
        result_list.append(result)

    sorted_result_list = sorted(result_list, key=lambda x: -x["top_k_count"])
    print(sorted_result_list[0]["s"].vec)

if __name__ == '__main__':
    main()
