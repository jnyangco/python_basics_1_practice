import shlex
import subprocess
import sys
from pathlib import Path

test_path =         Path("/project/tests/features/cms/auth/login.feature")
test_parent_path =  Path("/project/tests/features")

# result = Path("/project/tests/features/cms/auth/login.feature").relative_to(Path("/project/tests/features"))
result = Path(test_path).relative_to(test_parent_path)

print("====================================================")
print(f"Result Path -> {result}")
# returns -> cms/auth/login.feature
# That means the path is inside the parent.


def _is_inside_path(path: Path, parent_path: Path) -> bool:
    """Return True when path is inside parent."""
    try:
        path.relative_to(parent_path)
        return True
    except ValueError:
        return False


def _as_command_path(path: Path) -> str:
    """Use a project-relative path when possible to keep the command readable."""
    try:
        return str(path.relative_to(Path(__file__)))
    except ValueError:
        return str(path)



print("====================================================")
result_bool = _is_inside_path(test_path, test_parent_path)
print(f"Result bool: {result_bool}")


print("====================================================")
print(_as_command_path(test_path))
print(_as_command_path(test_parent_path))