import requests

def get_categories():
    url = 'https://fakestoreapi.com/products/categories'
    response = requests.get(url)
    if response.status_code == 200:
        categories = response.json()
        return categories
    else:
        print("Failed to retrieve categories")
        return []

def get_products_by_category(category):
    url = f'https://fakestoreapi.com/products/category/{category}'
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        print(f"Products in category '{category}':")
        for product in products:
            print(f"- {product['title']}: ${product['price']}")
    else:
        print(f"Failed to retrieve products for category '{category}'")

def main():
    categories = get_categories()
    if categories:
        print("Available categories:")
        for category in categories:
            print(f"- {category}")
        selected_category = input("Enter the category you want to view products for: ")
        get_products_by_category(selected_category)

if __name__ == "__main__":
    main()