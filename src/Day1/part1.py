
def execute(numbers):
    for x in numbers:
        result = list(filter(lambda y: y == 2020-x, numbers))
        if result:
            return result[0] * x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('input.txt', 'r')
    numbers = list(map(lambda x: int(x.strip()), file))
    print(execute(numbers))
