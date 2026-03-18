import redis
import base64

# Conecta ao Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Nome do arquivo de imagem que você colocou na pasta
nome_da_imagem = r"C:\Users\Usuario\SENAI-Banco-de-Dados-NoSQL\Redis\Onca.png"

try:
    # Abre a imagem em modo de leitura binária ('rb')
    with open(nome_da_imagem, "rb") as image_file:
        # Codifica os bytes da imagem para Base64 e converte para string
        imagem_base64 = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Salva no Redis com a chave 'minha_imagem_front'
    redis_client.set("minha_imagem_front", imagem_base64)
    print("Sucesso! Imagem convertida para Base64 e salva no Redis.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_da_imagem}' não foi encontrado na pasta.")