test_pages = ["login", "homepage", "article"]

# for page in test_pages:
#     print(f"Testing {page} page")

# using enumerate (to have index)
# for index, page in enumerate(test_pages):
#     print(f"{index}: Testing {page} page")

for index, page in enumerate(test_pages, start=1):
    print(f"{index}: Testing {page} page")