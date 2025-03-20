# Solicita ao usuário que digite seu nome
while True:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        # Verifica se o nome é composto apenas de espaços
        elif nome.isspace():
            raise ValueError("O nome não deve ser composto apenas de espaços.")
        else:
            print("Nome válido:", nome)
            break
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while True:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
            continue
        break
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while True:
    try:
        bonus = float(input("Digite o valor do bônus: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
            continue
        break
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

# Calcula o bônus final
bonus_recebido = 1000 + salario * bonus

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_recebido:.2f}.")