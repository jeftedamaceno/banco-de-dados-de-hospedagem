from classes.cliente import Cliente, ClienteVip
from classes.pousada import Pousada
from classes.condominio import Condominio

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    tipo = input("O cliente é VIP? (s/n): ").strip().lower()

    if tipo == "s":
        return ClienteVip(nome)
    else:
        return Cliente(nome)

def escolher_hospedagem(hospedagens, tipo_hospedagem):
    """Exibe opções e permite ao usuário escolher uma hospedagem."""
    print(f"\nEscolha um {tipo_hospedagem}:")
    for i, hospedagem in enumerate(hospedagens):
        print(f"{i} - {hospedagem.nome} ({hospedagem.localizacao})")

    while True:
        escolha = input(f"Digite o número do {tipo_hospedagem} desejado: ").strip()
        if escolha.isdigit() and 0 <= int(escolha) < len(hospedagens):
            return hospedagens[int(escolha)]
        print("Opção inválida! Tente novamente.")

def menu():
    print("\n=== Sistema de Hospedagem ===")
    
    cliente = criar_cliente()
    print(f"Cliente {cliente.nome} criado com sucesso!\n")

    pousadas = [
        Pousada("Pousada Beira-Mar", "Praia de Icaraizinho", 200, 5),
        Pousada("Pousada Sol Nascente", "Jericoacoara", 250, 3)
    ]
    
    condominios = [
        Condominio("D'Vera", "Rua Felipe Sampaio 208, Itapajé, CE", 1500, [10, 5, 3]),
        Condominio("Condomínio Atlântico", "Fortaleza, CE", 2000, [8, 6, 4])
    ]

    while True:
        print("\nMenu:")
        print("1 - Calcular preço em uma pousada")
        print("2 - Fazer check-in em uma pousada")
        print("3 - Fazer check-out em uma pousada")
        print("4 - Fazer check-in em um condomínio")
        print("5 - Fazer check-out em um condomínio")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            pousada = escolher_hospedagem(pousadas, "pousada")
            noites = int(input("Quantas noites deseja ficar? "))
            print(pousada.calcular_preco(noites, cliente))

        elif escolha == "2":
            pousada = escolher_hospedagem(pousadas, "pousada")
            print(pousada.hospedar(cliente))

        elif escolha == "3":
            pousada = escolher_hospedagem(pousadas, "pousada")
            print(pousada.deixar_hospedagem(cliente))

        elif escolha == "4":
            condominio = escolher_hospedagem(condominios, "condomínio")
            tipo = int(input("Escolha um tipo (0: Standard, 1: Luxo, 2: Suíte): "))
            print(condominio.hospedar(cliente, tipo))

        elif escolha == "5":
            condominio = escolher_hospedagem(condominios, "condomínio")
            print(condominio.deixar_hospedagem(cliente))

        elif escolha == "6":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
