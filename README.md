# Automação de Testes Web com Python e Selenium

## 📌 Sobre o projeto

Este projeto tem como objetivo desenvolver uma automação de testes de software Web utilizando **Python e Selenium WebDriver**.

O projeto foi criado como parte dos estudos de **Automação de Testes**, com foco na aplicação prática de conceitos utilizados no processo de **Quality Assurance (QA)**.

Nesta primeira etapa, será automatizado o fluxo básico de **login de um usuário**, contemplando:

* Acesso à página de login;
* Preenchimento do campo de usuário/login;
* Preenchimento do campo de senha;
* Clique no botão **Entrar**;
* Validação do resultado do login.

## 🎯 Objetivo

O principal objetivo é praticar a criação e execução de testes automatizados utilizando Python, desenvolvendo gradualmente uma estrutura de automação organizada e reutilizável.

Durante a evolução do projeto, serão aplicados conceitos como:

* Automação de testes Web;
* Selenium WebDriver;
* Python;
* Pytest;
* Assertions;
* Explicit Wait;
* Page Object Model (POM);
* Organização de código;
* Boas práticas de automação;
* Execução e análise dos testes.

## 🧪 Cenário inicial

### Login com credenciais válidas

**Pré-condição:**
O usuário deve possuir credenciais válidas para acesso ao sistema.

**Passos:**

1. Acessar a página de login;
2. Informar o usuário;
3. Informar a senha;
4. Clicar no botão **Entrar**;
5. Verificar se o acesso foi realizado com sucesso.

**Resultado esperado:**

O sistema deve autenticar o usuário e direcioná-lo para a área interna da aplicação.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Selenium WebDriver**
* **Pytest** *(em evolução)*
* **Git / GitHub**
* **Google Chrome**

## 📂 Estrutura do projeto

A estrutura inicial do projeto será organizada da seguinte forma:

```text
automacao-web-python/
│
├── tests/
│   └── test_login.py
│
├── pages/
│   └── login_page.py
│
├── venv/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Evolução do projeto

Este projeto será desenvolvido de forma incremental. Após a implementação do cenário de login, novos cenários e funcionalidades de automação serão adicionados.

Entre as próximas etapas estão:

* [ ] Criar automação do login;
* [ ] Implementar validações com `assert`;
* [ ] Utilizar `WebDriverWait`;
* [ ] Implementar Page Object Model;
* [ ] Integrar Pytest;
* [ ] Criar cenário de login inválido;
* [ ] Criar cenários de validação de mensagens de erro;
* [ ] Melhorar a organização do projeto;
* [ ] Implementar geração de evidências;
* [ ] Criar relatórios de execução.

## 📚 Objetivo de aprendizado

Além da automação do fluxo de login, este projeto busca demonstrar a evolução do conhecimento em **automação de testes de software**, desde um script simples até uma estrutura mais próxima de um projeto profissional de QA Automation.

---

**Projeto desenvolvido para fins de estudo e prática em automação de testes Web com Python.**
