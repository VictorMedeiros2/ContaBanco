class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def gerar_extrato(self):
        print(f'Numero: {self.numero} \n Cpf: {self.cpf} \n Nome do Titular: {self.nomeTitular} \n Saldo: {self.saldo}')


def main():
    c1 = Conta(123489, 18432839475, "Victor", 1001)
    c1.depositar(1000)  # Chamando metodo depositar para c1(cliente 1)
    c1.gerar_extrato()  # Chamando metodo que mostra o extrato
    c1.sacar(500)  # Chamando metodo de sacar para c1
    c1.gerar_extrato()  # Chamando metodo que mostra o extrato


if __name__ == "__main__":
    main()