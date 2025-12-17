kids_lunch = {"Alice": {"Burger": 3, "Banana": 1},
              "Bob": {"Sandwich": 2, "Apple": 1},
              "Charlie": {"Pie": 4, "Sandwich": 5}}

alice_lunch = kids_lunch.get("Alice")
print(alice_lunch)
print(alice_lunch.items())
print(alice_lunch.get("Burger"))
print(alice_lunch.get("Banana"))

# print("-----------------------------------------")
# key, value
# for kid, lunch in kids_lunch.items():
#     print(f"Kid: {kid} -> Lunch: {lunch}")
#
#     for lunch_item, total in lunch.items():
#         print(f"Lunch Item: {lunch_item} -> {total}")


def get_kid_total_items(kid, lunch):
    kid_total_items = 0
    for k, v in lunch.get(kid).items():
        # print(f"{k} -> {v}")
        kid_total_items += v
    # print(f"TOTAL: {kid_total_items}")
    return kid_total_items

def get_item_total(item, lunch):
    item_total = 0

    for k, v in lunch.items():
        # print(v.get(item))
        item_total += int(v.get(item, 0))
    # print(f"Item Total: {item_total}")
    return item_total

    # for k, v in lunch.items():
    #     print(v.get(item))
    #     try:
    #         item_total += int(v.get(item))
    #     except:
    #         pass
    # print(f"Item Total: {item_total}")


print("-----------------------------------------")
alice_total = get_kid_total_items("Alice", kids_lunch)
print(f"Alice Total: {alice_total}")

print("-----------------------------------------")
sandwich_total = get_item_total("Sandwich", kids_lunch)
print(f"Sandwich Total: {sandwich_total}")


print("-----------------------------------------")
print(kids_lunch.get("Alice").get("Burger"))
print(kids_lunch.get("Alice").get("Banana"))
print(kids_lunch.get("Alice").get("Candy"))


print("-----------------------------------------")
for k, v in kids_lunch.items():
    print(f"{k} -> {v}")
    # print(v.items())

    for k2, v2 in v.items():
        print(f"{k2} -> {v2}")