from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

print(Path(__file__))
print(Path(__file__).resolve())

print("=====================================")
print(Path(__file__).resolve().parents[1])
print(Path(__file__).resolve().parents[2])
print(Path(__file__).resolve().parents[3])