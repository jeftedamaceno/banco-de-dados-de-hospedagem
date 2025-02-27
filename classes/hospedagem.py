class Hospedagem:
    def __init__(self, nome, localizacao, preco_base, total_quartos):
        self.nome = nome
        self.localizacao = localizacao
        self.preco_base = preco_base
        self.total_quartos = total_quartos
        self.quartos_disponiveis = total_quartos
        self.hospedes = {}

    def hospedar(self, cliente):
        """Realiza o check-in do cliente na hospedagem."""
        if self.quartos_disponiveis <= 0:
            return "Este hotel está lotado."

        self.quartos_disponiveis -= 1
        cliente.numero_de_check_in += 1
        self.hospedes[cliente.nome] = cliente  # Armazena o objeto cliente
        return f"Check-in realizado com sucesso! Bem-vindo, {cliente.nome}."

    def deixar_hospedagem(self, cliente):
        """Realiza o check-out do cliente."""
        if cliente.nome in self.hospedes:
            self.quartos_disponiveis += 1
            del self.hospedes[cliente.nome]  # Remove o cliente da lista de hóspedes
            return f"Obrigado por visitar, {cliente.nome}!"
        return "Cliente não encontrado."

    def calcular_preco(self, num_noites, cliente):
        """Calcula o preço total da hospedagem com desconto aplicado."""
        if num_noites <= 0:
            return "Número de noites inválido."

        valor_total = num_noites * self.preco_base
        valor_com_desconto = cliente.calcular_desconto(valor_total)

        return (f"O valor do aluguel é R${valor_com_desconto:.2f}, "
                f"com desconto de R${valor_total - valor_com_desconto:.2f} aplicado.")

    def __str__(self):
        return (f"{self.nome} - Localização: {self.localizacao}\n"
                f"Preço Base: R${self.preco_base:.2f}\n"
                f"Quartos Disponíveis: {self.quartos_disponiveis}/{self.total_quartos}\n"
                f"Hóspedes Atuais: {', '.join(self.hospedes.keys()) if self.hospedes else 'Nenhum'}")
