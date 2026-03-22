from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def buscar_paciente(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nome, telefone, rua, agente_saude FROM pacientes WHERE id=?", (id,))
    paciente = cursor.fetchone()

    conn.close()
    return paciente

# 🔥 NOVA ROTA (COLOCA ISSO)
@app.route("/")
def home():
    return "SERVIDOR ONLINE"

# SUA ROTA ORIGINAL
@app.route("/paciente/<int:id>")
def paciente(id):
    dados = buscar_paciente(id)

    if dados:
        return render_template("paciente.html", paciente=dados)
    else:
        return "Paciente não encontrado"

if __name__ == "__main__":
    app.run()
