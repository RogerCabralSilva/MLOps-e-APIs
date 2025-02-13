# Importação
from flask import Flask

# Instanciando
app = Flask("meu_app")

# Rota


@app.route('/')
def home():
    return "Minha primeira API."


app.run()
