import datetime
from connection.Model import Model
from Cliente import Cliente

class AluguelPatins(Model):

    def __init__(self):
        super().__init__('estoque')
        self.createTable()
        self.verificaEstoque()
        self.estoque = self.mostrarEstoque()

    def createTable(self):
        sql = """
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                estoque INTEGER
            );
        """
        super().createTable(sql)

    def mostrarEstoque(self):
        """
        Exibe os patins atualmente disponíveis para aluguel na loja
        """

        self.select = 'estoque'
        result = self.get()
        estoqueTotal = 0
        estoqueDisponivel = 0
        for (estoque) in result:
            estoqueTotal = estoque[0]

        cliente = Cliente()
        result = cliente.retornarPatinsAlugados()
        
        patinsAlugados = 0
        for (patinsAlugados) in result:
            if (patinsAlugados[0] != None):
                estoqueTotal -= patinsAlugados[0]

        print(f"Atualmente, temos {estoqueTotal} patins disponíveis para aluguel" )
        return estoqueTotal

    def verificaEstoque(self):
        """ Verifica se o estoque está inserido na tabela estoque """
        self.select = 'estoque'
        result = self.get()
        """ Se não estiver inserido, solicita o usuário a inserir o estoque inicial """
        if (len(result) == 0):
            estoque = input("Digite o estoque inicial: ")
            try:
                """ Verifica se digitou um número """
                estoque = int(estoque)
            except ValueError:
                print("Esse não é um número inteiro positivo!")
                return -1
            """ Verifica se digitou um número maior que 1 """
            if estoque < 1:
                print("Entrada inválida. O número de patins deve ser maior que zero!")
            else:
                """ Monta o sql de acordo com o total que o usuario digitou """
                sql = f"""
                INSERT INTO {self._table} (estoque)
                values
                ({estoque});
                """
                """ Executa o sql para inserir o estoque no banco """
                super().post(sql)

    def alugarPatinsDeHoraEmHora(self, n):
        """
        Aluga um par de patins a cada hora para um cliente.
        """
        if n <= 0:
            print("O número de patins deve ser positivo!"
            .format(self.estoque))
            return None
        elif n > self.estoque:
            print(f"Desculpa! Atualmente temos {self.estoque} patins disponíveis para aluguel.")
            return None
        else:
            agora = datetime.datetime.now()
            print(f"Você alugou {n} patins para hoje, às {agora.hour} horas")
            print("Você será cobrado R$5,00 por cada hora, por par de patins.")
            print("Esperamos que você goste do nosso serviço.")

            self.estoque -= n
            return agora

    def alugarPatinsDiariamente(self, n):
        """
        Aluga um par de patins diariamente para um cliente.
        """
        if n <= 0:
            print("O número de patins deve ser positivo!"
            .format(self.estoque))
            return None
        elif n > self.estoque:
            print(f"Desculpa! Atualmente temos {self.estoque} patins disponíveis para aluguel.")
            return None
        else:
            agora = datetime.datetime.now()
            print(f"Você alugou {n} patins diariamente, às {agora.hour} horas")
            print("Você será cobrado R$20,00 por cada dia, por par de patins.")
            print("Esperamos que você goste do nosso serviço.")

            self.estoque -= n
            return agora

    def alugarPatinsSemanalmente(self, n):
        """
        Aluga um par de patins semanalmente para um cliente.
        """
        if n <= 0:
            print("O número de patins deve ser positivo!"
            .format(self.estoque))
            return None
        elif n > self.estoque:
            print(f"Desculpa! Atualmente temos {self.estoque} patins disponíveis para aluguel.")
            return None
        else:
            agora = datetime.datetime.now()
            print(f"Você alugou {n} patins semanalmente, às {agora.hour} horas")
            print("Você será cobrado R$60,00 por cada semana, por par de patins.")
            print("Esperamos que você goste do nosso serviço.")

            self.estoque -= n
            return agora
    def devolverPatins(self, requerimento):
        """
        1. Aceitar patins alugados de um cliente
        2. Reabastecer o inventário se é por hora, dia ou semana
        3. Devolver uma fatura, quantidade de patins alugados
        """

        horaDoAluguel, baseAluguel, numeroDePatins = requerimento
        calculo = 0

        if horaDoAluguel and baseAluguel and numeroDePatins:
            self.estoque += numeroDePatins
            agora = datetime.datetime.now()
            periodoDeAluguel = agora - horaDoAluguel

            #cálculo de fatura por hora
            if baseAluguel == 1:
                calculo = round(periodoDeAluguel.seconds / 3600) * 5 * numeroDePatins

            #cálculo de fatura por dia
            elif baseAluguel ==2:
                calculo = round(periodoDeAluguel.days) * 20 * numeroDePatins
            
            #cálculo de faturas por semana
            elif baseAluguel ==3:
                calculo = round(periodoDeAluguel.days/7) * 60 * numeroDePatins
            print(periodoDeAluguel)
            if (3<= numeroDePatins <=5):
                print(" Você está qualificado para a promoção de aluguel familiar" + "com 30% de desconto")
                calculo = calculo * 0.7

            print("Obrigado por devolver seus patins. Espero que tenha gostado do nosso serviço")
            print(f"Valor total a pagar R${calculo}")
            return calculo
        else:
            print("Tem certeza de que alugou os patins conosco? Confira os dados!")
            return None