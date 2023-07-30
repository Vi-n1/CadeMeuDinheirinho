# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

CORES = [
    '#4a1564',
    '#a492ff',
    '#aaaaff',
    '#aaffff',
    '#aaff7f',
    '#cffacc',
    '#511595',
]


def plot_pizza(descricao: list, valor: list[int], titulo: str, salvar: bool):
    """Cria um gráfico de pizza das receitas ou despesas

    Args:
        descricao (list): Descrições das receitas ou despesas.
        valor (list[int]): Valores das receitas ou despesas.
        titulo (str): Contexto do gráfico
        salvar (bool): Salvar foto para plotar na aplicação.

    Returns:
        str | None: Caminho da foto ou None.
    """
    valores = [valor[i][0] for i in range(len(valor))]
    descricoes = [descricao[i][0] for i in range(len(descricao))]
    fig, ax = plt.subplots()
    ax.pie(
        valores, labels=descricoes, autopct='%.2f%%', shadow=True, colors=CORES
    )
    ax.set_title(titulo)
    if not salvar:
        plt.savefig(f'{titulo}.png')
        plt.close('all')
        return f'{titulo}.png'
    else:
        fig.show()


def plot_bar(
    valor: list[int],
    ylabel: str,
    categoria: list,
    data: list,
    titulo: str,
    salvar: bool,
) -> str | None:
    """Cria um gráfico de barras das receitas ou despesas.

    Args:
        valor (list[int]): Valores referente as categorias.
        ylabel (str): Texto exibido na vertical.
        categoria (list): Categorias das receitas ou despesas.
        data (list): Datas dos registos das receitas ou despesas.
        titulo (str): Titulo.
        salvar (bool): Salvar foto para plotar na aplicação.

    Returns:
        str | None: Caminho da foto ou None
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    valores = [valor[i][0] for i in range(len(valor))]
    Categorias = [categoria[i][0] for i in range(len(categoria))]
    meses = [data[i][0] for i in range(len(data))]
    barras_container = ax.bar(meses, valores, color=CORES)
    ax.set(ylabel=ylabel, title=titulo)
    ax.bar_label(barras_container, labels=Categorias)
    plt.xticks(rotation=20)
    if not salvar:
        plt.savefig(f'{titulo}.png')
        plt.close('all')
        return f'{titulo}.png'
    else:
        fig.show()
