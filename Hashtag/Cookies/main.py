from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Meu site está no ar"

@app.route("/criar-cookie")
def criar_cookie():
    resposta = make_response("O cookie foi criado")
    resposta.set_cookie("nome_usuario", "Lira")
    return resposta

@app.route("/ver-cookie")
def ver_cookie():
    cookies = request.cookies
    return cookies

if __name__ == "__main__":
    app.run(debug=True)