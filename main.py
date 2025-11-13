import os

ARQUIVO_ESTOQUE = "estoque.txt"
ARQUIVO_RELATORIO = "relatorio.txt"

def menu():
    print("\n=== TECHWAVE DIGITAL - GESTÃO DE ESTOQUE ===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto (Nome)")
    print("4. Calcular Total de Itens (Recursivo)")
    print("5. Gerar Relatório de Fechamento")
    print("6. Sair")
    return input(">> Escolha uma opção: ").strip()

def cadastrar_produto():
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    try:
        qtd = int(input("Quantidade: ").strip())
        preco = float(input("Preço (R$): ").strip().replace(",", "."))
    except ValueError:
        print("Erro: digite números válidos.")
        return
    if qtd < 0 or preco < 0:
        print("Erro: valores negativos não permitidos.")
        return
    with open(ARQUIVO_ESTOQUE, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{qtd},{preco}\n")
    print("Produto salvo com sucesso!")

def gerar_relatorio():
    produtos = carregar_dados_do_arquivo()
    if not produtos:
        print("Nenhum dado para gerar relatório.")
        return
    total_itens = 0
    valor_total = 0.0
    with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== RELATÓRIO DE ESTOQUE TECHWAVE ===\n\n")
        for prod in produtos:
            try:
                nome = prod[0]
                qtd = int(prod[1])
                preco = float(prod[2])
            except:
                continue
            subtotal = qtd * preco
            total_itens += qtd
            valor_total += subtotal
            arquivo.write(f"{nome:<20} | QTD: {qtd:<5} | R$ {preco:.2f}\n")
        arquivo.write("\n" + "-"*40 + "\n")
        arquivo.write(f"TOTAL DE ITENS: {total_itens}\n")
        arquivo.write(f"VALOR TOTAL: R$ {valor_total:.2f}\n")
    print(f"Relatório gerado em '{ARQUIVO_RELATORIO}'")

def carregar_dados_do_arquivo():
    lista = []
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                dados = [p.strip() for p in linha.split(",")]
                if len(dados) == 3:
                    lista.append(dados)
    return lista

def listar_produtos():
    produtos = carregar_dados_do_arquivo()
    print("\n--- LISTA DE PRODUTOS ---")
    if not produtos:
        print("O estoque está vazio.")
    else:
        for p in produtos:
            try:
                preco = f"{float(p[2]):.2f}"
            except:
                preco = p[2]
            print(f"{p[0]} | Qtd: {p[1]} | R$ {preco}")

def buscar_produto():
    termo = input("\nDigite o nome para buscar: ").strip().lower()
    if not termo:
        print("Busca vazia.")
        return
    produtos = carregar_dados_do_arquivo()
    achou = False
    print(f"\nResultados para '{termo}':")
    for p in produtos:
        if termo in p[0].lower():
            try:
                preco = f"{float(p[2]):.2f}"
            except:
                preco = p[2]
            print(f"-> {p[0]} (Qtd: {p[1]} - R$ {preco})")
            achou = True
    if not achou:
        print("Nenhum produto encontrado.")

def somar_recursivo(lista, i=0):
    if i >= len(lista):
        return 0
    return lista[i] + somar_recursivo(lista, i + 1)

def exibir_total_recursivo():
    produtos = carregar_dados_do_arquivo()
    if not produtos:
        print("Estoque vazio.")
        return
    try:
        qtds = [int(p[1]) for p in produtos]
    except:
        qtds = [int(p[1]) for p in produtos if p[1].isdigit()]
    total = somar_recursivo(qtds)
    print(f"\nTotal de itens (recursivo): {total}")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            exibir_total_recursivo()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")
