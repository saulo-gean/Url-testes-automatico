import requests

urls = [
    "https://meusite.com/login",
    "https://meusite.com/admin",
    "https://meusite.com/produtos",
    "https://www.google.com/pagina-que-nao-existe-12345",
    "https://httpbin.org/status/403",
    "https://sitequenaoexiste123456789.com",
]

# Explicação dos principais status HTTP
status_explicacao = {
    200: "OK - Requisição bem-sucedida.",
    400: "Bad Request - A requisição pode estar mal formada.",
    401: "Unauthorized - Pode estar faltando autenticação ou token.",
    403: "Forbidden - Acesso negado. Permissão insuficiente.",
    404: "Not Found - Endpoint ou página não encontrada.",
    500: "Internal Server Error - Erro interno no servidor.",
    502: "Bad Gateway - Problema de comunicação entre servidores.",
    503: "Service Unavailable - Serviço pode estar fora do ar.",
}

for url in urls:
    print(f"\n🔎 Testando: {url}")

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

        print(f"Status Code: {status}")

        if status in status_explicacao:
            print(f"Possível causa: {status_explicacao[status]}")
        else:
            print("Status não mapeado no script.")

    except requests.exceptions.RequestException:
        print("ERRO DE CONEXÃO - URL inválida ou servidor fora do ar.")