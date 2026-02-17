# Testador de URLs e APIs em Python

Esse é um projetinho em Python que eu fiz para testar URLs e endpoints de API.

A ideia é simples: caso eu precise testar várias URLs no trabalho ou validar se uma API está respondendo corretamente, eu já tenho um script pronto para isso.

---

## O que ele faz

- Testa várias URLs automaticamente
- Mostra o status HTTP (200, 404, 403, 500…)
- Identifica erro de conexão
- Pode ser usado para validação rápida de APIs

---

## Tecnologias usadas

- Python
- requests

---

## Como usar

### Instale as dependências

pip install requests

---

### Coloque as URLs que deseja testar no arquivo `python Teste-de-Url-automatico.py`

Exemplo:

python
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpbin.org/status/403",
    "https://sitequenaoexiste123456789.com",
]


---

### Execute o script

python testar_urls.py

---

Projeto criado para prática de automação e estudos em QA.