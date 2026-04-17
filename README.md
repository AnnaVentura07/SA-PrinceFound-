# Prince Found — Gestão de Cosméticos

Este sistema foi desenvolvido como uma **Situação de Aprendizagem (SA)** para consolidar conceitos de desenvolvimento Full Stack. A aplicação é focada no gerenciamento de estoque para o setor de cosméticos, unindo uma interface web funcional a uma API robusta construída com Django.

## Critérios Atendidos

* **CRUD Completo**: Controle total de produtos, permitindo cadastrar, listar, editar e excluir registros do sistema.
* **Gestão de Estoque**: Monitoramento de quantidades, validades e localização física dos itens.
* **Segurança de Dados**: Proteção de rotas sensíveis através de decoradores de autenticação, garantindo que apenas usuários logados gerenciem o catálogo.
* **Arquitetura de API**: Implementação de endpoints REST para integração e serialização de dados em formato JSON.
* **Automação de Dados**: O sistema realiza o autopreenchimento das categorias de cosméticos (Skincare, Maquiagem, etc.) na primeira execução.

## Tecnologias Utilizadas

* **Linguagem**: Python 3.x.
* **Framework**: Django (Web) e Django REST Framework (API).
* **Banco de Dados**: SQLite (Desenvolvimento).
* **Padrão de Projeto**: MVC (Model-View-Controller) / MVT (Model-View-Template).

## Como Executar o Projeto

### 1. Clonar o Repositório
Abra o seu terminal e clone o projeto da pasta raiz:
```bash
git clone [[https://github.com/AnnaVentura07/SA-PrinceFound.git](https://github.com/AnnaVentura07/SA-PrinceFound.git)](https://github.com/AnnaVentura07/SA-PrinceFound/tree/main)
cd SA-PrinceFound
2. Configurar o Ambiente Virtual
No Windows:
Bash
python -m venv venv
venv\Scripts\activate
No Linux / macOS:
Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar Dependências
Bash
pip install django djangorestframework
4. Preparar o Banco de Dados
Bash
python manage.py migrate
5. Criar Acesso Administrativo
Para acessar o Dashboard e o painel Admin, é necessário criar um usuário:

Bash
python manage.py createsuperuser
6. Rodar o Servidor
Bash
python manage.py runserver
Acesse a aplicação em: http://127.0.0.1:8000/

Principais Rotas
Login: /accounts/login/ (Ponto de entrada para autenticação).

Dashboard: /dashboard/ (Painel principal de gestão de produtos).

Dicas: /dicas/ (Área de conteúdo e orientações ao usuário).

API: /api/ (Acesso aos dados serializados via REST).

Admin: /admin/ (Gerenciamento de banco de dados nativo do Django).

Desenvolvido por: Anna Luisa dos Santos Ventura
Projeto Acadêmico: Situação de Aprendizagem (SA).

