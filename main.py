from Atividade_07_06 import Produto, ProdutoImportado, ProdutoNacional, FuncionarioCLT, FuncionarioPJ

# Ativ1
p1 = Produto("Teclado", 100.0, 20)
p2 = ProdutoNacional("Monitor", 800.0, 10)
p3 = ProdutoImportado("Celular", 2000.0, 5, 0.15)

# Ativ2
p1.exibir_detalhes()
p2.exibir_detalhes()
p3.exibir_detalhes()

# Ativ3
print("Preço final:", p1.preco_final())
print("Preço final:", p2.preco_final())
print("Preço final:", p3.preco_final())

# Ativ4
p1.emitir_nota()
p2.emitir_nota()
p3.emitir_nota()

# Ativ5
p1.repor(10)
p1.vender(5)
p1.vender(30)  

# Atividade 6 

produtos = [
    ProdutoNacional("Monitor", 800.0, 10),
    ProdutoImportado("Notebook", 3000.0, 5, 0.2),
    Produto("Teclado", 100.0, 20)
]

funcionarios = [
    FuncionarioCLT("Maria", 3000.0),
    FuncionarioPJ("João", 160, 25.0)
]

print("\n=== DETALHES DOS PRODUTOS ===")
for p in produtos:
    p.exibir_detalhes()
    print(f"Preço final: R${p.preco_final():.2f}")
    p.emitir_nota()
    print("-" * 40)

print("\n=== PAGAMENTO DOS FUNCIONÁRIOS ===")
for f in funcionarios:
    print(f"{f.nome} receberá: R${f.calcular_pagamento():.2f}")

print("\n=== OPERAÇÕES DE ESTOQUE ===")
produto_escolhido = produtos[0]  
produto_escolhido.vender(3)
produto_escolhido.repor(5)