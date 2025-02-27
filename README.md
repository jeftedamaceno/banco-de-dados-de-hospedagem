# banco-de-dados-de-hospedagem
# 🏨 Sistema de Hospedagem

Este é um sistema simples de gerenciamento de hospedagem, permitindo a criação de clientes (incluindo clientes VIPs) e a interação com diferentes tipos de estabelecimentos, como pousadas e condomínios. O usuário pode calcular preços, fazer check-in e check-out de clientes.

## ✨ Funcionalidades
- Criar clientes (normais ou VIPs)
- Gerenciar múltiplas pousadas e condomínios
- Calcular preços com descontos baseados no histórico do cliente
- Realizar check-in e check-out

## 📂 Estrutura do Projeto
```
📦 sistema-hospedagem
 ┣ 📂 classes
 ┃ ┣ 📜 cliente.py
 ┃ ┣ 📜 hospedagem.py
 ┃ ┣ 📜 pousada.py
 ┃ ┗ 📜 condominio.py
 ┣ 📜 menu.py
 ┣ 📜 README.md
```

## 🚀 Instalação e Uso
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-hospedagem.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd sistema-hospedagem
   ```
3. Execute o sistema:
   ```bash
   python menu.py
   ```

## 🛠 Tecnologias Utilizadas
- Python 3+

## 📌 Exemplo de Uso
```
=== Sistema de Hospedagem ===
Digite o nome do cliente: João
O cliente é VIP? (s/n): n
Cliente João criado com sucesso!

Menu:
1 - Calcular preço em uma pousada
2 - Fazer check-in em uma pousada
3 - Fazer check-out em uma pousada
4 - Fazer check-in em um condomínio
5 - Fazer check-out em um condomínio
6 - Sair
Escolha uma opção: 1
```

## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias e novas funcionalidades. Para isso:
1. Fork o projeto
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m 'Adicionando nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request 🚀

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo! 🎉

