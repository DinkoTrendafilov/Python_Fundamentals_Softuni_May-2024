class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item_name):
        if len(self.items) >= self.__capacity:
            return "not enough room in the inventory"

        self.items.append(item_name)

    def get_capacity(self):
        return self.__capacity

    def __get_items_count(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.get_capacity() - self.__get_items_count()}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)



