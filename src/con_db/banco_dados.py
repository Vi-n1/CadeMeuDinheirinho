# -*- coding: utf-8 -*-
import sqlite3
import pathlib
from .criardb import criabasedados

criabasedados()
caminho_db = pathlib.Path('.\dados/baseDados.db')
con = sqlite3.connect(str(caminho_db))
cursor = con.cursor()

_RECEITAS = 'RECEITAS'


def get_colunas(nome_tabela: str) -> list:
    """Retorna colunas da tabela

    Args:
        nome_tabela (str): Nome da tabela

    Returns:
        list: Todas as colunas
    """
    if nome_tabela == _RECEITAS:
        return ['id', 'categoria', 'descrição', 'valor', 'data', 'status']
    return ['id', 'categoria', 'descrição', 'valor', 'data']


def set_valores(nome_tabela: str, dados: list) -> None:
    """Coloca valores na tabela

    Args:
        nome_tabela (str): Nome da tabela
        dados (str): Dados que serão inseridos
    Returns:
        None: setter
    """
    if nome_tabela == _RECEITAS:
        cursor.execute(
            f"""INSERT INTO {nome_tabela}(categoria, descrição, valor, data, status)
            VALUES {dados[0], dados[1], dados[2], dados[3], dados[4]}"""
        )
    else:
        cursor.execute(
            f"""INSERT INTO {nome_tabela}(categoria, descrição, valor, data)
            VALUES {dados[0], dados[1], dados[2], dados[3]}"""
        )
    con.commit()

def get_coluna_especifica(nome_tabela: str, coluna: str) -> list:
    """Retorna valores de uma coluna

    Args:
        nome_tabela (str): Nome da tabela
        coluna (str): Colunas que serão buscadas
    Returns:
        list: valores da coluna [('foo',), ('bar',)]
    """
    consulta = cursor.execute(f""" SELECT {coluna} FROM {nome_tabela}""")
    resultado = consulta.fetchall()
    return resultado
    
def get_todos_valores(nome_tabela) -> list:
    """Retorna todos valores da tabela

    Args:
        nome_tabela (str): Nome da tabela
    Returns:
        list: valores das colunas
    """
    consulta = cursor.execute(f'SELECT * FROM {nome_tabela}')
    resultado = consulta.fetchall()
    
    return resultado
