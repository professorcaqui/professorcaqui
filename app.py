from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Insira sua chave da OpenAI aqui
openai.api_key = "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"

@app.route('/')
def home():
    return "API do Chatbot está rodando no Render!"

@app.route('/pergunta', methods=['POST'])
def responder_pergunta():
    dados = request.json
    pergunta = dados.get("pergunta")

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o Professor Caqui, um assistente da Mentoria M5, que responde dúvidas sobre aulas e materiais."},
            {"role": "user", "content": pergunta}
        ]
    )

    return jsonify({"resposta": resposta["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
