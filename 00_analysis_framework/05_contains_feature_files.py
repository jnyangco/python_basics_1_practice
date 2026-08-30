from pathlib import Path

def contains_feature_files(path: Path) -> bool:
    """Return True when the path is a feature file or contains feature files."""

    # if path is a file -> check if .feature file
    if path.is_file():
        return path.suffix == ".feature"

    # if path is not a file (that means can be a folder) -> check any list of *.feature files
    else:
        return any(path.rglob("*.feature"))



print(Path.cwd())
path_feature_file = Path("/Users/jerome/Developer/python/python_basics_1_practice/00_analysis_framework/05_test_feature_files/login.feature")
path_feature_folder = Path("/Users/jerome/Developer/python/python_basics_1_practice/00_analysis_framework/05_test_feature_files")


print(contains_feature_files(path_feature_file))
print(contains_feature_files(path_feature_folder))