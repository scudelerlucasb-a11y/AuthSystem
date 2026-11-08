import secrets
import string
import sqlite3

conexao = sqlite3.connect("../authsystem.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

conexao.commit()


letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*."


opcao1 = "1- Logar"
opcao2 = "2- Cadastrar"
opcao3 = "3- Esqueci a senha"
opcao4 = "4- Logout"

while True:
    print("escolha uma das opçoes abaixo: ")
    print(opcao1)
    print(opcao2)
    print(opcao3)
    print(opcao4)

    resposta = int(input("Digite o numero da opçao desejada: "))

    if resposta == 1:
        email_login = input("Digite seu e-mail: ")
        senha_login = input("Digite sua senha: ")
        cursor.execute(
            "SELECT * FROM usuarios WHERE email = ? AND senha = ?",
            (email_login, senha_login)
        )
        usuario = cursor.fetchone()

        if usuario:
            print("Login realizado com sucesso!")
            print("Bem-vindo,", usuario[1] + "!")

            while True:
                print("\n--- Minha conta ---")
                print("E-mail:", email_login)
                print("1 - Trocar senha")
                print("2 - Sair da conta")

                opcao_conta = int(input("Digite o número da opção desejada: "))

                if opcao_conta == 1:
                    nova = input("Digite a nova senha (mínimo 8 caracteres): ")
                    if len(nova) >= 8:
                        cursor.execute(
                            "UPDATE usuarios SET senha = ? WHERE email = ?",
                            (nova, email_login)
                        )
                        conexao.commit()
                        print("Senha alterada com sucesso!")
                    else:
                        print("A senha deve ter no mínimo 8 caracteres.")

                elif opcao_conta == 2:
                    print("Você saiu da sua conta.\n")
                    break

                else:
                    print("Opção inválida!")
        else:
            print("E-mail ou senha incorretos!")


    elif resposta == 2:
        nome = input("\nDigite seu nome completo: ").strip()
        email = input("Digite seu email: ").strip()

        if len(nome.split()) < 2:
            print("Digite seu nome e sobrenome.")
        elif "@" not in email or "." not in email or " " in email:
            print("E-mail inválido!")
        else:
            print("Deseja gerar uma senha segura automaticamente?")
            print("1 - Sim")
            print("2 - Não, quero criar minha própria senha")
            digite = int(input("Digite o número desejado: "))
            if digite == 1:
                caracteres = string.ascii_letters + string.digits + "!@#$%^&*."
                senha = ''.join(secrets.choice(caracteres) for _ in range(12))
                print("Sua senha gerada foi:", senha)
            elif digite == 2:
                senha = input("Digite sua senha (mínimo 8 caracteres): ")
            else:
                print("Opção inválida!")
                continue
            if len(senha) >= 8:
                try:
                    cursor.execute(
                        "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                        (nome, email, senha)
                    )
                    conexao.commit()
                    print("Conta criada com sucesso!")
                except sqlite3.IntegrityError:
                    print("Este e-mail já está cadastrado!")
            else:
                print("A senha deve ter no mínimo 8 caracteres.")



    elif resposta == 3:
        valor = input("Digite o email para atualizar a senha: ")
        cursor.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (valor,)
        )
        usuario = cursor.fetchone()
        if usuario:
            nova = input("Digite a nova senha: ")
            if len(nova) >= 8:
                cursor.execute(
                    "UPDATE usuarios SET senha = ? WHERE email = ?",
                    (nova, valor)
                )
                conexao.commit()
                print("Senha atualizada com sucesso!")
            else:
                print("A senha deve ter no mínimo 8 caracteres.")
        else:
            print("E-mail não encontrado. Verifique se possui cadastro.")

    elif resposta == 4:
        print("Logout. Até mais!")
        break
conexao.close()