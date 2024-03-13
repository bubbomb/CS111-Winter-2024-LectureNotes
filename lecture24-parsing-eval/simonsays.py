VERB_LIST = [
    'run',
    'jump',
    'eat', 
    'touch',
    'fly',
    'buy',
    'join', 
]

def simonize(phrase):
    phrase = phrase.strip()
    phrase = phrase.lower()

    all_words = phrase.split()
    print(all_words)
    first_word = all_words[0]
    print(first_word)

    if first_word in VERB_LIST:
        return f'Simon says "{phrase}"'

    raise TypeError(f'Needs a starting verb from this set: {VERB_LIST}')


if __name__ == '__main__':
    print('Welcome to Simon Says-er!')



    while True:
        phrase = input('Phase: ')

        if phrase == 'cease':
            break

        try:
            print()
            print(simonize(phrase))
            print()
        except TypeError as e:
            print('you had a syntax error:')
            print(e)

    print()
    print('Simon Says,  well played')