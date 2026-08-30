from pathlib import Path

path1 = Path("/Users/jerome/project/tests") # True
path2 = Path("Users/jerome/project/tests")  # False
path3 = Path("login.feature")

print(path1.is_absolute())
print(path2.is_absolute())

# cwd -> current working directory
print(Path.cwd())
print(Path.cwd() / path3)

