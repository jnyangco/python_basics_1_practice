import shlex
import subprocess
import sys


def _format_command(cmd: list[str]) -> str:
    """Format a command for display without changing how it runs."""

    if sys.platform == "win32":
        return subprocess.list2cmdline(cmd)
    return shlex.join(cmd)

command = [
    "/path/to/python",
    "-m",
    "pytest",
    "tests",
    "--env",
    "qa-1",
]

print(f"Format Command -> \n{_format_command(command)}")
# /path/to/python -m pytest tests --env qa-1