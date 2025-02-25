from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configurar a API Key corretamente
openai.api_key = os.getenv("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")

@app.route('/')
def home():
    return "API do Chatbot está rodando no Render!"

@app.route('/pergunta', methods=['POST'])
def responder_pergunta():
    try:
        dados = request.json
        
        if not dados or "pergunta" not in dados:
            return jsonify({"erro": "Envie uma pergunta válida no formato JSON."}), 400

        pergunta = dados.get("pergunta")

        # 🚀 Forma correta de chamar a API na versão OpenAI 1.0.0
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente de um curso online que responde dúvidas sobre aulas e materiais."},
                {"role": "user", "content": pergunta}
            ]
        )

        return jsonify({"resposta": resposta["choices"][0]["message"]["content"]})

    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    import logging

# Configurar logs detalhados
logging.basicConfig(level=logging.DEBUG)

@app.route('/pergunta', methods=['POST'])
def responder_pergunta():
    try:
        dados = request.json
        if not dados or "pergunta" not in dados:
            logging.error("Erro: Nenhuma pergunta enviada no JSON.")
            return jsonify({"erro": "Envie uma pergunta válida no formato JSON."}), 400

        pergunta = dados.get("pergunta")
        logging.info(f"Pergunta recebida: {pergunta}")

        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente de um curso online que responde dúvidas sobre aulas e materiais."},
                {"role": "user", "content": pergunta}
            ]
        )

        logging.info(f"Resposta gerada: {resposta}")

        return jsonify({"resposta": resposta["choices"][0]["message"]["content"]})

    except openai.error.AuthenticationError:
        logging.error("Erro de autenticação na OpenAI. Verifique sua API Key.")
        return jsonify({"erro": "Erro de autenticação na OpenAI. Verifique sua API Key."}), 401
    except openai.error.OpenAIError as e:
        logging.error(f"Erro na API OpenAI: {str(e)}")
        return jsonify({"erro": f"Erro na API OpenAI: {str(e)}"}), 500
    except Exception as e:
        logging.error(f"Erro interno no servidor: {str(e)}")
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500

