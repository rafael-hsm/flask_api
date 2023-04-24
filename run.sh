#!/bin/bash

# Verifica se o pacote pipenv está instalado
if ! command -v pipenv &> /dev/null
then
    echo "pipenv não encontrado. Instalando pipenv..."
    pip install pipenv
fi

# Cria um ambiente virtual e instala as dependências
pipenv install

# Verifica se o sistema operacional é Linux
if [ "$(uname)" == "Linux" ]; then
    # Verifica se o pacote libpq-dev está instalado
    if ! dpkg -s libpq-dev &> /dev/null
    then
        echo "libpq-dev não encontrado. Instalando libpq-dev..."
        sudo apt-get install libpq-dev
    fi
fi

# Define as variáveis de ambiente
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    export FLASK_APP=main.py
else
    set FLASK_APP=main.py
fi

# Inicializa o banco de dados
flask db init

# Cria as migrações
flask db migrate

# Aplica as migrações
flask db upgrade

# Inicia o servidor Flask
flask run
