

not_world = list('капотлмубгдис'.upper())
yes_world = list(''.upper())

with open('summary.txt') as rus_fl:
    rus_world_db = rus_fl.readlines()

for rus_word in rus_world_db:
    x = 0
    rus_word_strip = rus_word.strip('\n').upper()
    if len(rus_word_strip) == 5:
        for y_key in yes_world:
            if y_key not in rus_word_strip:
                x = 1

        for n_key in not_world:
            if n_key in rus_word_strip:
                x = 1
        if x == 0:
            print(f'{rus_word_strip}')
