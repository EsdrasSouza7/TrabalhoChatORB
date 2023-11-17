def calculadora():
    while True:
        # Solicitação de entrada do usuário
        expressao = input("Digite uma expressão (ou 'sair' para encerrar): ")

        # Verifica se o usuário quer sair
        if expressao.lower() == 'sair':
            print("Calculadora encerrada. Até mais!")
            break

        try:
            # Avalia a expressão e imprime o resultado
            resultado = eval(expressao)
            print("Resultado:", resultado)
        except Exception as e:
            # Se houver um erro, imprime uma mensagem de erro
            print("Erro ao calcular a expressão:", e)

# Chama a função da calculadora
calculadora()
