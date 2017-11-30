
def handle_numbers(start, end, divisor):
    return len([x for x in range(start, end+1) if not x % divisor])


def handle_string(string):
    letters = sum(x.isalpha() for x in string)
    digits = sum(x.isdigit() for x in string)
    return f'Letters: {letters} \nDigits: {digits}'


def handle_list_of_tuples(array):
    """
        "sort it based on the next rules: name / age / height / weight"

    Did not understood proper way to sort. For retrieve exact same result:

    return sorted(input, key=lambda x: (x[1], x[2], x[3], x[0]), reverse=True)

    """

    from operator import itemgetter
    # return sorted(array, key=lambda x: (x[0], x[1], x[2]. x[3])
    return sorted(array, key=itemgetter(0, 1, 2, 3))


if __name__ == '__main__':
    print(handle_numbers(1, 10, 2))

    print(handle_string('dsadasd      123'))

    array = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
    ]

    print(handle_list_of_tuples(array))
