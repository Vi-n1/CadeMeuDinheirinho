# -*- coding: utf-8 -*-
import sqlite3
import os
import pathlib


def criabasedados() -> None:
    """
    Cria a base de dados
    RECEITA(id, categoria, descrição, valor, data, status)
    DESPESAS(id, categoria, descrição, valor, data, status)
    """
    caminho_dados = pathlib.Path('.\dados/')
    if not caminho_dados.exists():
        os.mkdir(caminho_dados)
        con = sqlite3.connect(str(caminho_dados) + '/baseDados.db')
        cursor = con.cursor()
        cursor.execute(
            """CREATE TABLE RECEITAS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            descrição TEXT,
            valor INTEGER NOT NULL,
            data TEXT NOT NULL,
            status TEXT NOT NULL
            )"""
        )
        cursor.execute(
            """CREATE TABLE DESPESAS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            descrição TEXT,
            valor INTEGER NOT NULL,
            data TEXT NOT NULL
            )"""
        )
        con.commit()
        con.close()
