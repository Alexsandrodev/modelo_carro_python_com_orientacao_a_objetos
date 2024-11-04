from script import Carro

meu_carro = Carro("Volkswagen", "Gol", 2020, "Vermelho")

print(meu_carro)

meu_carro.abastecer(10)
meu_carro.acelerar()

print(meu_carro.mostrar_tanque())