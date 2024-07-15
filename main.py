import csv
import matplotlib.pyplot as plt
from itertools import groupby

def read_sales_data(file_path):
    '''Принимает путь к файлу csv и возвращает список продаж'''
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        return list(reader)

def total_sales_per_product(sales_data):
    '''Принимает список продаж и возвращает словарь, где ключ - название продукта,
    а значение - общая сумма продаж этого продукта.'''
    sales_data = sales_data.copy()
    result_di = {}
    k = lambda x: x['product_name']
    sales_data.sort(key=k)
    for k, g in groupby(sales_data, key=k):
        result_di[k] = sum(map(lambda x: int(x['price'])*int(x['quantity']), g))
    return result_di

def sales_over_time(sales_data):
    '''Принимает список продаж и возвращает словарь, где ключ - дата,
    а значение общая сумма продаж за эту дату.'''
    sales_data = sales_data.copy()
    result_di = {}
    k = lambda x: x['date']
    sales_data.sort(key=k)
    for k, g in groupby(sales_data, key=k):
        result_di[k] = sum(map(lambda x: int(x['price'])*int(x['quantity']), g))
    return result_di

# main >>
# получение списка продаж
sales_data = read_sales_data('input_data.csv')

# выводим продукт, который принес наибольшую выручку
products = total_sales_per_product(sales_data)
max_product = max(products, key=products.get, default=None)
print(f'Наибольшую выручку принёс продукт: "{max_product}"')

# выводит день, когда была наибольшая сумма продаж
dates = sales_over_time(sales_data)
max_date = max(dates, key=dates.get, default=None)
print(f'Наибольшая сумма продаж была: "{max_date}"')

# график общей суммы продаж по каждому продукту
plt.bar(products.keys(), products.values())
plt.xlabel('Продукт')
plt.ylabel('Сумма')
plt.title('Сумма продаж по продуктам')
plt.xticks(rotation=65)
plt.show()

# график общей суммы продаж по дням
plt.plot(dates.keys(), dates.values())
plt.xlabel('Дата')
plt.ylabel('Сумма')
plt.title('Сумма продаж по дням')
plt.xticks(rotation=65)
plt.show()