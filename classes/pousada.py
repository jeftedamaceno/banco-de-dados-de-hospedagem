from classes.hospedagem import Hospedagem

class Pousada(Hospedagem):
    def __init__(self, nome, localizacao, preco_base, total_quartos):
        super().__init__(nome, localizacao, preco_base, total_quartos)  # Removida redundância
    
    def calcular_preco(self, num_noites, cliente):
        """Calcula o preço total da hospedagem com desconto adicional para estadias longas."""
        if num_noites <= 0:
            return "Número de noites inválido."

        valor_total = num_noites * self.preco_base
        valor_com_desconto = cliente.calcular_desconto(valor_total)

        # Aplicar desconto adicional de 3% se for mais de 5 noites
        if num_noites > 5:
            valor_com_desconto *= 0.97
            desconto_total = 1 - (valor_com_desconto / valor_total)
        else:
            desconto_total = 1 - (valor_com_desconto / valor_total)

        return (f"O valor do aluguel é R${valor_com_desconto:.2f}, "
                f"com desconto total de {desconto_total:.2%} aplicado.")
