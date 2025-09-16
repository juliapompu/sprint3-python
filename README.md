# Rede Social do Futebol Feminino

## Integrantes do Grupo

- Eduardo Duran RM:562017
- Henrique Castro RM:564560
- Fernando Bellegarde RM:564169
- Giovana Parreira RM:562275
- Julia Pompeu RM:561955

---

## Descrição do Projeto

Este projeto é uma aplicação de terminal em Python que simula uma rede social voltada para o futebol feminino. Usuárias podem criar contas, postar vídeos, curtir, comentar, visualizar perfis e interagir com outros membros da comunidade. O sistema utiliza arquivos JSON para persistência dos dados de usuários, vídeos e interações.

## Funcionalidades

- **Cadastro e Login de Usuário**: Criação de conta com email, senha, nome de usuário, nome real, tipo (jogadora ou torcedora) e biografia.
- **Postagem de Vídeos**: Usuárias podem postar vídeos com título, descrição e link. Cada vídeo recebe um identificador único (UUID).
- **Feed de Vídeos**: Visualização de todos os vídeos postados, com informações de autor, curtidas, visualizações e comentários.
- **Curtir Vídeos**: Usuárias podem curtir vídeos. O sistema impede múltiplas curtidas do mesmo usuário no mesmo vídeo.
- **Comentar em Vídeos**: Usuárias podem comentar nos vídeos. Os comentários são associados ao id do usuário e do vídeo.
- **Visualização de Perfis**: É possível visualizar o próprio perfil e o perfil de autoras dos vídeos.
- **Edição de Perfil**: Alteração de nome de usuário, nome real, biografia e senha.
- **Persistência de Dados**: Todos os dados são salvos em arquivos JSON (`usuarios.json`, `videos.json`, `curtidas.json`).

## Estrutura dos Arquivos

- `app.py`: Código principal da aplicação.
- `usuarios.json`: Armazena os dados das usuárias cadastradas.
- `videos.json`: Armazena os vídeos postados.
- `curtidas.json`: Armazena registros de curtidas e comentários.
- `README.md`: Este arquivo de documentação.

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone ou baixe o repositório.
3. No terminal, navegue até a pasta do projeto.
4. Execute o comando:

```bash
python app.py
```

5. Siga as instruções exibidas no terminal para criar uma conta, postar vídeos e interagir.

## Exemplo de Uso

- Crie uma conta informando email, senha, nome de usuário, nome real, tipo e biografia.
- Faça login com seu email e senha.
- No menu principal, escolha postar um vídeo, ver vídeos, curtir, comentar ou editar seu perfil.
- Visualize perfis de outras usuárias a partir do feed de vídeos.

## Tecnologias Utilizadas

- Python 3
- Bibliotecas padrão: `json`, `os`, `uuid`, `time`, `re`

## Observações Técnicas

- Cada usuário e vídeo possui um campo `id` único (UUID) para garantir integridade nas buscas e interações.
- O sistema é totalmente baseado em terminal e não possui interface gráfica.
- Os dados são persistidos localmente em arquivos JSON.
- O código está preparado para fácil expansão de funcionalidades.

Projeto desenvolvido para fins acadêmicos, promovendo a valorização do futebol feminino e o aprendizado de programação em Python.
