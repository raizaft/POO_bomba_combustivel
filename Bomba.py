class Bomba:
    def __init__(self, tipo_combustivel:str, valor_litro:float=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro

    def abastecerPreco(self, valor):
        litros = valor/self.valor_litro
        print(f'Abasteceu {litros:.2f} litros por R${valor}.')

    def abastecerLitro(self, quantidade):
        preco = quantidade * self.valor_litro
        print(f'Abasteceu {quantidade:.2f} litros por R${preco:.2f}.')
        
    def alterarValor(self):
        novoValor = float(input('Qual o valor do litro: '))
        self.valor_litro = novoValor

    def alterarCombustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
        print(f'Combustível: {tipo_combustivel}.')

    def tipoCombustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
