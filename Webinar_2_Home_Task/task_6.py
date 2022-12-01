'''Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список значений-
характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}'''

from pprint import pprint


def create_goods_list():
    goods_list = []
    vendor_code = 0
    while True:
        if input('Would you like add product parameters? Enter y/n: ') == 'y':
            features = input('Enter the features of product '
                             'separated by a space: ').split()
        else:
            print('Good buy!')
            break
        while input('Would you like add product? Enter y/n: ') == 'y':
            values = input('Enter the value of features '
                           'separated by a space: ').split()
            feature_dic = dict(zip(features, values))
            vendor_code += 1
            goods_list.append(tuple([vendor_code, feature_dic]))
        return goods_list


result = create_goods_list()
pprint(f'Goods list is\n {result}')


def goods_analytics(goods_list):
    analytics = {}
    for value in goods_list:
        for feature_key, feature_value in value[1].items():
            if feature_key in analytics:
                analytics[feature_key].append(feature_value)
            else:
                analytics[feature_key] = [feature_value]
    pprint(f'Analytic of goods\n {analytics}')


goods_analytics(result)
