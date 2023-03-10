class Bomba:
    def __init__(self, tipo_combustivel:str, valor_litro_alcool:float=0, valor_litro_gaso:float=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro_alcool = valor_litro_alcool
        self.valor_litro_gaso = valor_litro_gaso


    def abastecerPreco(self, valor):
        if self.tipo_combustivel == 'álcool':
            litros = valor/self.valor_litro_alcool
            print(f'Abasteceu {litros:.2f} litros de {self.tipo_combustivel} por R${valor}.')
        else:
            litros = valor/self.valor_litro_gaso
            print(f'Abasteceu {litros:.2f} litros de {self.tipo_combustivel} por R${valor}.')

    def abastecerLitro(self, quantidade):
        if self.tipo_combustivel == 'álcool':
            preco = quantidade * self.valor_litro_alcool
            print(f'Abasteceu {quantidade:.2f} litros de {self.tipo_combustivel} por R${preco:.2f}.')
        if self.tipo_combustivel == 'gasolina':
            preco = quantidade * self.valor_litro_gaso
            print(f'Abasteceu {quantidade:.2f} litros de {self.tipo_combustivel} por R${preco:.2f}.')
        
    def alterarValor(self):
        novoValor = float(input('Qual o valor do litro: '))
        self.valor_litro = novoValor

    def alterarCombustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
        print(f'Tipo de combustível alterado para {tipo_combustivel}.')
