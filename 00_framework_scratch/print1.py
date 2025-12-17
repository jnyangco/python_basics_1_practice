


format_string = ("env={}, build={}, type={}".format("qa-1", "337.4.0", "regression"))
# the same with number -> format_string = ("env={0}, build={1}, type={2}".format("qa-1", "337.4.0", "regression"))
# reverse format -> format_string = ("env={2}, build={1}, type={0}".format("qa-1", "337.4.0", "regression"))
print(format_string)

