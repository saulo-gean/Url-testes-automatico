import requests

urls = [
    "https://meusite.com/login",
    "https://meusite.com/admin",
    "https://meusite.com/produtos",
    "https://www.google.com/pagina-que-nao-existe-12345",
    "https://httpbin.org/status/403",
    "https://sitequenaoexiste123456789.com",
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} → Status: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} → ERRO DE CONEXÃO")