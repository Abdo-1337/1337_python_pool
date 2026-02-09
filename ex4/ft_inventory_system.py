inventory_data = {

                    "players": {

                        "alice": {
                            "items": {
                                "sword": {
                                    "quantity": 1,
                                    "type": "weapon",
                                    "rarity": "rare",
                                    "value": 500,
                                },
                                "potion": {
                                    "quantity": 5,
                                    "type": "consumable",
                                    "rarity": "common",
                                    "value": 50,
                                },
                                "shield": {
                                    "quantity": 1,
                                    "type": "armor",
                                    "rarity": "uncommon",
                                    "value": 200,
                                },
                            }
                        },

                        "bob": {
                            "items": {
                                "potion": {
                                    "quantity": 0,
                                    "type": "consumable",
                                    "rarity": "common",
                                    "value": 50,
                                }
                            }
                        },
                    },

                    "catalog": {
                        "sword": {
                            "type": "weapon",
                            "rarity": "rare",
                            "value": 500,
                        },
                        "potion": {
                            "type": "consumable",
                            "rarity": "common",
                            "value": 50,
                        },
                        "shield": {
                            "type": "armor",
                            "rarity": "uncommon",
                            "value": 200,
                        },
                        "magic_ring": {
                            "type": "accessory",
                            "rarity": "rare",
                            "value": 800,
                        },
                    }
                }


def ft_inventory_system():
    """
    Manages and analyzes a player's inventory using nested dictionaries.

    - Displays a player's inventory with details
                (type, rarity, quantity, value).
    - Calculates total inventory value and total item count.
    - Groups items by category.
    - Simulates a transaction between players by updating item quantities.
    - Produces simple inventory analytics such as most valuable player,
      total items owned, and rare items from the catalog.
    """
    print("=== Player Inventory System ===\n")

    print("=== Alice's Inventory ===")
    items = inventory_data["players"]["alice"]["items"]
    items_count = 0
    inventory_value = 0
    for key, value in items.items():
        print(f"{key} ({value.get('type')}, {value.get('rarity')}): "
              f"{value.get('quantity')}x @ {value.get('value')} "
              f"gold each = {value.get('value') * value.get('quantity')} gold")
        inventory_value += (value.get('value') * value.get('quantity'))
        items_count += value.get('quantity')
    print()
    print(f"Inventory value: {inventory_value} gold")
    print(f"Item count: {items_count} items")
    print("Categories: ", end=" ")
    for key, value in items.items():
        print(f"{value['type']}({value['quantity']})", end="")
        if key != "shield":
            print(", ", end="")
    print("\n\n=== Transaction: Alice gives Bob 2 potions ===")
    alice_potion = inventory_data["players"]["alice"]["items"]["potion"]
    bob_potion = inventory_data["players"]["bob"]["items"]["potion"]
    alice_potion['quantity'] -= 2
    bob_potion['quantity'] += 2
    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_potion['quantity']}")
    print(f"Bob potions: {bob_potion['quantity']}")

    print("\n=== Inventory Analytics ===")
    inventory_value = 0
    items_count = 0
    for key, value in items.items():
        inventory_value += (value.get('value') * value.get('quantity'))
        items_count += value.get('quantity')
    print(f"Most valuable player: Alice ({inventory_value})")
    print(f"Most items: Alice ({items_count} items)")
    print("Rarest items:", end=" ")
    rare_list = []
    for key, value in inventory_data["catalog"].items():
        if value.get('rarity') == 'rare':
            rare_list.append(key)

    print(f"{rare_list[0]}, {rare_list[1]}")


if __name__ == "__main__":
    ft_inventory_system()
