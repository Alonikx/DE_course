
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(i['price'] * i['quantity'] for i in purchases) 

def items_by_category(purchases):
    new_dict = {}
    for purchase in purchases:
        category = purchase['category']
        item = purchase['item']
        
        if category not in new_dict:
            new_dict[category] = []
        new_dict[category].append(item)
    return new_dict

def expensive_purchases(purchases, min_price):
    return [i for i in purchases if i['price']>=min_price]

def average_price_by_category(purchases):
    new_dict = {}
    for purchase in purchases:
        category = purchase['category']
        price = purchase['price']
        
        if category not in new_dict:
            new_dict[category] = []
        new_dict[category].append(price)
    return {i:sum(j)/len(j) for i,j in new_dict.items()}

def most_frequent_category(purchases):
    return max(purchases, key=lambda x: x['quantity'])['category']

print('Общая выручка:', total_revenue(purchases))
print('Товары по категориям:',items_by_category(purchases))
print('Покупки дороже 1.0:',expensive_purchases(purchases, 1.0))
print('Средняя цена по категориям:', average_price_by_category(purchases))
print('Категория с наибольшим количеством проданных товаров:',most_frequent_category(purchases))
