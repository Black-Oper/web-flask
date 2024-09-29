# Aplicação de Gerenciamento de Tarefas com Flask

Esta é uma aplicação web desenvolvida em Python utilizando o framework Flask, com o propósito de um trabalho acadêmico. A aplicação permite a gestão de tarefas de forma simples e eficaz.

## Funcionalidades

- **Criar, editar e excluir tarefas**
- **Atribuir tarefas a outros usuários**
- **Sistema de cadastro e login**
- **Armazenamento de dados em um banco SQLite**

## Estrutura de Pastas

### `instance/`
Contém o arquivo SQLite, que armazena as informações do banco de dados.

### `static/`
Contém arquivos de estilo (CSS) e imagens utilizados na aplicação.

### `templates/`
Contém os arquivos HTML responsáveis pelas páginas da aplicação.

## Descrição dos Arquivos

### `config.py`
Arquivo responsável pela configuração geral da aplicação e sua execução.

### `criarbanco.py`
Script utilizado para criar o banco de dados a partir das classes definidas em `models.py`.

### `forms.py`
Gerencia as informações dos formulários HTML da aplicação.

### `main.py`
Contém a lógica central da aplicação e as funções que controlam o funcionamento das principais funcionalidades.

### `models.py`
Define as classes utilizadas para criar o banco de dados da aplicação.

---

Este projeto foi desenvolvido como parte de um trabalho acadêmico e utiliza tecnologias como Flask e SQLite.
