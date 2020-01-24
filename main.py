from earley import Earley
from rule import Rule


def main():
    word = input('Введите распознаваемое слово\n')

    earley = Earley(word)

    n = int(input('Введите количество правил в грамматике: '))
    print('Введите правила грамматики в формате S -> aB')
    for i in range(n):
        parts = input(f'Правило {i + 1} из {n}: ').split()
        if len(parts) != 3:
            print("Неправильное правило")
            exit(1)
        earley.add_rule(Rule(parts[0], parts[2]))
    earley.add_rule(Rule('S#', 'S'))

    if earley.get_answer():
        print("YES\n")
    else:
        print("NO\n")


if __name__ == "__main__":
    main()
