class Registro:
    def __init__(self, nome, carga, valor):
        self.nome = nome
        self.carga = carga
        self.valor = valor

    def calcular_salario(self):
        return self.carga * self.valor

def coletar_dados():
    while True:
        nome = input("Coloque seu nome: ")
        carga = int(input("Coloque sua carga horária: "))  
        valor = float(input("Coloque o valor do horário: "))

        finalizar = input("Deseja finalizar? S/N ").upper()  
        if finalizar == 'S':
            break
    
    registro = Registro(nome, carga, valor)
    
    print(f"\nNome: {registro.nome}, Carga Horária: {registro.carga}, Valor por hora: {registro.valor}")
    print(f"Salário calculado: {registro.calcular_salario()}")      
    return registro

registro_criado = coletar_dados()
