for first_digit in range(10):
    for second_digit in range(first_digit - 1):
        print("{:02d}".format(first_digit+second_digit), end=', ' if second_digit < 10 else '\n')
