#! /usr/bin/python3
# pw.py - Um programa para repositório de senhas que não é seguro.

import sys
import pyperclip

PASSWORDS = {
    'email': 234324523452345,
    'blog': 34234,
    'windows': 3343434
}

if len(sys.argv) < 2:
    print('Use o comando: python pw.py email')
    sys.exit()

# O primeiro argumento da linha de comando é o nome da pessoa
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Senha para ' + account + ' copiada')
else:
    print('Conta ' + account + ' não existe')
