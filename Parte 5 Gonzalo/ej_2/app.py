from flask import Flask, jsonify
app = Flask(__name__)

# Ruta para enviar datos al Front-End
@app.route('/datos', methods=['GET'])
def obtener_datos():
    ejemplo_datos = {
        "mensaje": "Hello, World!",
        "usuarios": ["Ana", "Carlos", "Beatriz"],
        "estado": "éxito"
    }
    return jsonify(ejemplo_datos)

if __name__ == '__main__':
    app.run(debug=True)
