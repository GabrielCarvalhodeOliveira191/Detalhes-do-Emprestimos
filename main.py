from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def inicio():
    return render_template("historico_emprestimos.html", dados=[])


@app.route("/historico_emprestimos")
def historico_emprestimos():
    return render_template("historico_emprestimos.html", dados=[])


@app.route("/logo")
def logo():
    caminho = os.path.join(app.root_path, "static", "uploads")
    return send_from_directory(caminho, "logo.png")

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
