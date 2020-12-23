

def execute(numbers):
    for x in numbers:
        for y in numbers:
            result = list(filter(lambda z: z == 2020-x-y, numbers))
            if result:
                return result[0] * x * y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('../Day2/input.txt', 'r')
    numbers = list(map(lambda x: int(x.strip()), file))
    print(execute(numbers))
