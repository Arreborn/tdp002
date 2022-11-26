# 1

def main():
    numbers = [1, 2, 3]
    numbers_ref = numbers
main()

# 2

def main():
    numbers = [1, 2, 3]
    numbers_ref = numbers.copy()
main()

# 3

def add_element(l, e):
    l.append(e)

def main():
    numbers = [1, 2, 3]
    add_element(numbers, 4)

main()

# 4

def add_element(l, e):
    l.append(e)

def main():
    numbers = [1, 2, 3]
    add_element(numbers.copy(), 4)

main()


