# Higher-order function: select_items
def select_items(items, condition):
    """
    items: Liste
    condition: Bir koşulu kontrol eden bir fonksiyon
    """
    # Filter fonksiyonu, bir koşula uyan tüm öğeleri döndürür
    selected_items = filter(condition, items)
    return list(selected_items)

# Higher-order function: create_item_selector
def create_item_selector(item_list):
    def item_selector(item):
        return item.lower() in item_list
    return item_selector

# Örnek bir liste
grocery_items = ['apple', 'banana', 'carrot', 'potato', 'orange', 'grape', 'broccoli', 'spinach', 'kiwi', 'cucumber']

# Meyveleri seçme
fruits_selector = create_item_selector(['apple', 'banana', 'orange', 'grape', 'kiwi'])
fruits = select_items(grocery_items, fruits_selector)
print("Fruits:", fruits)

# Sebzeleri seçme
vegetables_selector = create_item_selector(['carrot', 'potato', 'broccoli', 'spinach', 'cucumber'])
vegetables = select_items(grocery_items, vegetables_selector)
print("Vegetables:", vegetables)
