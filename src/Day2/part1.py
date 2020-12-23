
def execute(pwds):
        return list(filter(lambda pwd: pwd is not None and validate(pwd), pwds)).__len__()


def validate(password):
    splt = password.split(' ')
    min_max = splt[0].split('-')
    return int(min_max[0]) <= count(splt[-1], splt[1].replace(':', '')) <= int(min_max[1])


def count(pwd, criteria):
    return list(filter(lambda letter: letter == criteria, pwd)).__len__()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('input.txt', 'r')
    passwords = list(map(lambda x: x.strip(), file))
    print(execute(passwords))
