from AluguelPatins import AluguelPatins
from Cliente import Cliente

def main():
    loja = AluguelPatins()
    cliente = Cliente()
    
    while True:
        print("""
        ====== Loja de Aluguel de Patins ======
        1. Exibir patins disponíveis
        2. Requisitar patins por hora   -R$5,00
        3. Requisitar patins por dia    -R$20,00
        4. Requisitar patins por semana -R$60,00
        5. Devolver patins
        6. Sair
        """)

        escolha = input("Escolha uma opção: ")

        try:
            escolha = int(escolha)
        except ValueError:
            print("Atenção! Digite o número da opção escolhida!")
            continue

        if escolha == 1:
            loja.mostrarEstoque()
        elif escolha == 2:
            cliente.solicitarCPF()
            cliente.horaDoAluguel = loja.alugarPatinsDeHoraEmHora(cliente.pedirPatins())
            cliente.baseAluguel = 1
            cliente.salvar()
        elif escolha == 3:
            cliente.solicitarCPF()
            cliente.horaDoAluguel = loja.alugarPatinsDiariamente(cliente.pedirPatins())
            cliente.baseAluguel = 2
            cliente.salvar()
        elif escolha == 4:
            cliente.solicitarCPF()
            cliente.horaDoAluguel = loja.alugarPatinsSemanalmente(cliente.pedirPatins())
            cliente.baseAluguel = 3
            cliente.salvar()
        elif escolha == 5:
            cliente.solicitarCPF()
            cliente.calculo = loja.devolverPatins(cliente.devolverPatins())
            cliente.baseAluguel, cliente.horaDoAluguel, cliente.patins = 0,0,0
            cliente.confirmarDevolucao()
        elif escolha == 6:
            break
        else:
            print("Entrada inválida! Por favor, entre com uma opção de 1 a 6")
    print("Obrigado por usar o sistema de aluguel de patins")

if __name__=="__main__":
    main()

