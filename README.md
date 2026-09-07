# 🤖 Automação de Testes Web com Python e Selenium

Projeto de estudo e evolução em **Quality Assurance (QA)**, desenvolvido com **Python + Selenium WebDriver**, com foco na automação de testes funcionais em aplicações web.

O projeto tem como objetivo simular uma estrutura utilizada em um ambiente profissional de QA, incorporando gradualmente conceitos de **automação, organização de cenários, evidências, logs, relatórios e execução automatizada**.

> 🚧 **Projeto em evolução:** novas funcionalidades, melhorias de arquitetura e práticas de automação serão incorporadas continuamente.

---

## 🎯 Objetivo

Desenvolver uma estrutura de automação de testes web capaz de:

* Automatizar cenários funcionais;
* Validar comportamentos de aplicações web;
* Organizar cenários de teste utilizando BDD;
* Registrar evidências das execuções;
* Gerar logs técnicos;
* Gerar relatórios de execução em PDF;
* Manter evidências e relatórios separados por execução;
* Evoluir posteriormente para execução via pipeline CI/CD.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Selenium WebDriver**
* **Chrome / ChromeDriver**
* **Pytest** — em evolução
* **Git / GitHub**
* **ReportLab**
* **BDD / Gherkin**
* **VS Code**

---

## 📁 Estrutura atual do projeto

```text
Estudo_Automacao_Python/
│
├── .venv/
│
├── tests/
│   └── teste_login.py
│
├── cenarios/
│   └── CT-LOGIN-001.md
│
├── evidencias/
│   └── <ID_EXECUCAO>/
│       ├── 01_pagina_login.png
│       ├── 02_usuario_preenchido.png
│       ├── 03_senha_preenchida.png
│       └── erro_login.png
│
├── logs/
│   └── <ID_EXECUCAO>/
│       └── teste_login.log
│
├── reports/
│   └── <ID_EXECUCAO>/
│       └── relatorio_<ID_EXECUCAO>.pdf
│
├── utils/
│   ├── __init__.py
│   ├── evidencia.py
│   ├── logger.py
│   └── relatorio_pdf.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧪 Cenário automatizado

### CT-LOGIN-001 — Login com credenciais válidas

O primeiro cenário automatizado do projeto tem como objetivo validar o fluxo de login de uma aplicação web.

Fluxo:

```gherkin
Feature: Login

Scenario: Login com credenciais válidas

Given que estou na página de login
When informo um usuário válido
And informo uma senha válida
And clico no botão "Entrar"
Then devo ser autenticado com sucesso
```

O cenário é mantido em um arquivo externo dentro da pasta:

```text
cenarios/
```

Essa separação permite que os cenários de teste permaneçam independentes da implementação da automação.

---

# 📸 Evidências de teste

Durante a execução, o Selenium realiza capturas de tela em pontos importantes do cenário.

Exemplo:

```text
evidencias/
└── 2026-09-07_18-30-15/
    ├── 01_pagina_login.png
    ├── 02_usuario_preenchido.png
    ├── 03_senha_preenchida.png
    └── erro_login.png
```

Cada execução possui sua própria pasta.

Dessa forma, uma nova execução **não sobrescreve as evidências de execuções anteriores**.

---

# 📝 Logs

Cada execução também gera um arquivo de log contendo informações sobre o comportamento do teste.

Exemplo:

```text
logs/
└── 2026-09-07_18-30-15/
    └── teste_login.log
```

Os logs registram informações como:

* Início da execução;
* Acesso à página;
* Preenchimento do usuário;
* Preenchimento da senha;
* Ações realizadas;
* Erros encontrados;
* Encerramento do navegador;
* Finalização do teste.

---

# 📄 Relatório PDF

Ao final da execução é gerado automaticamente um relatório em PDF.

O relatório reúne informações da execução, incluindo:

* Identificação da execução;
* Cenário BDD;
* Ambiente;
* Status do teste;
* Evidências capturadas;
* Logs;
* Resultado da execução.

Exemplo:

```text
reports/
└── 2026-09-07_18-30-15/
    └── relatorio_2026-09-07_18-30-15.pdf
```

A geração do relatório ocorre mesmo quando o teste apresenta uma falha, permitindo manter o histórico da execução para análise.

---

# 🆔 Identificação das execuções

Cada execução recebe um identificador baseado em data e horário:

```text
YYYY-MM-DD_HH-MM-SS
```

Exemplo:

```text
2026-09-07_18-30-15
```

Esse identificador é utilizado para organizar:

```text
Evidências
     ↓
Logs
     ↓
