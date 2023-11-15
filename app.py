from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from assistant import callchat
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        messages = request.get_json()
        if 'message' in messages:
            user_message = messages['message']
            result = callchat(user_message)
            return result
    return "message not found", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234) #서비스시 host값 ip로 변경, port도 변경, route경로도 확인할것
