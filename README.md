# 🔐 AuthSystem

Sistema simples de cadastro e login feito em Python com SQLite, rodando no terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Projeto de estudo](https://img.shields.io/badge/projeto-de%20estudo-blue)

---

## ✨ O que ele faz

- Cadastra usuários (nome, e-mail e senha)
- Gera uma senha segura automaticamente, se a pessoa quiser
- Faz login com e-mail e senha
- Depois do login, mostra o e-mail e permite trocar a senha
- Permite redefinir a senha pela opção "Esqueci a senha"

## 🚀 Como rodar

Precisa só do Python 3 instalado. Não é preciso instalar mais nada.

```bash
python "Projetos/AuthSystem.py"
```

O banco de dados (`authsystem.db`) é criado sozinho na primeira vez.

## 📋 Menu

| Opção | Ação |
|:-----:|------|
| **1** | Logar |
| **2** | Cadastrar |
| **3** | Esqueci a senha |
| **4** | Logout (encerra o programa) |

## 🖥️ Exemplo de uso

```
escolha uma das opçoes abaixo:
1- Logar
2- Cadastrar
3- Esqueci a senha
4- Logout
Digite o numero da opçao desejada: 1
Digite seu e-mail: joao@teste.com
Digite sua senha: minhasenha123
Login realizado com sucesso!
Bem-vindo, Joao Silva!

--- Minha conta ---
E-mail: joao@teste.com
1 - Trocar senha
2 - Sair da conta
```

## ✅ Regras do cadastro

- Nome e sobrenome
- E-mail válido (com `@` e `.`, sem espaços) e que ainda não esteja cadastrado
- Senha com no mínimo 8 caracteres

## 🧠 Competências praticadas

- Laços (`while`) e condicionais (`if`, `elif`, `else`)
- Entrada e saída de dados (`input` e `print`)
- Manipulação de textos (`strip`, `split`)
- Validação de dados digitados pelo usuário
- Tratamento de erros com `try` e `except`
- Banco de dados SQLite: `CREATE TABLE`, `INSERT`, `SELECT` e `UPDATE`
- Consultas parametrizadas (`?`), que evitam SQL injection
- Geração de senhas com o módulo `secrets`
- Versionamento com Git e GitHub

## ⚠️ Observação

As senhas ficam salvas em texto puro no banco. Por ser um projeto de estudo, isso foi mantido simples, mas num sistema real o ideal é guardar a senha com hash.
