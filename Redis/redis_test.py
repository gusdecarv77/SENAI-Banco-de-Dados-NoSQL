"""
Arquivo de teste para Redis - Testes básicos e exemplo de uso
Criado para validar a conexão e funcionalidades do Redis
"""

import redis
import time

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
    
    # SET - Armazenar dados
    redis_client.set("nome", "João")
    redis_client.set("idade", "25")
    redis_client.set("cidade", "São Paulo")
    
    # GET - Recuperar dados
    nome = redis_client.get("nome")
    idade = redis_client.get("idade")
    cidade = redis_client.get("cidade")
    
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

def test_performance():
    """Testa o desempenho do Redis com múltiplas operações"""
    print("\n=== Testando Desempenho ===")
    
    start_time = time.time()
    
    # Armazenar 1000 chaves
    for i in range(1000):
        redis_client.set(f"item_{i}", f"valor_{i}")
    
    store_time = time.time() - start_time
    print(f"Tempo para armazenar 1000 itens: {store_time:.4f} segundos")
    
    # Recuperar 1000 chaves
    start_time = time.time()
    for i in range(1000):
        redis_client.get(f"item_{i}")
    
    retrieve_time = time.time() - start_time
    print(f"Tempo para recuperar 1000 itens: {retrieve_time:.4f} segundos")

def test_delete():
    """Testa a exclusão de chaves"""
    print("\n=== Testando Deleção ===")
    
    redis_client.set("chave_temp", "valor_temporario")
    print(f"Chave antes de deletar: {redis_client.get('chave_temp')}")
    
    redis_client.delete("chave_temp")
    print(f"Chave após deletar: {redis_client.get('chave_temp')}")

def main():
    """Executa todos os testes"""
    print("=" * 50)
    print("TESTES REDIS")
    print("=" * 50)
    
    if not test_connection():
        print("Encerrando... Redis não está disponível")
        return
    
    test_basic_operations()
    test_performance()
    test_delete()
    
    print("\n" + "=" * 50)
    print("Testes concluídos com sucesso!")
    print("=" * 50)

if __name__ == "__main__":
    main()
