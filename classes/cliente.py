class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.numero_de_check_in = 0  # O número de check-ins define o desconto

    def obter_desconto(self):
        """Retorna a porcentagem de desconto baseada no número de check-ins."""
        if 0 < self.numero_de_check_in < 10:
            return 0.05
        elif 10 <= self.numero_de_check_in < 50:
            return 0.10
        return 0

    def calcular_desconto(self, valor):
        """Calcula o valor final aplicando o desconto."""
        desconto = self.obter_desconto()
        return valor * (1 - desconto)


class ClienteVip(Cliente):
    def obter_desconto(self):
        """Cliente VIP recebe descontos maiores."""
        desconto_padrao = super().obter_desconto()  # Obtém o desconto normal
        return desconto_padrao + 0.10  # Adiciona 10% extra para VIP
