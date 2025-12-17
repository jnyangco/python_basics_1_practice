inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def show_all_inventory(stuffs):
    for key, value in stuffs.items():
        print(f"{key} -> {value}")


def get_item_count_in_inventory(item, stuffs):
    return stuffs.get(item.lower())

def add_item_to_inventory(add_item, count, inventory_list):
    # print(add_item in inventory_list)
    # print(add_item in inventory_list.keys())
    # print(add_item in inventory_list.values())
    # print(add_item in inventory_list.items())

    if add_item in inventory_list:
        print(f"{add_item} is existing. Adding {count}")
        inventory_list[add_item] += count
        # print(f"After count: {inventory_list[add_item]}")
    else:
        print(f"{add_item} is not existing. Set count {count}")
        inventory_list[add_item] = count


    # for key in inventory_list:
    #     # print(key)
    #     if add_item == key:
    #         print("Zig")
    #         inventory_list[key] += count
    #     else:
    #         inventory_list[key] = count
    # print(inventory_list.get("zig"))


print("-------------------------")
show_all_inventory(inventory)

print("-------------------------")
gold_coin_total = get_item_count_in_inventory("gold coin", inventory)
print(gold_coin_total)

print("-------------------------")
print("-------------------------")
print(f"Rope Total: {inventory.get("rope")}")
add_item_to_inventory("rope", 10, inventory)
print(f"Rope Total: {inventory.get("rope")}")

print("-------------------------")
print("-------------------------")
print(f"Shiel Total: {inventory.get("shield")}")
add_item_to_inventory("shield", 20, inventory)
print(f"Shiel Total: {inventory.get("shield")}")
