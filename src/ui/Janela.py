# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Janela.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)
from .icons_rc import *

class Ui_janela(object):
    def setupUi(self, janela):
        if not janela.objectName():
            janela.setObjectName(u"janela")
        janela.setEnabled(True)
        janela.resize(1463, 600)
        janela.setMinimumSize(QSize(800, 600))
        janela.setMaximumSize(QSize(1463, 600))
        janela.setStyleSheet(u"")
        self.centralwidget = QWidget(janela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.204545 rgba(172, 133, 226, 255), stop:0.994318 rgba(32, 27, 44, 118));\n"
"border: 2px solid rgb(164, 146, 255);\n"
"border-radius: 50%;\n"
"}\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"}\n"
"QPushButton{\n"
"border-radius: 10%;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(74, 21, 100);\n"
"border: 1px solid  rgb(164, 146, 255);\n"
"}\n"
"QPushButton::pressed{\n"
"font: 700 12pt \"Comic Sans MS\";\n"
"border: 2px solid rgb(164, 146, 255);\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(71, 21, 120);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 151, 121))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(74, 21, 100);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 60, 151, 121))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(74, 21, 100);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(263, 0, 291, 61))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(239, 255, 201);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.label_saldo = QLabel(self.frame)
        self.label_saldo.setObjectName(u"label_saldo")
        self.label_saldo.setGeometry(QRect(30, 30, 91, 16))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_saldo.setFont(font2)
        self.label_saldo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.label_saldo.setAlignment(Qt.AlignCenter)
        self.label_receita = QLabel(self.frame)
        self.label_receita.setObjectName(u"label_receita")
        self.label_receita.setEnabled(True)
        self.label_receita.setGeometry(QRect(140, 80, 111, 16))
        self.label_receita.setFont(font2)
        self.label_receita.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.label_receita.setAlignment(Qt.AlignCenter)
        self.L_valor_saldo = QLabel(self.frame)
        self.L_valor_saldo.setObjectName(u"L_valor_saldo")
        self.L_valor_saldo.setGeometry(QRect(10, 50, 131, 51))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.L_valor_saldo.setFont(font3)
        self.L_valor_saldo.setAutoFillBackground(False)
        self.L_valor_saldo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.L_valor_saldo.setScaledContents(False)
        self.L_valor_saldo.setAlignment(Qt.AlignCenter)
        self.L_valor_receita = QLabel(self.frame)
        self.L_valor_receita.setObjectName(u"L_valor_receita")
        self.L_valor_receita.setGeometry(QRect(130, 100, 131, 51))
        self.L_valor_receita.setFont(font3)
        self.L_valor_receita.setAutoFillBackground(False)
        self.L_valor_receita.setStyleSheet(u"color: rgb(85, 170, 127);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.L_valor_receita.setScaledContents(False)
        self.L_valor_receita.setAlignment(Qt.AlignCenter)
        self.PB_fechar = QPushButton(self.frame)
        self.PB_fechar.setObjectName(u"PB_fechar")
        self.PB_fechar.setGeometry(QRect(735, 2, 31, 20))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.PB_fechar.setFont(font4)
        self.PB_fechar.setStyleSheet(u"")
        self.PB_minimizar = QPushButton(self.frame)
        self.PB_minimizar.setObjectName(u"PB_minimizar")
        self.PB_minimizar.setGeometry(QRect(700, 2, 31, 20))
        self.PB_minimizar.setFont(font4)
        self.PB_minimizar.setStyleSheet(u"")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 100, 151, 121))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(74, 21, 100);")
        self.label_despesas = QLabel(self.frame)
        self.label_despesas.setObjectName(u"label_despesas")
        self.label_despesas.setEnabled(True)
        self.label_despesas.setGeometry(QRect(10, 130, 111, 16))
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        self.label_despesas.setFont(font5)
        self.label_despesas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"")
        self.label_despesas.setAlignment(Qt.AlignCenter)
        self.L_valor_despesas = QLabel(self.frame)
        self.L_valor_despesas.setObjectName(u"L_valor_despesas")
        self.L_valor_despesas.setGeometry(QRect(10, 150, 131, 51))
        self.L_valor_despesas.setFont(font3)
        self.L_valor_despesas.setAutoFillBackground(False)
        self.L_valor_despesas.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(141, 0, 0);\n"
