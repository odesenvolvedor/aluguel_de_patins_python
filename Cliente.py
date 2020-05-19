from connection.Model import Model
import datetime

class Cliente(Model):
    def __init__(self):
        super().__init__('cliente')
        self.cpf = ''
        self.patins = 0
        self.baseAluguel = 0
        self.horaDoAluguel = 0
        self.calculo = 0

        self.createTable()

    def createTable(self):
        sql = """
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                patins INTEGER NOT NULL,
                baseAluguel INTEGER NOT NULL,
                cpf varchar(20),
                horaDoAluguel datetime not null,
                calculo decimal(11,2),
                devolvido integer default(0)
            );
        """
        super().createTable(sql)

    def solicitarCPF(self):
        """
        Solicita ao cliente o número do CPF.
        """ 
        self.cpf = input("Digite o número do CPF do cliente: ")
        return self.cpf

    def pedirPatins(self):
        """
        Solicita ao cliente o número de par de patins.
        """ 

        patins = input("Quantos pares de patins você gostaria de alugar? ")
        try:
            patins = int(patins)
        except ValueError:
            print("Esse não é um número inteiro positivo!")
            return -1
        if patins < 1:
            print("Entrada inválida. O número de patins deve ser maior que zero!")
        else:
            self.patins = patins
        return self.patins

    def devolverPatins(self):
        """
        Permite que os clientes devolvam seus patins à locadora.
        """

        self.select = 'baseAluguel, horaDoAluguel, patins'
        self.where = f"devolvido = 0 AND cpf = '{self.cpf}'"
        result = self.get()

        for (baseAluguel, horaDoAluguel, patins) in result:
            self.baseAluguel = baseAluguel
            self.horaDoAluguel = datetime.datetime.strptime(horaDoAluguel, '%Y-%m-%d %H:%M:%S.%f')
            self.patins = patins

        if self.baseAluguel and self.horaDoAluguel and self.patins:
            return self.horaDoAluguel, self.baseAluguel, self.patins
        else:
            return 0,0,0

    def salvar(self):
        sql = f"""
            INSERT INTO {self._table} (cpf, patins, baseAluguel, horaDoAluguel)
            values
            ('{self.cpf}', {self.patins}, {self.baseAluguel}, '{self.horaDoAluguel}');
        """
        super().post(sql)

    def retornarPatinsAlugados(self) :
        self.select = "SUM(patins) as total_alugado"
        self.where = "devolvido = 0"
        return self.get()

    def confirmarDevolucao(self):
        if (self.calculo):
            sql = f"""
                UPDATE {self._table} SET devolvido = 1, calculo = {self.calculo}
                WHERE cpf = '{self.cpf}'
            """
            super().post(sql)