Relatório PDF
```

Isso permite relacionar todos os artefatos pertencentes à mesma execução.

---

# 🔎 Tratamento de falhas

O projeto também está sendo estruturado para registrar informações quando ocorre uma falha durante a execução.

Em caso de erro:

1. O Selenium registra a exceção;
2. Uma evidência da tela é capturada;
3. O erro é registrado no log;
4. O teste é marcado como `FAIL`;
5. O relatório PDF é gerado;
6. A exceção é propagada para que futuramente o pipeline consiga identificar a falha.

Exemplo de status:

```text
PASS
```

ou

```text
FAIL
```

---

# ▶️ Executando o projeto

Primeiro, ativar o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Depois, executar o teste a partir da raiz do projeto:

```powershell
python -m tests.teste_login
```

Após a execução, os artefatos serão organizados automaticamente nas pastas:

```text
evidencias/
logs/
reports/
```

---

# 📦 Dependências

As dependências utilizadas pelo projeto estão relacionadas no arquivo:

```text
requirements.txt
```

Para instalar as dependências:

```powershell
pip install -r requirements.txt
```

---

# 🔐 Segurança

Informações sensíveis, como credenciais de acesso, não devem ser armazenadas diretamente no código ou no repositório.

Como próxima evolução, as credenciais serão retiradas do código e armazenadas por meio de **variáveis de ambiente** ou arquivo `.env`, devidamente protegido pelo `.gitignore`.

---

# 🚀 Roadmap

O projeto está sendo desenvolvido de forma incremental.

### ✅ Concluído

* [x] Configuração do ambiente Python
* [x] Configuração do Selenium WebDriver
* [x] Primeiro cenário de login
* [x] Estruturação dos testes
* [x] Cenário BDD externo
* [x] Captura de evidências
* [x] Identificação única por execução
* [x] Separação das evidências por execução
* [x] Implementação de logs
* [x] Separação dos logs por execução
* [x] Geração automática de relatório PDF
* [x] Inclusão do cenário BDD no relatório
* [x] Inclusão das evidências no relatório
* [x] Inclusão dos logs no relatório
* [x] Tratamento de execução com sucesso ou falha

### 🔄 Em evolução

* [ ] Melhorar o layout visual do relatório PDF
* [ ] Migrar a execução para Pytest
* [ ] Implementar assertions
* [ ] Criar novos cenários de teste
* [ ] Criar testes negativos
* [ ] Implementar Page Object Model (POM)
* [ ] Melhorar gerenciamento de waits
* [ ] Implementar configuração por ambiente
* [ ] Implementar gerenciamento seguro de credenciais
* [ ] Criar massa de dados de teste
* [ ] Estruturar testes parametrizados

### 🔮 Próximas etapas

* [ ] Estruturar suíte de testes
* [ ] Criar execução via linha de comando
* [ ] Integrar GitHub Actions
* [ ] Executar testes automaticamente em pipeline CI/CD
* [ ] Publicar evidências como artefatos da pipeline
* [ ] Incorporar informações de build/branch/commit aos relatórios
* [ ] Automatizar geração de relatórios
* [ ] Enviar relatório automaticamente para stakeholders
* [ ] Expandir cobertura de testes
* [ ] Evoluir a arquitetura do framework de automação

---

# 📊 Evolução planejada

A ideia é transformar este projeto gradualmente de uma automação simples de estudo em uma estrutura mais próxima de um **framework de automação de testes utilizado em projetos reais**.

A evolução planejada segue aproximadamente:

```text
Teste Selenium
      ↓
Organização dos testes
      ↓
BDD
      ↓
Evidências
      ↓
Logs
      ↓
Relatórios
      ↓
Pytest
      ↓
Page Object Model
      ↓
Massa de dados
      ↓
Execução automatizada
      ↓
CI/CD
      ↓
Relatórios da Pipeline
      ↓
Notificação de resultados
```

---

# 📚 Objetivo de aprendizado

Este projeto também funciona como laboratório prático para desenvolvimento de conhecimentos em:

* Automação de testes;
* Selenium WebDriver;
* Python para QA;
* BDD;
* Pytest;
* Estruturação de frameworks;
* Tratamento de exceções;
* Evidências de teste;
* Logs;
* Relatórios;
* Git e GitHub;
* CI/CD;
* Boas práticas de QA.

---

## 👨‍💻 Projeto em desenvolvimento

Este é um projeto de estudo contínuo.

Novos cenários, ferramentas, boas práticas e melhorias de arquitetura serão adicionados conforme a evolução dos conhecimentos em **QA, automação de testes e engenharia de qualidade de software**.

**Status atual:** 🚧 Em evolução

**Próxima evolução:** melhoria visual do relatório PDF e migração da execução para **Pytest**.
