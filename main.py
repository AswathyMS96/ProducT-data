import requests

response = requests.get("https://fakestoreapi.com/products?limit=5")
products = response.json()

highest_rated_product = max(products, key=lambda product: product['rating']['rate'])

print("Product with the highest rating:")
print(f"Title: {highest_rated_product['title']}")
print(f"Rating: {highest_rated_product['rating']['rate']}")
print(f"Rating Count: {highest_rated_product['rating']['count']}")
print(f"Price: {highest_rated_product['price']}")
print(f"Description: {highest_rated_product['description']}")
print(f"Category: {highest_rated_product['category']}")
print(f"Image: {highest_rated_product['image']}")
