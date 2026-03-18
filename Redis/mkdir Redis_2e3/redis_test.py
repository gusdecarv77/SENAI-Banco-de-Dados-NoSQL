"""
Arquivo de teste para Redis - Testes básicos e exemplo de uso
Criado para validar a conexão e funcionalidades do Redis
"""

import redis
import time
import base64

# Conexão com Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def test_connection():
    """Testa a conexão com o servidor Redis"""
    try:
        response = redis_client.ping()
        print("✓ Conexão com Redis estabelecida com sucesso!")
        return True
    except Exception as e:
        print(f"✗ Erro ao conectar com Redis: {e}")
        return False

def test_basic_operations():
    """Testa operações básicas: SET e GET"""
    print("\n=== Testando Operações Básicas ===")
    
    redis_client.set("nome", "João")
    redis_client.set("idade", "25")
    redis_client.set("cidade", "São Paulo")
    
    print(f"Nome: {redis_client.get('nome')}")
    print(f"Idade: {redis_client.get('idade')}")
    print(f"Cidade: {redis_client.get('cidade')}")

def test_performance():
    """Testa o desempenho e a escalabilidade do Redis"""
    print("\n=== Testando Desempenho e Escalabilidade ===")
    
    start_time = time.time()
    for i in range(1000):
        redis_client.set(f"item_{i}", f"valor_{i}")
    store_time = time.time() - start_time
    print(f"Tempo para armazenar 1000 itens: {store_time:.4f} segundos")
    
    start_time = time.time()
    for i in range(1000):
        redis_client.get(f"item_{i}")
    retrieve_time = time.time() - start_time
    print(f"Tempo para recuperar 1000 itens: {retrieve_time:.4f} segundos")

def test_flexibilidade():
    """Testa diferentes tipos de dados suportados pelo Redis (Listas, Hashes, Base64)"""
    print("\n=== Testando Flexibilidade ===")
    
    # Lista
    redis_client.delete("lista_teste") # Limpa caso exista
    redis_client.rpush("lista_teste", "item1", "item2", "item3")
    print(f"Lista armazenada: {redis_client.lrange('lista_teste', 0, -1)}")
    
    # Hash
    redis_client.hset("hash_teste", "campo1", "valor1")
    redis_client.hset("hash_teste", "campo2", "valor2")
    print(f"Hash armazenado: {redis_client.hgetall('hash_teste')}")
    
    # Binário (Base64)
    image_data = base64.b64encode(b"dados_binarios_simulados").decode("utf-8")
    redis_client.set("binario_teste", image_data)
    print(f"Dado binário salvo: {redis_client.get('binario_teste')[:20]}... [Cortado]")

def test_baixa_latencia():
    """Demonstra o uso como cache para acessos rápidos"""
    print("\n=== Testando Baixa Latência (Cache) ===")
    
    redis_client.set("config_cache", "ativo")
    for _ in range(3):
        start = time.time()
        val = redis_client.get("config_cache")
        end = time.time()
        print(f"Cache lido: {val} | Tempo: {end - start:.6f}s")

def test_delete():
    """Testa a exclusão de chaves"""
    print("\n=== Testando Deleção ===")
    
    redis_client.set("chave_temp", "valor_temporario")
    print(f"Antes de deletar: {redis_client.get('chave_temp')}")
    redis_client.delete("chave_temp")
    print(f"Após deletar: {redis_client.get('chave_temp')}")

def main():
    """Executa todos os testes"""
    print("=" * 50)
    print("TESTES REDIS - PARTE 2")
    print("=" * 50)
    
    if not test_connection():
        print("Encerrando... Redis não está disponível")
        return
    
    test_basic_operations()
    test_performance()
    test_flexibilidade()
    test_baixa_latencia()
    test_delete()
    
    print("\n" + "=" * 50)
    print("Todos os testes concluídos com sucesso!")
    print("=" * 50)

if __name__ == "__main__":
    main()