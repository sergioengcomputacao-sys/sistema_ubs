import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    rua TEXT,
    agente_saude TEXT
)
""")

# EXEMPLO
cursor.execute("""
INSERT INTO pacientes (nome, telefone, rua, agente_saude)
VALUES ('João Silva', '48999999999', 'Rua A, 123', 'Maria Agente')
""")

conn.commit()
conn.close()
