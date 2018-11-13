import click
import numpy as np
from datetime import datetime
from baseclass import BaseClass
from user import User
from product import Product
from file_manager import import_json, export_json_list


def user_factory(id, d, vec=None):
    return User(id, d, vec)


def product_factory(id, d, vec=None, score_list=None):
    return Product(id, d, vec, score_list)


def complete_filename(prefix, file_name_main, extension):
    return f"{prefix}_{file_name_main}.{extension}"


def get_factory(name):
    factories = {
        "user": user_factory,
        "product": product_factory
    }

    return factories[name]


def generate_list(num, d, factory_cb):
    result = []
    for i in range(num):
        result.append(factory_cb(i, d))

    return result


def import_json_list(file_name, factory):
    json_data_list = import_json(f"./data/{file_name}")
    data_list = []

    for json_data in json_data_list:
        list_item = factory(json_data["id"], json_data["d"], json_data["vec"])
        data_list.append(list_item)

    return data_list


def build_list(n, d, name, filename):
    factory = get_factory(name)

    if filename is None:
        return generate_list(n, d, factory)
    else:
        return import_json_list(f"{name}_{filename}.json", factory)


def export_result(user_list, product_list):
    export_json_list(user_list, 'user')
    export_json_list(product_list, 'product')


def calculate_score(user_list, product_list):
    for p in product_list:
        for u in user_list:
            score = np.dot(p.vec, u.vec)
            p.score_list.append({"id": u.id, "score": score})


def get_reverse_rank(product):
    return sorted(product.score_list, key=lambda x: -x["score"])


@click.command()
@click.option('--user_num', '-un', default=100)
@click.option('--product_num', '-pn', default=100)
@click.option('--dimension', '-d', default=100)
@click.option('--product_id', '-p', default=0)
@click.option('--k', '-k')
@click.option('--filename', '-fn')
def main(user_num, product_num, dimension, product_id, k, filename):
    user_list = build_list(user_num, dimension, 'user', filename)
    product_list = build_list(product_num, dimension, 'product', filename)

    calculate_score(user_list, product_list)

    reverse_rank = get_reverse_rank(product_list[product_id])

    print(reverse_rank)

    if filename is None:
        export_result(user_list, product_list)


if __name__ == '__main__':
    main()

