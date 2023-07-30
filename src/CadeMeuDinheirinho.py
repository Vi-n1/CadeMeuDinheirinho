# -*- coding: utf-8 -*-
from ui.Janela import Ui_janela
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QTableWidgetItem,
    QMessageBox,
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPoint, Qt
import sys
import os
from plotting import plot_bar, plot_pizza
from con_db import banco_dados


class CadeMeuDinheirinho(QMainWindow, Ui_janela):
    def __init__(self):
        super(CadeMeuDinheirinho, self).__init__()

        # Configuração da janela.
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.janela_graficos.setVisible(False)
        self.DESPESAS = 'DESPESAS'
        self.RECEITAS = 'RECEITAS'

        # Atribuindo as funções aos botões.
        self.PB_minimizar.clicked.connect(lambda: self.showMinimized())
        self.PB_fechar.clicked.connect(lambda: self.close())
        self.PB_fechar_graficos.clicked.connect(self.fecha_janela_graficos)
        self.PB_plt_graficos.clicked.connect(self.pagina_grafico)
        self.PB_plt_externo_ganhos.clicked.connect(
            lambda: self.plot_barras(self.RECEITAS, True)
        )
        self.PB_plt_externo_gastos.clicked.connect(
            lambda: self.plot_barras(self.DESPESAS, True)
        )
        self.PB_plt_externo_evl_ganhos.clicked.connect(
            lambda: self.plot_evl(self.RECEITAS, True)
        )
        self.PB_plt_externo_evl_gastos.clicked.connect(
            lambda: self.plot_evl(self.DESPESAS, True)
        )
        self.PB_adicionar_receitas.clicked.connect(self.pagina_receita)
        self.PB_adicionar_despesas.clicked.connect(self.pagina_despesa)
        self.PB_nova_foto_usuario.clicked.connect(self.adiciona_foto_usuario)
        self.PB_adicionar_valores_receita.clicked.connect(
            self.adiciona_valores_receitas
        )
        self.PB_adicionar_valores_despesa.clicked.connect(
            self.adiciona_valores_despesas
        )

        # Adicionando colunas nas tabelas.
        self.TW_tabela_receita.setColumnCount(6)
        self.TW_tabela_receita.setHorizontalHeaderLabels(
            banco_dados.get_colunas(self.RECEITAS)
        )
        self.TW_tabela_despesa.setColumnCount(5)
        self.TW_tabela_despesa.setHorizontalHeaderLabels(
            banco_dados.get_colunas(self.DESPESAS)
        )

        # Verifica se foi salvo uma foto anteriormente.
        if os.path.exists('img.cfg'):
            with open('img.cfg', 'r') as arquivo:
                caminho_foto = arquivo.read()
                arquivo.close()
            self.L_foto_usuario.setPixmap(QPixmap(caminho_foto))
        # Atualiza os valores de: Saldo, Despesas, Receitas
        self.atualizar_sdr()

    # Plota gráfico de barras na tela ou na aplicação.
    def plot_barras(self, nome_tabela: str, plot_externo: bool = False):
        categorias = banco_dados.get_coluna_especifica(
            nome_tabela, 'categoria'
        )
        valores = banco_dados.get_coluna_especifica(nome_tabela, 'valor')
        datas = banco_dados.get_coluna_especifica(nome_tabela, 'data')
        if nome_tabela == self.RECEITAS:
            nome_vertical = 'Maior melhor'
            titulo = 'Ganhos'
        else:
            nome_vertical = 'Maior pior'
            titulo = 'Gastos'
        caminho_foto = plot_bar(
            valor=valores,
            ylabel=nome_vertical,
            categoria=categorias,
            data=datas,
            titulo=titulo,
            salvar=plot_externo,
        )
        if not plot_externo:
            # Colocando o gráfico no QLabel.
            if nome_tabela == self.RECEITAS:
                self.l_plt_ganhos.setPixmap(QPixmap(caminho_foto))
                os.remove(caminho_foto)
            else:
                self.l_plt_gastos.setPixmap(QPixmap(caminho_foto))
                os.remove(caminho_foto)

    # Plota gráfico de pizza na tela ou na aplicação.
    def plot_evl(self, nome_tabela: str, plot_externo: bool = False):
        descricoes = banco_dados.get_coluna_especifica(
            nome_tabela, 'descrição'
        )
        valores = banco_dados.get_coluna_especifica(nome_tabela, 'valor')
        titulo = nome_tabela
        caminho_foto = plot_pizza(
            descricao=descricoes,
            valor=valores,
            titulo=titulo,
            salvar=plot_externo,
        )
        if not plot_externo:
            # Colocando o gráfico no QLabel.
            if nome_tabela == self.RECEITAS:
                self.l_plt_evolucao_ganhos.setPixmap(QPixmap(caminho_foto))
                os.remove(caminho_foto)
            else:
                self.l_plt_evolucao_gastos.setPixmap(QPixmap(caminho_foto))
                os.remove(caminho_foto)

    # Plota todos os gráficos na aplicação.
    def plot_todos_graficos(self):
        self.plot_barras(self.RECEITAS)
        self.plot_barras(self.DESPESAS)
        self.plot_evl(self.RECEITAS)
        self.plot_evl(self.DESPESAS)

    # Esconde a janela de gráficos.
    def fecha_janela_graficos(self):
        self.janela_graficos.setEnabled(False)
        self.janela_graficos.setVisible(False)

    # Exibi a janela de gráficos.
    def pagina_grafico(self):
        self.plot_todos_graficos()
        self.janela_graficos.setEnabled(True)
        self.janela_graficos.setVisible(True)

    # Exibi a página de adicionar receitas.
    def pagina_receita(self):
        self.paginas.setCurrentIndex(1)
        self.atualizar_tabela(self.RECEITAS)

    # Exibi a página de adicionar despesas.
    def pagina_despesa(self):
        self.paginas.setCurrentIndex(2)
        self.atualizar_tabela(self.DESPESAS)

    # Adiciona uma foto do usuário.
    def adiciona_foto_usuario(self):
        caminho_foto = QFileDialog.getOpenFileName()
        self.L_foto_usuario.setPixmap(QPixmap(caminho_foto[0]))
        with open('img.cfg', 'w') as arquivo:
            arquivo.write(caminho_foto[0])
            arquivo.close()

    # Atualiza os valores de: Saldo, Despesas, Receitas
    def atualizar_sdr(self):
        valor_pesquisa_receita = banco_dados.get_coluna_especifica(
            self.RECEITAS, 'valor'
        )
        valor_receita = sum(
            [
                valor_pesquisa_receita[i][0]
                for i in range(len(valor_pesquisa_receita))
            ]
        )
        valor_pesquisa_despesas = banco_dados.get_coluna_especifica(
            self.DESPESAS, 'valor'
        )
        valor_despesas = sum(
            [
                valor_pesquisa_despesas[i][0]
                for i in range(len(valor_pesquisa_despesas))
            ]
        )
        valor_saldo = valor_receita - valor_despesas
        self.L_valor_receita.setText('{:,.2f}'.format(valor_receita))
        self.L_valor_despesas.setText('{:,.2f}'.format(valor_despesas))
        self.L_valor_saldo.setText('{:,.2f}'.format(valor_saldo))

    # Salva os valores no banco de dados.
    def adiciona_valores_receitas(self):
        # Verifica se o valor da receita é válido.
        if self.LE_valor_receita.text() != '':
            dados = [
                self.CB_salario_receita.currentText(),
                self.TE_descricao_receita.toPlainText(),
                self.LE_valor_receita.text(),
                self.DE_data_receita.text(),
                self.CB_tipo_receita.currentText(),
            ]
            banco_dados.set_valores(self.RECEITAS, dados)
            self.atualizar_tabela(self.RECEITAS)
        else:
            msg_error = QMessageBox(self)
            msg_error.setWindowTitle('Error no valor')
            msg_error.setText('Adicione o valor')
            msg_error.open()

    # Salva os valores no banco de dados.
    def adiciona_valores_despesas(self):
        # Verifica se o valor da despesa é válida.
        if self.LE_valor_despesa.text() != '':
            dados = [
                self.CB_salario_despesa.currentText(),
                self.TE_descricao_despesa.toPlainText(),
                self.LE_valor_despesa.text(),
                self.DE_data_despesa.text(),
            ]
            banco_dados.set_valores(self.DESPESAS, dados)
            self.atualizar_tabela(self.DESPESAS)
        else:
            msg_error = QMessageBox(self)
            msg_error.setWindowTitle('Error no valor')
            msg_error.setText('Adicione o valor')
            msg_error.open()

    # Busca valores no banco de dados e preenche a tabela.
    def atualizar_tabela(self, nome_tabela):
        linhas = banco_dados.get_todos_valores(nome_tabela)
        quantidade_linhas = len(linhas)
        if nome_tabela == self.RECEITAS:
            self.TW_tabela_receita.setRowCount(quantidade_linhas)
            for index_linha in range(quantidade_linhas):
                for index_coluna in range(6):
                    self.TW_tabela_receita.setItem(
                        index_linha,
                        index_coluna,
                        QTableWidgetItem(
                            f'{linhas[index_linha][index_coluna]}'
                        ),
                    )
        else:
            self.TW_tabela_despesa.setRowCount(quantidade_linhas)
            for index_linha in range(quantidade_linhas):
                for index_coluna in range(5):
                    self.TW_tabela_despesa.setItem(
                        index_linha,
                        index_coluna,
                        QTableWidgetItem(
                            f'{linhas[index_linha][index_coluna]}'
                        ),
                    )
        # Atualiza os valores de: Saldo, Despesas, Receitas
        self.atualizar_sdr()

    # Capturando o evento do mouse para mover a janela.
    def mousePressEvent(self, event):
        self.evento_antigo = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        # Se o mouse for pressionado e movido sobre um botão é levantado uma exceção
        try:
            delta = QPoint(
                event.globalPosition().toPoint() - self.evento_antigo
            )
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.evento_antigo = event.globalPosition().toPoint()

        except AttributeError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = CadeMeuDinheirinho()
    janela.show()
    sys.exit(app.exec())
