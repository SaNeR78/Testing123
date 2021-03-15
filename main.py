# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import yaml

if __name__ == '__main__':
    # print('{0:15.4f}{1:15.4f}{2:15.4f}{3:15.4f}\n'
    #       '{4:15.4f}{5:15.4f}{6:15.4f}{7:15.4f}'.format(0.21334325, 0.32424325, 0.24353256,
    #                                                     0.21343466, 0.24325366, 0.42636222,
    #                                                     0.32425566, 0.14346766))
    # list_one = [1, 2, 3, 4, 5, 6]
    # list_two = list_one[1:4]
    # print(list_two)

    # example = {'one': 1, 'two': 2}
    # print(example['one'])
    #
    # computer = (
    #     'Dell',
    #     'Latitude 7480',
    #     '8 Gb',
    #     'Windows 10',
    #     '1 Tb'
    # )
    #
    # name, model, capacity, os, ssd = computer
    #
    # print(f"Характеристики компьютера:\n"
    #       f"Наименование марки: {name}\n"
    #       f"Модель: {model}\n"
    #       f"Объем оперативной памяти: {capacity}\n"
    #       f"Операционная система: {os}\n"
    #       f"Объем жесткого диска: {ssd}")

    # text = 'Hello! This text haven\'t meaning'
    #
    # sets = set(text)
    #
    # print(sets)
    # print(type(sets))

    # answer = int(input('Enter any number'))
    # if answer == 7:
    #     print(f'{answer} is a lucky number! Today is your lucky day!')
    # else:
    #     print('Thank you! Have a nice day!')

    # try:
    #     number = int(input('Enter an integer number'))
    #
    #     if number % 2 == 0:
    #         print('This number is even')
    #     elif number % 2 != 0:
    #         print('This number is odd')
    #
    # except ValueError as e:
    #     print('Please, enter integer')

    # def odd_numbers(a=0, b=1):
    #     numbers_list = []
    #     for number in range(a, b + 1, 2):
    #         numbers_list.append(number)
    #     return numbers_list
    #
    #
    # print(odd_numbers(1, 10))
    #
    # def odd_numbers_1(a=0, b=1):
    #     numbers_list = ''
    #     for number in range(a, b + 1, 2):
    #         numbers_list += str(number) + ' '
    #     return numbers_list
    #
    #
    # print(odd_numbers_1(1, 10))

    with open('YAMLex/a.yml', 'r') as f:
        s = yaml.load(f, Loader=yaml.FullLoader)
        for i in s:
            if i.get('games'):
                for y in i.values():
                    if 'games_name' in y.keys():
                        print(y.get('games_name'))

    with open('YAMLex/martin.yml', 'r') as f:
        s = yaml.load(f, Loader=yaml.FullLoader)
        for i in s:
            if 'martin' in i.keys():
                for y in i.values():
                    if 'skills' in y.keys():
                        a = y.get('skills')
                        for b in a:
                            if 'pascal' in b:
                                print(b)
