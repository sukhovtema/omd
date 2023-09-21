import random


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def choose_cocktail():
    cocktails = [
        "Махито 🍹",
        "Пина Калада 🍍",
        "Маргорита 🍸",
        "Космаполетен 🍸",
        "Мортини 🍸",
        "Секс на пляже 🍹",
        "Блуд Мэри 🍹",
        "Манхэттен 🍸",
        "Дайкири 🍹",
        "Бульварь страстей 🍸"
    ]

    return random.choice(cocktails)


def step2_umbrella():
    print(f'Сухая утка 🦆 успешно пришла в бар и коктейль {choose_cocktail()} покарил ее ум')


def step2_no_umbrella():
    print(f'Мокрая утка 🦆 не захотела покупать коктейль, а решила украсть {choose_cocktail()} у кого-то из гостей')


if __name__ == '__main__':
    step1()
