![Logo](https://i.imgur.com/cI3icML.png)

# PFC Tech-Blog

Este é um projeto de conclusão de curso sobre um blog de tecnologia

## Screenshots

![Homepage](https://i.imgur.com/mZFKLhn.png)

### Login

![Login](https://i.imgur.com/6g0xoph.png)

### Registro

![Registro](https://i.imgur.com/y2wktIp.png)

## Características

- Listar Postagens
- Listar Categorias
- Listar Postagens por Categoria
- Criar Postagens
- Criar Categorias
- Editar Postagens
- Editar Categorias
- Criar Conta
- Logar na Conta
- Ver Perfil
- Editar Perfil
- Editar Senha

## Rodando o Projeto

### Criando Ambiente Virtual & Comandos necessarios

    python -m venv env
    env\scripts\activate
    pip install -r requirements.txt

    python manage.py makemigrations contas
    python manage.py makemigrations postagens
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

## Tecnologias Usadas

**FrontEnd:** HTML, CSS, TailwindCSS

**Backend:** Python, Django

## Created By

- [wesley wilson](https://github.com/wesleywil)
