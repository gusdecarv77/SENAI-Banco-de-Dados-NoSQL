from flask import Flask, render_template_string
import redis

app = Flask(__name__)

# Conecta ao Redis
try:
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    redis_client.ping()  # Testa a conexão
except Exception as e:
    print(f"⚠️ AVISO: Redis não está disponível. Erro: {e}")
    redis_client = None

# Estrutura HTML da nossa interface (Front-end)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redis - Visualizador de Imagem</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
        .container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); display: inline-block; }
        img { max-width: 500px; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Imagem Recuperada do Redis 🗄️</h2>
        
        {% if imagem_b64 %}
            <img src="data:image/png;base64,{{ imagem_b64 }}" alt="Imagem salva no banco">
        {% else %}
            <p style="color: red;">Nenhuma imagem encontrada no Redis com a chave especificada.</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Busca a string Base64 da imagem salva no Redis
    if redis_client is None:
        return render_template_string(HTML_TEMPLATE, imagem_b64=None)
    
    imagem_salva = redis_client.get("minha_imagem_front")
    
    # Renderiza a página HTML injetando a variável imagem_salva
    return render_template_string(HTML_TEMPLATE, imagem_b64=imagem_salva)

if __name__ == '__main__':
    # Inicia o servidor web na porta 5000
    print("Iniciando o servidor... Acesse http://127.0.0.1:5000 no seu navegador.")
    app.run(debug=True)
    