from Bomba import Bomba

b1 = Bomba('gasolina', 4, 5.50)

print(f'Combustível: {b1.tipo_combustivel}')

b1.abastecerPreco(150)
b1.abastecerLitro(22.35)

b1.alterarCombustivel('álcool')

b1.abastecerPreco(150)
b1.abastecerLitro(22.35)
