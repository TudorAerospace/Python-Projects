import json

class InventoryManager:
    def __init__(self):
        file_path = r'C:\Users\Tudor\Desktop\Python\inventory.json'
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.inventory = data
        print(self.inventory)
    def add_product(name, description, price, quantity):
        file_path = r'C:\Users\Tudor\Desktop\Python\inventory.json'
