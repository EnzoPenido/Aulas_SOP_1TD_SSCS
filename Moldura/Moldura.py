frase = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDigite uma frase: \n')
ch = '\u2588'
for i in range(len(frase)+4):
    print(ch, end='')
print(f'\n{ch} {frase} {ch}')
for i in range(len(frase)+4):
    print(ch, end='')