"border: 0px;\n"
"")
        self.L_valor_despesas.setScaledContents(False)
        self.L_valor_despesas.setAlignment(Qt.AlignCenter)
        self.paginas = QStackedWidget(self.frame)
        self.paginas.setObjectName(u"paginas")
        self.paginas.setGeometry(QRect(10, 230, 781, 361))
        self.paginas.setFont(font)
        self.paginas.setStyleSheet(u"QStackedWidget{\n"
"	border-radius: 0;\n"
"	border: 0px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel{\n"
"	color: rgb(85, 170, 127);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 0px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10%;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(74, 21, 100);\n"
"	border: 1px solid  rgb(164, 146, 255);\n"
"}\n"
"QPushButton::pressed{\n"
"	font: 700 12pt \"Comic Sans MS\";\n"
"	border: 2px solid rgb(164, 146, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(71, 21, 120);\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 10%;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(74, 21, 100);\n"
"}\n"
"QTextEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid  rgb(164, 146, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(74, 21, 100);\n"
"}\n"
"QDateEdit{\n"
"	border-radius: 5%;\n"
"	color: rgb(239, 255, 201);\n"
"	background-color: rgb(74, 21, 100);\n"
"}\n"
"QComboBox{\n"
"	border-radius: 5%;\n"
"	border: 1px solid  "
                        "rgb(164, 146, 255);\n"
"	color: rgb(239, 255, 201);\n"
"	background-color: rgb(74, 21, 100);\n"
"}\n"
"QComboBox QListView{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QTableView{\n"
"	border-radius: 6%;\n"
"	border: 1px solid  rgb(164, 146, 255);\n"
"	color: rgb(85, 170, 127);\n"
"	background-color: rgb(74, 21, 100);\n"
"}")
        self.pg_inicial = QWidget()
        self.pg_inicial.setObjectName(u"pg_inicial")
        self.L_link_git = QLabel(self.pg_inicial)
        self.L_link_git.setObjectName(u"L_link_git")
        self.L_link_git.setGeometry(QRect(0, 0, 781, 321))
        self.L_link_git.setOpenExternalLinks(True)
        self.L_link_git.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label = QLabel(self.pg_inicial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(317, 142, 41, 41))
        self.label.setPixmap(QPixmap(u":/git/github-mark.png"))
        self.label.setScaledContents(True)
        self.paginas.addWidget(self.pg_inicial)
        self.label.raise_()
        self.L_link_git.raise_()
        self.pg_receita = QWidget()
        self.pg_receita.setObjectName(u"pg_receita")
        self.LE_valor_receita = QLineEdit(self.pg_receita)
        self.LE_valor_receita.setObjectName(u"LE_valor_receita")
        self.LE_valor_receita.setGeometry(QRect(390, 60, 113, 22))
        font6 = QFont()
        font6.setPointSize(9)
        self.LE_valor_receita.setFont(font6)
        self.LE_valor_receita.setStyleSheet(u"")
        self.LE_valor_receita.setInputMethodHints(Qt.ImhNone)
        self.LE_valor_receita.setMaxLength(11)
        self.LE_valor_receita.setAlignment(Qt.AlignCenter)
        self.LE_valor_receita.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.LE_valor_receita.setClearButtonEnabled(True)
        self.label_descricao = QLabel(self.pg_receita)
        self.label_descricao.setObjectName(u"label_descricao")
        self.label_descricao.setGeometry(QRect(0, 30, 121, 31))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(17)
        font7.setBold(True)
        self.label_descricao.setFont(font7)
        self.TE_descricao_receita = QTextEdit(self.pg_receita)
        self.TE_descricao_receita.setObjectName(u"TE_descricao_receita")
        self.TE_descricao_receita.setGeometry(QRect(110, 60, 191, 81))
        font8 = QFont()
        font8.setFamilies([u"Comic Sans MS"])
        self.TE_descricao_receita.setFont(font8)
        self.label_valor = QLabel(self.pg_receita)
        self.label_valor.setObjectName(u"label_valor")
        self.label_valor.setGeometry(QRect(320, 55, 81, 31))
        self.label_valor.setFont(font7)
        self.label_data = QLabel(self.pg_receita)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setGeometry(QRect(320, 86, 61, 31))
        self.label_data.setFont(font7)
        self.DE_data_receita = QDateEdit(self.pg_receita)
        self.DE_data_receita.setObjectName(u"DE_data_receita")
        self.DE_data_receita.setGeometry(QRect(390, 90, 110, 22))
        self.DE_data_receita.setFont(font8)
        self.DE_data_receita.setMaximumDateTime(QDateTime(QDate(2023, 12, 31), QTime(20, 59, 59)))
        self.DE_data_receita.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.DE_data_receita.setCalendarPopup(True)
        self.DE_data_receita.setTimeSpec(Qt.LocalTime)
        self.label_categoria = QLabel(self.pg_receita)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setGeometry(QRect(522, 30, 121, 31))
        self.label_categoria.setFont(font7)
        self.CB_salario_receita = QComboBox(self.pg_receita)
        icon = QIcon()
        icon.addFile(u":/icons/carteira-hover.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CB_salario_receita.addItem(icon, "")
        self.CB_salario_receita.addItem(icon, "")
        self.CB_salario_receita.addItem(icon, "")
        self.CB_salario_receita.setObjectName(u"CB_salario_receita")
        self.CB_salario_receita.setGeometry(QRect(520, 60, 131, 31))
        self.CB_salario_receita.setFont(font8)
        self.CB_tipo_receita = QComboBox(self.pg_receita)
        self.CB_tipo_receita.addItem("")
        self.CB_tipo_receita.addItem("")
        self.CB_tipo_receita.setObjectName(u"CB_tipo_receita")
        self.CB_tipo_receita.setGeometry(QRect(520, 100, 131, 31))
        self.CB_tipo_receita.setFont(font8)
        self.line = QFrame(self.pg_receita)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 156, 781, 2))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_adicionar_receita = QLabel(self.pg_receita)
        self.label_adicionar_receita.setObjectName(u"label_adicionar_receita")
        self.label_adicionar_receita.setGeometry(QRect(260, 17, 251, 35))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_adicionar_receita.setFont(font9)
        self.PB_adicionar_valores_receita = QPushButton(self.pg_receita)
        self.PB_adicionar_valores_receita.setObjectName(u"PB_adicionar_valores_receita")
        self.PB_adicionar_valores_receita.setGeometry(QRect(425, 120, 75, 24))
        self.TW_tabela_receita = QTableWidget(self.pg_receita)
        self.TW_tabela_receita.setObjectName(u"TW_tabela_receita")
        self.TW_tabela_receita.setGeometry(QRect(0, 160, 781, 185))
        self.TW_tabela_receita.setRowCount(0)
        self.TW_tabela_receita.horizontalHeader().setCascadingSectionResizes(False)
        self.TW_tabela_receita.horizontalHeader().setStretchLastSection(True)
        self.TW_tabela_receita.verticalHeader().setVisible(False)
        self.paginas.addWidget(self.pg_receita)
        self.pg_despesa = QWidget()
        self.pg_despesa.setObjectName(u"pg_despesa")
        self.LE_valor_despesa = QLineEdit(self.pg_despesa)
        self.LE_valor_despesa.setObjectName(u"LE_valor_despesa")
        self.LE_valor_despesa.setGeometry(QRect(390, 60, 113, 22))
        font10 = QFont()
        font10.setFamilies([u"Comic Sans MS"])
        font10.setPointSize(9)
        self.LE_valor_despesa.setFont(font10)
        self.LE_valor_despesa.setStyleSheet(u"")
        self.LE_valor_despesa.setInputMethodHints(Qt.ImhNone)
        self.LE_valor_despesa.setMaxLength(11)
        self.LE_valor_despesa.setAlignment(Qt.AlignCenter)
        self.LE_valor_despesa.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.LE_valor_despesa.setClearButtonEnabled(True)
        self.label_despesas_valor = QLabel(self.pg_despesa)
        self.label_despesas_valor.setObjectName(u"label_despesas_valor")
        self.label_despesas_valor.setGeometry(QRect(320, 55, 81, 31))
        self.label_despesas_valor.setFont(font7)
        self.label_despesas_valor.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_despesas_categoria = QLabel(self.pg_despesa)
        self.label_despesas_categoria.setObjectName(u"label_despesas_categoria")
        self.label_despesas_categoria.setGeometry(QRect(522, 30, 121, 31))
        self.label_despesas_categoria.setFont(font7)
        self.label_despesas_categoria.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.CB_salario_despesa = QComboBox(self.pg_despesa)
        self.CB_salario_despesa.addItem(icon, "")
        self.CB_salario_despesa.addItem(icon, "")
        self.CB_salario_despesa.addItem(icon, "")
        self.CB_salario_despesa.addItem("")
        self.CB_salario_despesa.setObjectName(u"CB_salario_despesa")
        self.CB_salario_despesa.setGeometry(QRect(520, 60, 131, 31))
        self.CB_salario_despesa.setFont(font8)
        self.DE_data_despesa = QDateEdit(self.pg_despesa)
        self.DE_data_despesa.setObjectName(u"DE_data_despesa")
        self.DE_data_despesa.setGeometry(QRect(390, 90, 110, 22))
        self.DE_data_despesa.setMaximumDateTime(QDateTime(QDate(2023, 12, 31), QTime(20, 59, 59)))
        self.DE_data_despesa.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.DE_data_despesa.setCalendarPopup(True)
        self.DE_data_despesa.setTimeSpec(Qt.LocalTime)
        self.label_despesas_data = QLabel(self.pg_despesa)
        self.label_despesas_data.setObjectName(u"label_despesas_data")
        self.label_despesas_data.setGeometry(QRect(320, 86, 61, 31))
        self.label_despesas_data.setFont(font7)
        self.label_despesas_data.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.line_2 = QFrame(self.pg_despesa)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 156, 781, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_adicionar_despesas = QLabel(self.pg_despesa)
        self.label_adicionar_despesas.setObjectName(u"label_adicionar_despesas")
        self.label_adicionar_despesas.setGeometry(QRect(260, 17, 261, 35))
        self.label_adicionar_despesas.setFont(font9)
        self.label_adicionar_despesas.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.TE_descricao_despesa = QTextEdit(self.pg_despesa)
        self.TE_descricao_despesa.setObjectName(u"TE_descricao_despesa")
        self.TE_descricao_despesa.setGeometry(QRect(110, 60, 191, 81))
        font11 = QFont()
        font11.setFamilies([u"Comic Sans MS"])
        font11.setBold(False)
        self.TE_descricao_despesa.setFont(font11)
        self.label_despesas_descricao = QLabel(self.pg_despesa)
        self.label_despesas_descricao.setObjectName(u"label_despesas_descricao")
        self.label_despesas_descricao.setGeometry(QRect(0, 30, 121, 31))
        self.label_despesas_descricao.setFont(font7)
        self.label_despesas_descricao.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.PB_adicionar_valores_despesa = QPushButton(self.pg_despesa)
        self.PB_adicionar_valores_despesa.setObjectName(u"PB_adicionar_valores_despesa")
        self.PB_adicionar_valores_despesa.setGeometry(QRect(425, 120, 75, 24))
        self.TW_tabela_despesa = QTableWidget(self.pg_despesa)
        self.TW_tabela_despesa.setObjectName(u"TW_tabela_despesa")
        self.TW_tabela_despesa.setGeometry(QRect(0, 160, 781, 185))
        font12 = QFont()
        font12.setFamilies([u"Arial"])
        self.TW_tabela_despesa.setFont(font12)
        self.TW_tabela_despesa.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.TW_tabela_despesa.setRowCount(0)
        self.TW_tabela_despesa.horizontalHeader().setCascadingSectionResizes(False)
        self.TW_tabela_despesa.horizontalHeader().setStretchLastSection(True)
        self.TW_tabela_despesa.verticalHeader().setVisible(False)
        self.paginas.addWidget(self.pg_despesa)
        self.PB_adicionar_receitas = QPushButton(self.frame)
        self.PB_adicionar_receitas.setObjectName(u"PB_adicionar_receitas")
        self.PB_adicionar_receitas.setGeometry(QRect(280, 192, 121, 31))
        self.PB_adicionar_receitas.setFont(font)
        self.PB_adicionar_receitas.setStyleSheet(u"")
        self.PB_adicionar_receitas.setIconSize(QSize(16, 16))
        self.L_foto_usuario = QLabel(self.frame)
        self.L_foto_usuario.setObjectName(u"L_foto_usuario")
        self.L_foto_usuario.setGeometry(QRect(280, 50, 251, 141))
        self.L_foto_usuario.setStyleSheet(u"")
        self.L_foto_usuario.setScaledContents(True)
        self.L_foto_usuario.setAlignment(Qt.AlignCenter)
        self.PB_adicionar_despesas = QPushButton(self.frame)
        self.PB_adicionar_despesas.setObjectName(u"PB_adicionar_despesas")
        self.PB_adicionar_despesas.setGeometry(QRect(400, 192, 131, 31))
        self.PB_adicionar_despesas.setFont(font)
        self.PB_adicionar_despesas.setStyleSheet(u"")
        self.PB_nova_foto_usuario = QPushButton(self.frame)
        self.PB_nova_foto_usuario.setObjectName(u"PB_nova_foto_usuario")
        self.PB_nova_foto_usuario.setGeometry(QRect(510, 170, 21, 20))
        self.PB_nova_foto_usuario.setFont(font4)
        self.PB_nova_foto_usuario.setStyleSheet(u"")
        self.PB_plt_graficos = QPushButton(self.frame)
        self.PB_plt_graficos.setObjectName(u"PB_plt_graficos")
        self.PB_plt_graficos.setGeometry(QRect(354, 224, 91, 26))
        self.PB_plt_graficos.setFont(font)
        self.PB_plt_graficos.setStyleSheet(u"")
        self.paginas.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_receita.raise_()
        self.label_saldo.raise_()
        self.L_valor_saldo.raise_()
        self.L_valor_receita.raise_()
        self.PB_fechar.raise_()
        self.PB_minimizar.raise_()
        self.label_despesas.raise_()
        self.L_valor_despesas.raise_()
        self.PB_adicionar_receitas.raise_()
        self.L_foto_usuario.raise_()
        self.PB_adicionar_despesas.raise_()
        self.PB_nova_foto_usuario.raise_()
        self.PB_plt_graficos.raise_()
        self.janela_graficos = QFrame(self.centralwidget)
        self.janela_graficos.setObjectName(u"janela_graficos")
        self.janela_graficos.setEnabled(False)
        self.janela_graficos.setGeometry(QRect(785, 30, 671, 511))
        self.janela_graficos.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 2px solid;\n"
