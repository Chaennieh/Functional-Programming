# Functional programming example: Fruits and Vegetables

# Verilen bir liste üzerinde bir koşula göre seçim yapacak olan fonksiyon
def select_items(items, condition):
    """
    items: Liste
    condition: Bir koşulu kontrol eden bir fonksiyon
    """
    # Filter fonksiyonu, bir koşula uyan tüm öğeleri döndürür
    selected_items = filter(condition, items)
    return list(selected_items)

# Örnek bir koşul fonksiyonu: Meyveleri seçer
def is_fruit(item):
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    return item.lower() in fruits

# Örnek bir koşul fonksiyonu: Sebzeleri seçer
def is_vegetable(item):
    vegetables = ['carrot', 'potato', 'broccoli', 'spinach', 'cucumber']
    return item.lower() in vegetables

# Örnek bir liste
grocery_items = ['apple', 'banana', 'carrot', 'potato', 'orange', 'grape', 'broccoli', 'spinach', 'kiwi', 'cucumber']

# Meyveleri seçme
fruits = select_items(grocery_items, is_fruit)
print("Fruits:", fruits)

# Sebzeleri seçme
vegetables = select_items(grocery_items, is_vegetable)
print("Vegetables:", vegetables)
