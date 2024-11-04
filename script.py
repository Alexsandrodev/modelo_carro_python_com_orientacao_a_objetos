class Carro:

    def __init__(self, marca, modelo, ano, cor):

        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._gasolina = 0
        self._limite_gasolina = 10
        self._km_por_litro = 13.3

        self._estado = "parado"

        if self._ano <=0:
            raise "O ano do carro não pode ser negativo"
    

    def __str__(self):
        return f"carro: {self._marca}, {self._modelo}, {self._cor}, {self._ano}"
    
    @property   
    def km_por_litro(self):
        return self._km_por_litro

    @km_por_litro.setter
    def set_km_por_litro(self, novo_consumo):
        if novo_consumo > 0:
            self._km_por_litro = novo_consumo
        else:
            raise ValueError("O consumo por litro deve ser positivo.")

    def calcular_autonomia(self):
        return self._gasolina * self._km_por_litro


    def mostrar_tanque(self):
        """ Retorna uma string com o a quantidade de litros de gaslina no carro.

        Returns:
            String com a quantidade de litros de gasolina.
        """
        return f'O tanque tem {self._gasolina}L de gasolina.'
    

    def abastecer(self, valor):
        """ Abastece o tanque do carro com o valor informado pelo usuário, mas esse valor não ultrapassa o valor maximo que o tanque suporta.

        Args:
            valor: Valor no qual o usuário deseja abastecer o tanque do carro  

        Returns:
            
        """

        print("Abastecendo o carro")

        if self._gasolina == self._limite_gasolina:
            print("O tanque esta cheio")

            return
        
        if valor <= self._limite_gasolina:
            if valor + self._gasolina >= self._limite_gasolina:
                quantidade_a_abastecer  = self._limite_gasolina - self._gasolina
                tanque = self._gasolina

                self._gasolina += quantidade_a_abastecer
                print(f"O tanque já tinha {tanque}L de gasolinda, e foi completado com {quantidade_a_abastecer}L")
        
                return
        self._gasolina += valor
        print(f"Foram postos {valor}L de gasolina")

      
    def acelerar(self):      
        """ simula a ação do carro andar de acordo com a quantidade de km's que o usuário informa, e já subtrai de acordo com o km informado a quantidade de gasolina usada. 

        Rises:
            Error: se de km informado não for um valor númerico o programa retorna um erro.
        """
        pode_rodar = self._km_por_litro * self._gasolina
       
        if self._gasolina == 0:
            print('O tanque está vasio, abasteça para poder andar.')
            return

        km = input("Por quantos Km's você deseja dirigir? ")

        try:
            km = float(km)

        except:
            raise "Valor do km invalido"
        

        print(pode_rodar)

        if km > pode_rodar:
            km_faltante =  km - pode_rodar 

            print(f"O carro rodou por {km} Km's, e parou faltando {km_faltante} km's do destino...  ")

            self._gasolina = 0
            return
        
        self._estado = "andando"
        km_restante = pode_rodar - km

        aux = f"{km_restante / self._km_por_litro:.2f}"
        self._gasolina = aux

        self._estado = "parado"
        
        print(f"O carro andou por {km} km's")


    def ferar(self):
        """
        Simula a ação de friar o carro. Não é possivel friar caso o carro esteje andando  
        """
        if self._estado == "parado":
            print("O carro já está parado")
            return
        
        self._estado = "parado"
        print("O carro freiou")
