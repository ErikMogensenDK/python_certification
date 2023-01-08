# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


#print(add_time("11:06 PM", "2:02"))
#print(add_time("3:30 PM", "2:12"))
#print(add_time("11:59 PM", "24:05"))

#actual = add_time("2:59 AM", "24:00")
#expected = "2:59 AM (next day)"
#print(actual)
#print(expected)
#print('Expected 13:06)


# Run unit tests automatically
main(module='test_module', exit=False)