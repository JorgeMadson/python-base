#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Esse código pega a lingua pela variavel de ambiente LANG
Com caso padrão em português

Como usar:
    export LANG=pt_BR

Como executar:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Jorge Madson"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US").split(".")[0]

msg = "Olá Mundo!"

if current_language == "en_US":
    msg = "Hello World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
