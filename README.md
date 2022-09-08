![Logo](https://i.imgur.com/cI3icML.png)

# PFC Tech-Blog

Este é um projeto de conclusão de curso sobre um blog de tecnologia

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

### Backend

    pip install -r requirements.txt

    python ./manage.py makemigrations contas
    python ./manage.py makemigrations postagens
    python ./manage.py migrate
    python ./manage.py createsuperuser
    ./manage.py runserver

## Tecnologias Usadas

**FrontEnd:** HTML, CSS, TailwindCSS

**Backend:** Python, Django

## Criado por

- [wesley wilson](https://github.com/wesleywil)
