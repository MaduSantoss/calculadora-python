print("-----Calculadora Simples!-----")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        operacao = input("Digite a operação (+, -, *, /): ")
        
        if operacao == '+':
            resultado = num1 + num2
            print(f"O resultado é: {resultado}")
            
        elif operacao == '-':
            resultado = num1 - num2
            print(f"O resultado é: {resultado}")
            
        elif operacao == '*':
            resultado = num1 * num2
            print(f"O resultado é: {resultado}")
            
        elif operacao == '/':
            resultado = num1 / num2
            print(f"O resultado é: {resultado}")
            
        else:
            print("Erro: Operação inválida. Por favor, escolha entre +, -, * ou /.")
            

    except ValueError:
        print("Erro: Você digitou um valor que não é um número.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir um número por zero.")


    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower() 
    if continuar != 's':
        break


print("-" * 30)
print("Calculadora encerrada.")