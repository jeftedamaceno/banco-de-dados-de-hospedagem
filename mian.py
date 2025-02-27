from classes.cliente import Cliente, ClienteVip
from classes.condominio import Condominio
from classes.hospedagem import Hospedagem
from classes.pousada import Pousada

def main():
    # Criando clientes
    joao = Cliente("João")
    joao.numero_de_check_in = 5
    silas = Cliente("Silas")
    silas.numero_de_check_in = 10
    maria = ClienteVip("Maria")
    maria.numero_de_check_in = 15

    # Criando a pousada
    pousada_beira_mar = Pousada('Pousada Beira Mar', 'Praia de Icaraizinho', 200, 1)

    # Exibindo preço antes do check-in
    print(pousada_beira_mar.calcular_preco(10, maria))
    print(pousada_beira_mar.hospedar(maria))
    print(pousada_beira_mar.deixar_hospedagem(maria))

    print(pousada_beira_mar.calcular_preco(10, joao))
    print(pousada_beira_mar.hospedar(joao))

    print(pousada_beira_mar.calcular_preco(3, silas))
    print(pousada_beira_mar.hospedar(silas))  # Este deve falhar, pois só há 1 quarto

    # Criando um condomínio
    dvera = Condominio('DVera', 'Rua Felipe Sampaio 208, Itapajé, CE, 62600-000', 1500, [10, 5, 3])

    # Escolha do tipo de quarto
    tipo = int(input("Escolha um tipo de quarto (0 para Standard, 1 para Luxo, 2 para Suíte): "))

    print(dvera.hospedar(silas, tipo))

if __name__ == "__main__":
    main()