"	border-right-color: rgb(164, 146, 255);\n"
"	border-top-color: rgb(164, 146, 255);\n"
"	border-bottom-color: rgb(164, 146, 255);\n"
"	border-left-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 50%;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10%;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(74, 21, 100);\n"
"	border: 1px solid  rgb(164, 146, 255);\n"
"}\n"
"QPushButton::pressed{\n"
"	font: 700 12pt \"Comic Sans MS\";\n"
"	border: 2px solid rgb(164, 146, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(71, 21, 120);\n"
"}\n"
"QLabel{\n"
"	border-radius: 0;\n"
"}")
        self.janela_graficos.setFrameShape(QFrame.StyledPanel)
        self.janela_graficos.setFrameShadow(QFrame.Raised)
        self.l_plt_evolucao_gastos = QLabel(self.janela_graficos)
        self.l_plt_evolucao_gastos.setObjectName(u"l_plt_evolucao_gastos")
        self.l_plt_evolucao_gastos.setGeometry(QRect(350, 10, 291, 231))
        self.l_plt_evolucao_gastos.setStyleSheet(u"")
        self.l_plt_evolucao_gastos.setScaledContents(True)
        self.l_plt_evolucao_ganhos = QLabel(self.janela_graficos)
        self.l_plt_evolucao_ganhos.setObjectName(u"l_plt_evolucao_ganhos")
        self.l_plt_evolucao_ganhos.setGeometry(QRect(350, 250, 291, 231))
        self.l_plt_evolucao_ganhos.setStyleSheet(u"")
        self.l_plt_evolucao_ganhos.setScaledContents(True)
        self.l_plt_ganhos = QLabel(self.janela_graficos)
        self.l_plt_ganhos.setObjectName(u"l_plt_ganhos")
        self.l_plt_ganhos.setGeometry(QRect(20, 250, 321, 231))
        self.l_plt_ganhos.setStyleSheet(u"")
        self.l_plt_ganhos.setScaledContents(True)
        self.l_plt_gastos = QLabel(self.janela_graficos)
        self.l_plt_gastos.setObjectName(u"l_plt_gastos")
        self.l_plt_gastos.setGeometry(QRect(20, 10, 321, 231))
        self.l_plt_gastos.setStyleSheet(u"")
        self.l_plt_gastos.setScaledContents(True)
        self.line_3 = QFrame(self.janela_graficos)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(343, 180, 4, 131))
        self.line_3.setStyleSheet(u"background-color: rgb(71, 21, 120);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.janela_graficos)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(286, 245, 118, 4))
        self.line_4.setStyleSheet(u"background-color: rgb(71, 21, 120);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(self.janela_graficos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(325, 225, 41, 41))
        self.label_5.setStyleSheet(u"background-color: rgb(71, 21, 120);\n"
"border-color: rgba(0, 0, 0, 0);\n"
"border-radius: 20%;")
        self.PB_fechar_graficos = QPushButton(self.janela_graficos)
        self.PB_fechar_graficos.setObjectName(u"PB_fechar_graficos")
        self.PB_fechar_graficos.setGeometry(QRect(640, 15, 21, 21))
        self.PB_plt_externo_ganhos = QPushButton(self.janela_graficos)
        self.PB_plt_externo_ganhos.setObjectName(u"PB_plt_externo_ganhos")
        self.PB_plt_externo_ganhos.setGeometry(QRect(320, 460, 20, 20))
        self.PB_plt_externo_evl_ganhos = QPushButton(self.janela_graficos)
        self.PB_plt_externo_evl_ganhos.setObjectName(u"PB_plt_externo_evl_ganhos")
        self.PB_plt_externo_evl_ganhos.setGeometry(QRect(620, 460, 20, 20))
        self.PB_plt_externo_evl_gastos = QPushButton(self.janela_graficos)
        self.PB_plt_externo_evl_gastos.setObjectName(u"PB_plt_externo_evl_gastos")
        self.PB_plt_externo_evl_gastos.setGeometry(QRect(620, 220, 20, 20))
        self.PB_plt_externo_gastos = QPushButton(self.janela_graficos)
        self.PB_plt_externo_gastos.setObjectName(u"PB_plt_externo_gastos")
        self.PB_plt_externo_gastos.setGeometry(QRect(320, 220, 20, 20))
        self.label_5.raise_()
        self.l_plt_evolucao_gastos.raise_()
        self.l_plt_evolucao_ganhos.raise_()
        self.l_plt_ganhos.raise_()
        self.l_plt_gastos.raise_()
        self.line_4.raise_()
        self.line_3.raise_()
        self.PB_fechar_graficos.raise_()
        self.PB_plt_externo_ganhos.raise_()
        self.PB_plt_externo_evl_ganhos.raise_()
        self.PB_plt_externo_evl_gastos.raise_()
        self.PB_plt_externo_gastos.raise_()
        janela.setCentralWidget(self.centralwidget)
        self.janela_graficos.raise_()
        self.frame.raise_()

        self.retranslateUi(janela)

        self.paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(janela)
    # setupUi

    def retranslateUi(self, janela):
        janela.setWindowTitle(QCoreApplication.translate("janela", u"Or\u00e7amento Pessoal", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("janela", u"Cad\u00ea Meu Dinheirinho", None))
        self.label_saldo.setText(QCoreApplication.translate("janela", u"Saldo", None))
        self.label_receita.setText(QCoreApplication.translate("janela", u"Receitas", None))
        self.L_valor_saldo.setText(QCoreApplication.translate("janela", u"0", None))
        self.L_valor_receita.setText(QCoreApplication.translate("janela", u"0", None))
        self.PB_fechar.setText(QCoreApplication.translate("janela", u"X", None))
        self.PB_minimizar.setText(QCoreApplication.translate("janela", u"-", None))
        self.label_7.setText("")
        self.label_despesas.setText(QCoreApplication.translate("janela", u"Despesas", None))
        self.L_valor_despesas.setText(QCoreApplication.translate("janela", u"0", None))
        self.L_link_git.setText(QCoreApplication.translate("janela", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Vi-n1\"><span style=\" font-size:36pt; text-decoration: underline; color:#511595;\">Criad   por VI-N1</span></a></p></body></html>", None))
        self.label.setText("")
        self.LE_valor_receita.setInputMask(QCoreApplication.translate("janela", u"99999999999", None))
        self.LE_valor_receita.setPlaceholderText(QCoreApplication.translate("janela", u"Ex:5.000,00", None))
        self.label_descricao.setText(QCoreApplication.translate("janela", u"Descri\u00e7\u00e3o:", None))
        self.TE_descricao_receita.setPlaceholderText(QCoreApplication.translate("janela", u"Ex:Receita", None))
        self.label_valor.setText(QCoreApplication.translate("janela", u"Valor:", None))
        self.label_data.setText(QCoreApplication.translate("janela", u"Data:", None))
        self.label_categoria.setText(QCoreApplication.translate("janela", u"Categoria:", None))
        self.CB_salario_receita.setItemText(0, QCoreApplication.translate("janela", u"Sal\u00e1rio", None))
        self.CB_salario_receita.setItemText(1, QCoreApplication.translate("janela", u"Comiss\u00e3o", None))
        self.CB_salario_receita.setItemText(2, QCoreApplication.translate("janela", u"Investimentos", None))

        self.CB_tipo_receita.setItemText(0, QCoreApplication.translate("janela", u"Recebida", None))
        self.CB_tipo_receita.setItemText(1, QCoreApplication.translate("janela", u"Recorrente", None))

        self.label_adicionar_receita.setText(QCoreApplication.translate("janela", u"Adicionar Receitas", None))
        self.PB_adicionar_valores_receita.setText(QCoreApplication.translate("janela", u"Adicionar", None))
        self.LE_valor_despesa.setInputMask(QCoreApplication.translate("janela", u"99999999999[", None))
        self.LE_valor_despesa.setPlaceholderText(QCoreApplication.translate("janela", u"Ex:5.000,00", None))
        self.label_despesas_valor.setText(QCoreApplication.translate("janela", u"Valor:", None))
        self.label_despesas_categoria.setText(QCoreApplication.translate("janela", u"Categoria:", None))
        self.CB_salario_despesa.setItemText(0, QCoreApplication.translate("janela", u"Transporte", None))
        self.CB_salario_despesa.setItemText(1, QCoreApplication.translate("janela", u"Aluguel", None))
        self.CB_salario_despesa.setItemText(2, QCoreApplication.translate("janela", u"Sa\u00fade", None))
        self.CB_salario_despesa.setItemText(3, QCoreApplication.translate("janela", u"Impostos", None))

        self.label_despesas_data.setText(QCoreApplication.translate("janela", u"Data:", None))
        self.label_adicionar_despesas.setText(QCoreApplication.translate("janela", u"Adicionar Despesas", None))
        self.TE_descricao_despesa.setPlaceholderText(QCoreApplication.translate("janela", u"Ex:Receita", None))
        self.label_despesas_descricao.setText(QCoreApplication.translate("janela", u"Descri\u00e7\u00e3o:", None))
        self.PB_adicionar_valores_despesa.setText(QCoreApplication.translate("janela", u"Adicionar", None))
        self.PB_adicionar_receitas.setText(QCoreApplication.translate("janela", u"Receitas", None))
        self.L_foto_usuario.setText(QCoreApplication.translate("janela", u"Adicionar foto", None))
        self.PB_adicionar_despesas.setText(QCoreApplication.translate("janela", u"Depesas", None))
        self.PB_nova_foto_usuario.setText(QCoreApplication.translate("janela", u"+", None))
        self.PB_plt_graficos.setText(QCoreApplication.translate("janela", u"Mostrar gr\u00e1ficos", None))
        self.l_plt_evolucao_gastos.setText("")
        self.l_plt_evolucao_ganhos.setText("")
        self.l_plt_ganhos.setText("")
        self.l_plt_gastos.setText("")
        self.label_5.setText("")
        self.PB_fechar_graficos.setText(QCoreApplication.translate("janela", u"X", None))
        self.PB_plt_externo_ganhos.setText(QCoreApplication.translate("janela", u"+", None))
        self.PB_plt_externo_evl_ganhos.setText(QCoreApplication.translate("janela", u"+", None))
        self.PB_plt_externo_evl_gastos.setText(QCoreApplication.translate("janela", u"+", None))
        self.PB_plt_externo_gastos.setText(QCoreApplication.translate("janela", u"+", None))
    # retranslateUi

