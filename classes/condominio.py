from classes.hospedagem import Hospedagem

class Condominio(Hospedagem):
    def __init__(self, nome, localizacao, mensalidade, total_quartos):
        super().__init__(nome, localizacao, preco_base=0, total_quartos=total_quartos)
        
        self.mensalidade = mensalidade  # Mantém o conceito de mensalidade
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

    def escolher_quarto(self, tipo_int, cliente):
        """Define o tipo de quarto escolhido pelo cliente"""
        tipo = self.tipos_quarto.get(tipo_int)
        if tipo is not None:
            preco = self.precos[tipo]
            preco_final = self.calcular_mensalidade(preco, cliente)
            return f"Quarto {tipo} escolhido. Preço da mensalidade: R$ {preco_final:.2f}"
        else:
            return "Tipo de quarto inválido. Escolha entre: 0 (standard), 1 (luxo) ou 2 (suíte)."

    def calcular_mensalidade(self, mensalidade, cliente):
        """Aplica desconto do cliente e retorna o valor final"""
        return cliente.calcular_desconto(mensalidade)
