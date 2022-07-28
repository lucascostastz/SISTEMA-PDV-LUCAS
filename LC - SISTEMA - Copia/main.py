from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPixmap
import sqlite3
from tkinter import filedialog, messagebox
from PyQt6 import uic, QtWidgets
from reportlab.pdfgen import canvas
import time
import sqlite3


class Iniciar:
    app = QtWidgets.QApplication([])
    tela_login = uic.loadUi("./interfaces/login.ui")
    tela_inicio = uic.loadUi("./interfaces/main.ui")
    cadastro_clientes = uic.loadUi("./interfaces/cadastro_clientes.ui")
    cadastro_produtos = uic.loadUi("./interfaces/cadastro_produtos.ui")
    cadastro_usuarios = uic.loadUi("./interfaces/cadastro_usuarios.ui")
    editar_produtos = uic.loadUi("./interfaces/editar_produtos.ui")
    editar_clientes = uic.loadUi("./interfaces/editar_clientes.ui")
    alerta_pdf = uic.loadUi("./interfaces/alerta_salvar_pdf.ui")
    alerta_prod_cadastrado = uic.loadUi("./interfaces/alerta_cad_produtos.ui")
    alerta_prod_editado = uic.loadUi("./interfaces/alerta_prod_editar.ui")
    alerta_pesquisa_produto = uic.loadUi("./interfaces/alerta_pesquisa_produto.ui")
    alerta_pesquisa_cliente = uic.loadUi("./interfaces/alerta_pesquisa_cliente.ui")
    alerta_cliente_cadastrado = uic.loadUi(
        "./interfaces/alerta_cad_clientes.ui")
    fundo_login = tela_login.label_5.setPixmap(
        QPixmap("icones\imagem"))
    fundo_inicio = tela_inicio.label.setPixmap(
        QPixmap("icones\lcsistemas"))


def entrar():

    Iniciar.tela_login.label.setText("")
    user_1 = Iniciar.tela_login.lineEdit_3.text()
    senha = Iniciar.tela_login.lineEdit_4.text()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute(
        "SELECT senha FROM usuarios WHERE login ='{}'".format(user_1))
    senha_db = cursor.fetchall()
    bc.close()
    try:
        if senha == senha_db[0][0]:
            Iniciar.tela_login.lineEdit_3.setText("")
            Iniciar.tela_login.lineEdit_4.setText("")
            start() 
            Iniciar.tela_login.close()
            Iniciar.tela_inicio.show()
    except:
        Iniciar.tela_login.label_3.setText("Dados de login incorretos!")
    else:
        Iniciar.tela_login.label_3.setText("Dados de login incorretos!")


def start():
    Iniciar.tela_login.label_3.setText("")
    carregando = Iniciar.tela_login.label.setText("Carregando...")
    print(carregando)
    Iniciar.tela_login.my_progressBar.show()
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(10)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(20)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(30)
    time.sleep(0.5)
    aguarde = Iniciar.tela_login.label.setText("Aguarde...")
    print(aguarde)
    Iniciar.tela_login.my_progressBar.setValue(40)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(50)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(60)
    time.sleep(0.5)
    iniciando = Iniciar.tela_login.label.setText("Iniciando o sistema...")
    print(iniciando)
    Iniciar.tela_login.my_progressBar.setValue(70)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.setValue(80)
    time.sleep(0.3)
    Iniciar.tela_login.my_progressBar.setValue(90)
    time.sleep(0.1)
    Iniciar.tela_login.my_progressBar.setValue(100)
    time.sleep(0.5)
    Iniciar.tela_login.my_progressBar.close()


def chama_inicio():
    Iniciar.tela_inicio.show()
    Iniciar.tela_usuarios.close()


