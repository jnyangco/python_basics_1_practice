status_code = 200

if status_code == 200:
    print("Test passed")
elif status_code == 400:
    print("Server error")
else:
    print("Test failed")