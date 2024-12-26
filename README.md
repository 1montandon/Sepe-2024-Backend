## Sistema de Gerenciamento para o Copão (2024) - Backend Django REST Framework

Este repositório foi criado como parte do projeto desenvolvido para a **SEPE 2024** (Semana de Ensino, Pesquisa e Extensão do IFC Araquari). O objetivo principal é oferecer uma solução digital para gerenciar o **Copão**, um campeonato esportivo interno, otimizando a experiência de alunos e organizadores.

### Recursos e Objetivos

O principal objetivo deste backend é fornecer uma API RESTful que permita a criação de um front-end completo e dinâmico para o Copão. As funcionalidades principais incluem:

* **Gerenciamento de Equipes:**
  * Criação, leitura, atualização e deleção de equipes participantes.
  * Associação de jogadores a cada equipe.
* **Gerenciamento de Jogos:**
  * Criação de partidas, definição de datas e horários.
  * Registro de resultados e estatísticas dos jogos.
  * Criação de uma tabela de classificação dinâmica.
* **Autenticação e Autorização:**
  * Implementação de mecanismos de autenticação para controlar o acesso aos recursos da API.
  * Definição de permissões para diferentes tipos de usuários (administradores e usuarios).
* **API RESTful Completa:**
  * Exposição de endpoints para todas as operações CRUD (Create, Read, Update, Delete) sobre os recursos do sistema.
  

### Tecnologias Utilizadas

* **Django REST Framework:** Framework Python para a construção de APIs RESTful, oferecendo recursos como serialização, views, autenticação e permissões.
* **Django:** Framework Python para desenvolvimento web, utilizado como base para a construção da API.
* **Sqlite**: Para armazenamento dos dados do campeonato.

## Notas
- Este projeto foi desenvolvido com foco acadêmico e pode não seguir todas as melhores práticas de desenvolvimento.
- Embora funcional, ele é voltado para fins de aprendizado e não representa uma solução comercial final.
- Este fork foi criado a partir do projeto original da [SEPE](https://github.com/LucasLiebl/pi-backend) 2024 com o objetivo de continuar o projeto e compartilhar minhas implementações.