def lista_produtos():
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("SELECT * FROM produtos")
    dados_lidos = cursor.fetchall()
    Iniciar.tela_inicio.tableWidget_3.setRowCount(len(dados_lidos))
    Iniciar.tela_inicio.tableWidget_3.setColumnCount(10)
    for a in range(0, len(dados_lidos)):
        for b in range(0, 10):
            Iniciar.tela_inicio.tableWidget_3.setItem(
                a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
    bc.commit()


def Pesquisar_produtos():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    valor_consulta =""
    valor_consulta = Iniciar.tela_inicio.tx_BuscaProdutos.text()

    lista = cursor.execute(f"SELECT * FROM produtos where descricao like '%{valor_consulta}%' or codigo like'%{valor_consulta}%'")
    lista = list(lista)
    if not lista:
        return  Iniciar.alerta_pesquisa_produto.show()
        
    else:   
        Iniciar.tela_inicio.tableWidget_3.setRowCount(0)
        #primeiro for trás
        for idxLinha, linha in enumerate(lista):
            Iniciar.tela_inicio.tableWidget_3.insertRow(idxLinha)
            for idxColuna, coluna in enumerate(linha):
                Iniciar.tela_inicio.tableWidget_3.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
Pesquisar_produtos()


def salvar_lista_produtos_pdf():
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    comando = "SELECT * FROM produtos"
    cursor.execute(comando)
    dados_lidos = cursor.fetchall()
    bc.commit()
    y = 0
    x = 80
    conteudo = filedialog.asksaveasfilename(mode="w")
    pdf = canvas.Canvas(conteudo)
    pdf.setFont("Times-Bold", 16)
    pdf.drawString(200, 800, "PRODUTOS CADASTRADOS")
    pdf.setFont("Times-Bold", 9)
    pdf.drawString(5, 750, "ID")
    pdf.drawString(25, 750, "CÓDIGO")
    pdf.drawString(70, 750, "DESCRIÇÃO")
    pdf.drawString(180, 750, "PREÇO")
    pdf.drawString(220, 750, "CATEGORIA")
    pdf.drawString(300, 750, "ESTOQUE")
    pdf.drawString(390, 750, "MARCA")
    pdf.drawString(460, 750, "OBSERVAÇÃO")
    for i in range(0, len(dados_lidos)):
        y = y + 30
        x = x
        pdf.drawString(5, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(30, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(70, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(180, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(220, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(300, 750 - y, str(dados_lidos[i][5]))
        pdf.drawString(390, 750 - y, str(dados_lidos[i][6]))
        pdf.drawString(460, 750 - y, str(dados_lidos[i][9]))
    chama_alerta_pdf()


def inserir_produtos():
    descricao = Iniciar.cadastro_produtos.tx_DescricaoProduto.text()
    categoria = Iniciar.cadastro_produtos.cb_CategoriaProduto.currentText()
    marca = Iniciar.cadastro_produtos.tx_AddMarca.text()
    estoque = Iniciar.cadastro_produtos.tx_EstoqueMinimoProduto.text()
    codigo = Iniciar.cadastro_produtos.tx_EstoqueMaximoProduto.text()
    observacao = Iniciar.cadastro_produtos.tx_ObsProduto.text()
    preco = Iniciar.cadastro_produtos.tx_ValorCompraProduto.text()
    v_varejo = Iniciar.cadastro_produtos.tx_ValorUnitarioProduto.text()
    v_atacado = Iniciar.cadastro_produtos.tx_ValorAtacadoProduto.text()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("INSERT INTO produtos (codigo,descricao,preco,categoria,estoque,marca,observacao,v_varejo,v_atacado) VALUES('" +
                   codigo+"','"+descricao+"','"+preco+"','"+categoria+"','"+estoque+"','"+marca+"','"+observacao+"','"+v_varejo+"','"+v_atacado+"')")
    bc.commit()
    bc.close()
    chama_lerta_prod_cad()
    lista_produtos()


def inserir_img():
    conteudo = filedialog.askopenfilename()
    Iniciar.cadastro_produtos.lb_FotoProduto.setPixmap(QPixmap(conteudo))
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("INSERT INTO produtos (imagem) VALUES('"+conteudo+"')")
    bc.commit()

def editar_produtos():
    global numero_id
    linha = Iniciar.tela_inicio.tableWidget_3.currentRow()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()

    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id=" + str(valor_id))
    produto = cursor.fetchall()
    Iniciar.editar_produtos.show()
    numero_id = valor_id
    Iniciar.editar_produtos.tx_DescricaoProduto.setText(str(produto[0][2]))
    Iniciar.editar_produtos.tx_AddCategoria.setText(str(produto[0][4]))
    Iniciar.editar_produtos.tx_AddMarca.setText(str(produto[0][6]))
    Iniciar.editar_produtos.tx_EstoqueMinimoProduto.setText(str(produto[0][5]))
    Iniciar.editar_produtos.tx_Codigo.setText(str(produto[0][1]))
    Iniciar.editar_produtos.tx_Preco.setText(str(produto[0][3]))
    Iniciar.editar_produtos.tx_ValorUnitarioProduto.setText(str(produto[0][7]))
    Iniciar.editar_produtos.tx_ValorAtacadoProduto.setText(str(produto[0][8]))
    Iniciar.editar_produtos.tx_ObsProduto.setText(str(produto[0][9]))


def salvar_produto_editados():
    # Pega o numero id
    global numero_id
    # Valor digitado no lineEdit
    codigo = Iniciar.editar_produtos.tx_Codigo.text()
    descricao = Iniciar.editar_produtos.tx_DescricaoProduto.text()
    preco = Iniciar.editar_produtos.tx_Preco.text()
    categoria = Iniciar.editar_produtos.tx_AddCategoria.text()
    estoque = Iniciar.editar_produtos.tx_EstoqueMinimoProduto.text()
    marca = Iniciar.editar_produtos.tx_AddMarca.text()
    v_varejo = Iniciar.editar_produtos.tx_ValorUnitarioProduto.text()
    v_atacado = Iniciar.editar_produtos.tx_ValorAtacadoProduto.text()
    observacao = Iniciar.editar_produtos.tx_ObsProduto.text()
    # Atualizar os dados no banco
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria ='{}', estoque = '{}', marca = '{}', v_varejo = '{}', v_atacado = '{}', observacao = '{}' WHERE id = {}".format(
        codigo, descricao, preco, categoria, estoque, marca, v_varejo, v_atacado, observacao, numero_id))
    bc.commit()
    Iniciar.editar_produtos.close()
    lista_produtos()




def excluir_produtos():
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    linha = Iniciar.tela_inicio.tableWidget_3.currentRow()
    Iniciar.tela_inicio.tableWidget_3.removeRow(linha)
###Remover no banco###
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id =" + str(valor_id))
    bc.commit()


############ CLIENTES ############
def inserir_clientes():
    nome = Iniciar.cadastro_clientes.tx_NomeFantasia.text()
    rg = Iniciar.cadastro_clientes.tx_InscEstadual.text()
    cpf = Iniciar.cadastro_clientes.tx_cnpj.text()
    telefone = Iniciar.cadastro_clientes.tx_Telefone.text()
    email = Iniciar.cadastro_clientes.tx_Email.text()
    cep = Iniciar.cadastro_clientes.tx_Cep.text()
    endereco = Iniciar.cadastro_clientes.tx_Endereco.text()
    numero = Iniciar.cadastro_clientes.tx_Numero.text()
    bairro = Iniciar.cadastro_clientes.tx_Bairro.text()
    cidade = Iniciar.cadastro_clientes.tx_Cidade.text()
    estado = Iniciar.cadastro_clientes.tx_Estado.text()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("INSERT INTO clientes (nome,rg,cpf,telefone,email,cep,endereco,numero,bairro,cidade,estado) VALUES('" +
                   nome+"','"+rg+"','"+cpf+"','"+telefone+"','"+email+"','"+cep+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+estado+"')")
    bc.commit()
    bc.close()
    chama_alerta_cdst_clientes()
    lista_clientes()


def editar_clientes():
    global numero_id
    linha = Iniciar.tela_inicio.tableWidget_2.currentRow()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("SELECT id FROM clientes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM clientes WHERE id=" + str(valor_id))
    cliente = cursor.fetchall()
    Iniciar.editar_clientes.show()
    numero_id = valor_id
    Iniciar.editar_clientes.tx_NomeFantasia.setText(str(cliente[0][1]))
    Iniciar.editar_clientes.tx_InscEstadual.setText(str(cliente[0][2]))
    Iniciar.editar_clientes.tx_cnpj.setText(str(cliente[0][3]))
    Iniciar.editar_clientes.tx_Telefone.setText(str(cliente[0][4]))
    Iniciar.editar_clientes.tx_Email.setText(str(cliente[0][5]))
    Iniciar.editar_clientes.tx_Cep.setText(str(cliente[0][6]))
    Iniciar.editar_clientes.tx_Endereco.setText(str(cliente[0][7]))
    Iniciar.editar_clientes.tx_Numero.setText(str(cliente[0][8]))
    Iniciar.editar_clientes.tx_Bairro.setText(str(cliente[0][9]))
    Iniciar.editar_clientes.tx_Cidade.setText(str(cliente[0][10]))
    Iniciar.editar_clientes.tx_Estado.setText(str(cliente[0][11]))


def salvar_cliente_editado():
    # Pega o numero id
    global numero_id
    # Valor digitado no lineEdit
    nome = Iniciar.editar_clientes.tx_NomeFantasia.text()
    rg = Iniciar.editar_clientes.tx_InscEstadual.text()
    cpf = Iniciar.editar_clientes.tx_cnpj.text()
    telefone = Iniciar.editar_clientes.tx_Telefone.text()
    email = Iniciar.editar_clientes.tx_Email.text()
    cep = Iniciar.editar_clientes.tx_Cep.text()
    endereco = Iniciar.editar_clientes.tx_Endereco.text()
    numero = Iniciar.editar_clientes.tx_Numero.text()
    bairro = Iniciar.editar_clientes.tx_Bairro.text()
    cidade = Iniciar.editar_clientes.tx_Cidade.text()
    estado = Iniciar.editar_clientes.tx_Estado.text()
    # Atualizar os dados no banco
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("UPDATE clientes SET nome = '{}', rg = '{}', cpf = '{}', telefone ='{}', email = '{}', cep = '{}', endereco = '{}', numero = '{}', bairro = '{}', cidade = '{}', estado = '{}' WHERE id = {}".format(
        nome, rg, cpf, telefone, email, cep, endereco, numero, bairro, cidade, estado, numero_id))
    bc.commit()
    Iniciar.editar_clientes.close()
    lista_clientes()


def lista_clientes():
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados_lidosc = cursor.fetchall()
    Iniciar.tela_inicio.tableWidget_2.setRowCount(len(dados_lidosc))
    Iniciar.tela_inicio.tableWidget_2.setColumnCount(12)
    for a in range(0, len(dados_lidosc)):
        for b in range(0, 12):
            Iniciar.tela_inicio.tableWidget_2.setItem(
                a, b, QtWidgets.QTableWidgetItem(str(dados_lidosc[a][b])))
    bc.commit()


def Pesquisar_clientes():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    valor_consulta =""
    valor_consulta = Iniciar.tela_inicio.tx_BuscaClientes.text()
    lista = cursor.execute(f"SELECT * FROM clientes where nome like '%{valor_consulta}%' or cpf like'%{valor_consulta}%'")
    lista = list(lista)
    if not lista:
        return  Iniciar.alerta_pesquisa_cliente.show()
        
    else:   
        Iniciar.tela_inicio.tableWidget_2.setRowCount(0)
        #primeiro for trás
        for idxLinha, linha in enumerate(lista):
            Iniciar.tela_inicio.tableWidget_2.insertRow(idxLinha)
            for idxColuna, coluna in enumerate(linha):
                Iniciar.tela_inicio.tableWidget_2.setItem(idxLinha, idxColuna, QtWidgets.QTableWidgetItem(str(coluna)))
Pesquisar_clientes()


def excluir_clientes():
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()
    linha = Iniciar.tela_inicio.tableWidget_2.currentRow()
    Iniciar.tela_inicio.tableWidget_2.removeRow(linha)
    cursor.execute("SELECT id FROM clientes")
    dados_lidosce = cursor.fetchall()
    valor_id = dados_lidosce[linha][0]
    cursor.execute("DELETE FROM clientes WHERE id =" + str(valor_id))
    bc.commit()


def sair_alerta_cad_clientes():
    Iniciar.alerta_cliente_cadastrado.close()
    Iniciar.cadastro_clientes.tx_NomeFantasia.clear()
    Iniciar.cadastro_clientes.tx_cnpj.clear()
    Iniciar.cadastro_clientes.tx_InscEstadual.clear()
    Iniciar.cadastro_clientes.tx_Telefone.clear()
    Iniciar.cadastro_clientes.tx_Email.clear()
    Iniciar.cadastro_clientes.tx_Cep.clear()
    Iniciar.cadastro_clientes.tx_Endereco.clear()
    Iniciar.cadastro_clientes.tx_Numero.clear()
    Iniciar.cadastro_clientes.tx_Bairro.clear()
    Iniciar.cadastro_clientes.tx_Cidade.clear()
    Iniciar.cadastro_clientes.tx_Estado.clear()


def sair_login():
    Iniciar.tela_login.close()

def password_check():      
    bt=Iniciar.tela_login.sender()
    if bt.isChecked() == True:
        Iniciar.tela_login.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    else:    
        Iniciar.tela_login.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


def Pesquisar_produtos_venda():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    valor_consulta =""
    valor_consulta = Iniciar.tela_inicio.Pesquisar_Produto.text()   
    lista = cursor.execute(f"SELECT codigo, descricao, preco  FROM produtos where codigo like '%{valor_consulta}%' or descricao like '%{valor_consulta}%'")   
    lista = list(lista)
    if not lista:
        return  chama_alerta_pesquisa.show()     
    else:   
        Iniciar.tela_inicio.tableWidget_4.setRowCount(len(lista))
        Iniciar.tela_inicio.tableWidget_4.setColumnCount(5)
    for a in range(0, len(lista)):
        for b in range(0,3):
            Iniciar.tela_inicio.tableWidget_4.setItem(
                a, b, QtWidgets.QTableWidgetItem(str(lista[a][b])))
Pesquisar_produtos()


def inserir_preco():
    global numero_id
    linha = Iniciar.tela_inicio.tableWidget_4.currentRow()
    bc = sqlite3.connect('banco.db')
    cursor = bc.cursor()

    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id=" + str(valor_id))
    produto = cursor.fetchall()
    numero_id = valor_id
    Iniciar.tela_inicio.Valor_Unit.setText(str(produto[0][3]))


def somar():
    try:
        sub_total = float(Iniciar.tela_inicio.LB_Total.text())
       
        dinheiro = float(Iniciar.tela_inicio.Pagamento.text())
        b = float(dinheiro-int(sub_total))
        Iniciar.tela_inicio.Valor_Troco.setText(str(f'{b:.2f}'))
    except:
        return
        

def chama_alerta_prod_editar():
    Iniciar.alerta_prod_editado.show()

def sair_alerta_prod_editar():
    Iniciar.alerta_prod_editado.close()

def chama_lerta_prod_cad():
    Iniciar.alerta_prod_cadastrado.show()

def sair_alerta_prod_cad():
    Iniciar.alerta_prod_cadastrado.close()

def chama_alerta_pdf():
    Iniciar.alerta_pdf.show()

def sair_alerta_pdf_produtos():
    Iniciar.alerta_pdf.close()

def chama_alerta_cdst_clientes():
    Iniciar.alerta_cliente_cadastrado.show()

def sair_cad_produto():
    Iniciar.cadastro_produtos.close()

def sair_edit_produto():
    Iniciar.editar_produtos.close()

def sair_cad_clientes():
    Iniciar.cadastro_clientes.close()

def sair_edit_clientes():
    Iniciar.editar_clientes.close()

def chama_alerta_pesquisa():
    Iniciar.alerta_pesquisa_produto.show()

def sair_alerta_pesquisap():
    Iniciar.alerta_pesquisa_produto.close()

def sair_alerta_pesquisac():
    Iniciar.alerta_pesquisa_cliente.close()


def main():
    ############### Iniciar HOME ###############
    Iniciar.tela_inicio.Pagamento.textChanged.connect(somar)
    Iniciar.tela_inicio.pushButton.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.inicio))
    Iniciar.tela_inicio.pushButton.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.inicio))

    Iniciar.tela_inicio.pushButton_8.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.clientes))

    Iniciar.tela_inicio.pushButton_2.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.produtos))

    Iniciar.tela_inicio.pushButton_5.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.usuarios))

    Iniciar.tela_inicio.pushButton_4.clicked.connect(
        lambda: Iniciar.tela_inicio.stackedWidget.setCurrentWidget(Iniciar.tela_inicio.vendas))
    ############### PRODUTOS ###############
    Iniciar.tela_inicio.pushButton_24.clicked.connect(
        Iniciar.cadastro_produtos.show)

    Iniciar.cadastro_produtos.bt_SalvarProdutos.clicked.connect(inserir_produtos)

    Iniciar.tela_inicio.pushButton_21.clicked.connect(
        editar_produtos)

    Iniciar.editar_produtos.bt_SalvarProdutos.clicked.connect(
        salvar_produto_editados)

    Iniciar.editar_produtos.bt_CancelarProdutos.clicked.connect(sair_edit_produto)

    Iniciar.tela_inicio.pushButton_22.clicked.connect(excluir_produtos)

    Iniciar.tela_inicio.pushButton_23.clicked.connect(salvar_lista_produtos_pdf)

    Iniciar.alerta_prod_cadastrado.pushButton.clicked.connect(
        sair_alerta_prod_cad)

    Iniciar.alerta_pdf.pushButton.clicked.connect(sair_alerta_pdf_produtos)

    Iniciar.cadastro_produtos.bt_CancelarProdutos.clicked.connect(sair_cad_produto)

    Iniciar.cadastro_produtos.bt_AddImagem.clicked.connect(inserir_img)


    ############### CLIENTES ###############

    Iniciar.tela_inicio.pushButton_16.clicked.connect(
        editar_clientes)

    Iniciar.editar_clientes.bt_Salvar.clicked.connect(
        salvar_cliente_editado)

    Iniciar.cadastro_clientes.bt_Salvar.clicked.connect(inserir_clientes)

    Iniciar.tela_inicio.pushButton_17.clicked.connect(excluir_clientes)

    Iniciar.alerta_cliente_cadastrado.pushButton.clicked.connect(
        sair_alerta_cad_clientes)

    Iniciar.cadastro_clientes.bt_Voltar.clicked.connect(sair_cad_clientes)

    Iniciar.editar_clientes.bt_Voltar.clicked.connect(sair_edit_clientes)

    Iniciar.tela_inicio.pushButton_25.clicked.connect(
        Iniciar.cadastro_clientes.show)

    ############### USUÁRIOS ###############
    Iniciar.tela_inicio.pushButton_26.clicked.connect(
        Iniciar.cadastro_usuarios.show)

    Iniciar.cadastro_usuarios.bt_CancelarUsuarios.clicked.connect(
        Iniciar.cadastro_usuarios.close)

    Iniciar.tela_login.login_button_2.clicked.connect(entrar)
    Iniciar.tela_login.sair.clicked.connect(sair_login)

    ############### LOGIN ###############
    Iniciar.tela_login.checkBox_save_user.clicked.connect(password_check)
    Iniciar.tela_inicio.pesquisar_produto.clicked.connect(Pesquisar_produtos)
    Iniciar.tela_inicio.Bt_PesquisaClientes.clicked.connect(Pesquisar_clientes)
    Iniciar.tela_inicio.BT_Pequisar.clicked.connect(Pesquisar_produtos_venda)
    Iniciar.tela_inicio.Add_Produto.clicked.connect(inserir_preco)
    Iniciar.alerta_pesquisa_produto.Bt_Confirma.clicked.connect(sair_alerta_pesquisap)
    Iniciar.alerta_pesquisa_cliente.Bt_Confirma.clicked.connect(sair_alerta_pesquisac)
    Iniciar.tela_login.show()
    Iniciar.tela_login.my_progressBar.close()
    Iniciar.app.exec()


lista_clientes()
lista_produtos()
main()
