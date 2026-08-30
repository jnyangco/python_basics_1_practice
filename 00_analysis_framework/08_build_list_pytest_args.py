def build_pytest_args(
    pytest_target: str,
    env: str,
    # optional (with default values)
    tag: str | None = None,
    headed: bool = True,
    reruns_failures: int = 0,
    browser: str = "chrome",
) -> list[str]:

    command_list: list[str] = [pytest_target, env]

    if tag:
        command_list.append(tag)

    if headed:
        command_list.append(str(headed))

    if reruns_failures:
        command_list.append(str(reruns_failures))

    # .extent([]) -> adds multiple items to the list
    command_list.extend(["--browser-channel", browser])

    return command_list



get_command_list = build_pytest_args(pytest_target="/tests/login.feature", env="qa-1")
print(get_command_list)

get_command_list = build_pytest_args(pytest_target="/tests/login.feature", env="qa-1", tag="smoke", headed=True, reruns_failures=2, browser="edge")
print(get_command_list)

get_command_list = build_pytest_args(pytest_target="/tests/login.feature", env="qa-1", tag="smoke", headed=True, reruns_failures=2)
print(get_command_list)