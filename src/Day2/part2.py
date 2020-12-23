def execute(passwords):
    return list(filter(lambda pwd: pwd is not None and check(pwd), passwords)).__len__()


def check(password):
    splitted = password.split(' ')
    min_max = splitted[0].split('-')
    return validate(splitted[-1], splitted[1].replace(':', ''), min_max)


def validate(pwd, criteria, positions):
    first, last = int(positions[0]) - 1, int(positions[1]) - 1
    return (pwd[first] == criteria or pwd[last] == criteria) and pwd[first] != pwd[last]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('input.txt', 'r')
    passwords = list(map(lambda x: x.strip(), file))
    print(execute(passwords))
