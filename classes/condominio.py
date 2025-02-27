from classes.hospedagem import Hospedagem

class Condominio(Hospedagem):
    def __init__(self, nome, localizacao, mensalidade, quartos_por_tipo):
        total_quartos = sum(quartos_por_tipo)
        super().__init__(nome, localizacao, preco_base=0, total_quartos=total_quartos)
        
        self.mensalidade = mensalidade  
        self.tipos_quarto = {
            0: "standard",
            1: "luxo",
            2: "suíte"
        }
        self.precos = {
            "standard": self.mensalidade,
            "luxo": self.mensalidade * 1.5,
            "suíte": self.mensalidade * 2
        }
        self.quartos_disponiveis_por_tipo = {
            "standard": quartos_por_tipo[0],
            "luxo": quartos_por_tipo[1],
            "suíte": quartos_por_tipo[2]
        }

    def hospedar(self, cliente, tipo_quarto_int, realizar_check_in=False):
        """Realiza a escolha do quarto e, opcionalmente, o check-in do cliente."""
        tipo_quarto = self.tipos_quarto.get(tipo_quarto_int)
        
        if tipo_quarto is None:
            return "Tipo de quarto inválido. Escolha entre: 0 (standard), 1 (luxo) ou 2 (suíte)."
        
        preco = self.precos[tipo_quarto]
        preco_final = self.calcular_mensalidade(preco, cliente)
        
        if realizar_check_in:
            if self.quartos_disponiveis_por_tipo[tipo_quarto] <= 0:
                return f"Não há quartos {tipo_quarto} disponíveis."
            
            self.quartos_disponiveis_por_tipo[tipo_quarto] -= 1
            cliente.numero_de_check_in += 1
            self.hospedes[cliente.nome] = cliente
            
            return (f"Check-in realizado com sucesso! Bem-vindo, {cliente.nome}.")
        
        return f"Quarto {tipo_quarto} escolhido. Preço da mensalidade: R$ {preco_final:.2f}"
    def deixar_hospedagem(self, cliente):
        """Realiza o check-out do cliente no condomínio."""
        if cliente.nome in self.hospedes:
            for tipo_quarto, ocupados in self.quartos_disponiveis_por_tipo.items():
                if ocupados < self.total_quartos and self.hospedes[cliente.nome]:
                    self.quartos_disponiveis_por_tipo[tipo_quarto] += 1
                    break
            del self.hospedes[cliente.nome]  # Remove o cliente da lista de hóspedes
            return f"Obrigado por visitar, {cliente.nome}!"
        return "Cliente não encontrado."
    def calcular_mensalidade(self, mensalidade, cliente):
        """Aplica desconto do cliente e retorna o valor final"""
        return cliente.calcular_desconto(mensalidade)
