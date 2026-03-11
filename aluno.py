# Lista de caracteres especiais que não podem aparecer no nome
caracteres_especiais = "!@#$%&*()-_=+[];:,.?/"

# Função para verificar se a quantidade de alunos é válida
def verificar_quantidade(quantidade_alunos):
    if quantidade_alunos < 2:
        print("Quantidade de alunos deve ser maior ou igual a 10 tente novamente mais tarde.")
        print("O Sistema será encerrado e terá que rodar o sistema novamente.")

        return False


# Função para verificar se o nome do aluno é válido
def verificar_nome(nome):
    if nome in caracteres_especiais or nome.isdigit():
        print("Nome inválido! O nome deve conter apenas letras.")
        print("O Sistema será encerrado e terá que rodar o sistema novamente.")

        return False

# Função para verificar se a nota é válida
def verificar_nota(nota):
    if nota < 0 or nota > 10:
        print("Nota inválida! Deve ser entre 0 e 10.")
        print("O Sistema será encerrado e terá que rodar o sistema novamente.")

        return False


# Função para calcular a média das 3 notas
def calcular_media(lista):
    media = (lista[0] + lista[1] + lista[2]) / 3
    return media


# Função que define a situação do aluno baseado na média
def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# Pede ao usuário a quantidade de alunos
quantidade_alunos = int(input("Digite a quantidade de alunos: "))

verificar_quantidade(quantidade_alunos)

lista_alunos = []

# Repete para cada aluno
for i in range(quantidade_alunos):

    print(f"\nAluno {i + 1}:")
    nome = input("Digite o nome do aluno: ")

# Verifica se tem caracteres especiais no nome

    if verificar_nome(nome) == False:
        break

    lista = []

    # Repete para pedir 3 notas
    for j in range(3):

        nota = float(input(f"Digite a nota {j + 1}: "))

        if verificar_nota(nota) == False:
            break

        lista.append(nota)

    # Calcula a média
    media = calcular_media(lista)

    # Define situação
    situacao = situacao_aluno(media)

    # Guarda os dados do aluno
    lista_alunos.append([nome, lista[0], lista[1], lista[2], media, situacao])

print("\nQuantidade total de alunos:", len(lista_alunos))

# Mostra resultados
for aluno in lista_alunos:

    print("Aluno:", aluno[0])
    print("Nota 1:", aluno[1])
    print("Nota 2:", aluno[2])
    print("Nota 3:", aluno[3])
    print("Média:", aluno[4])
    print("Situação:", aluno[5])
    print()

    print(50 * "_")