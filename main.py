import click
import numpy as np
from baseclass import BaseClass
from user import User
from product import Product


def user_factory(id, d):
    return User(id, d)


def product_factory(id, d):
    return Product(id, d)


def generate_list(num, d, factory_cb):
    result = []
    for i in range(num):
        result.append(factory_cb(i, d))

    return result


def build_list(n, d, factory, file_name):
    if file_name is None:
        return generate_list(n, d, factory)
    else:
        return import_list(file_name)


def calculate_score(user_list, product_list):
    for p in product_list:
        for u in user_list:
            score = np.dot(p.vec, u.vec)
            p.score_list.append({"id": u.id, "score": score})


def get_reverse_rank(product):
    return sorted(product.score_list, key=lambda x: x["score"])


@click.command()
@click.option('--user_num', '-u_n', default=100)
@click.option('--product_num', '-p_n', default=100)
@click.option('--dimension', '-d', default=100)
@click.option('--product_id', '-p', default=0)
@click.option('--k', '-k')
@click.option('--file_name', '-fn')
def main(user_num, product_num, dimension, product_id, k, file_name):
    user_list = build_list(user_num, dimension, user_factory, file_name)
    product_list = build_list(product_num, dimension, product_factory, file_name)

    calculate_score(user_list, product_list)

    reverse_rank = get_reverse_rank(product_list[product_id])

    print(reverse_rank)


main()

