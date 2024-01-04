def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: divisão por zero"

def calculadora():
    while True:
        print("\nEscolha a Operação:")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. divisão")
        print("0. sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "0":
            print("Encerrando a calculadora.")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de inserir números válidos.")
            continue

        if escolha == "1":
            resultado = soma(num1, num2)
        elif escolha == "2":
            resultado = subtracao(num1, num2)
        elif escolha == "3":
            resultado = multiplicacao(num1, num2)
        elif escolha == "4":
            resultado = divisao(num1, num2)
        else:
            print("Escolha inválida. Por favor, escolha uma operação válida.")
            continue

        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()

   