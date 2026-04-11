from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá! Minha aplicação Python está rodando perfeitamente no Docker!"

if __name__ == '__main__':
    # O host '0.0.0.0' é crucial para que o Docker exponha a porta corretamente
    app.run(host='0.0.0.0', port=5000)