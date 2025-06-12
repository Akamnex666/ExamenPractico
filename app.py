from app import Flask, request, jsonify
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq


app = Flask(__name__)

# Inicializa tu agente (o modelo) aquí
agent = Agent()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Supongamos que tu agente recibe texto y devuelve respuesta
    input_text = data.get('text', '')
    response = agent.process(input_text)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
