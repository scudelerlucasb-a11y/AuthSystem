AuthSystem

Sistema simples de cadastro e login feito em Python com SQLite, rodando no terminal. É um projeto de estudo.

O que ele faz
Cadastra usuários (nome, e-mail e senha)
Gera uma senha segura automaticamente, se a pessoa quiser
Faz login com e-mail e senha
Depois do login, mostra o e-mail e permite trocar a senha
Permite redefinir a senha pela opção "Esqueci a senha"
Como rodar

Precisa só do Python 3 instalado. Não precisa instalar mais nada.

bash
python "Projetos/AuthSystem.py"

O banco de dados (authsystem.db) é criado sozinho na primeira vez.

Menu
1- Logar
2- Cadastrar
3- Esqueci a senha
4- Logout
Regras do cadastro
Nome e sobrenome
E-mail válido (com @ e ., sem espaços) e que ainda não esteja cadastrado
Senha com no mínimo 8 caracteres
