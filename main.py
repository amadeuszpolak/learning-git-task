shop_dict = {'piekarnia': ['chleb', 'pączek', 'bułki'], 'warzywniak': ['marchew', 'seler', 'rukola']}
product_counter = 0
for shop in shop_dict:
    temp_list = [each_string.capitalize() for each_string in shop_dict[shop]]
    print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {temp_list}")
    product_counter += len(shop_dict[shop])
print(f"W sumie kupuje {product_counter} produktów")
print("Warzywniak Zamknięty")
print("Piekarnia Zamknięta")
print("Special Greetings for my Mentor! :)")