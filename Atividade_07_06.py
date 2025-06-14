from abc import ABC, abstractmethod

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")

    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")

    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque. Estoque atual: {self.estoque}")

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} unidades vendidas. Estoque atual: {self.estoque}")
        else:
            print(f"Erro: estoque insuficiente. Estoque disponível: {self.estoque}")

class ProdutoNacional(Produto):
    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def preco_final(self):
        return self.preco + (self.preco * self.taxa_importacao)

    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa de {self.taxa_importacao * 100:.0f}% aplicada.")

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora



