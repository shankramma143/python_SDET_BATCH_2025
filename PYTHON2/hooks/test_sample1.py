# case1 using hooks function as a fixtures
#setup_function(function)
# teardown_function(function)

def setup_function(function):
   print("Launch Browser")


def teardown_function(function):
   print("Close Browser")


def test_one():
   print("Test one is executed")


def test_two():
   print("Test two is executed")


def test_three():
   print("Test three is executed")


def test_four():
   print("Test four is executed")


def test_five():
   print("Test five is executed")


def test_six():
   print("Test six is executed")