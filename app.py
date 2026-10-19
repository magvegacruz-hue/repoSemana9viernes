from flask import Flask, render_template, request, redirect, url_for
import logica

app = Flask(__name__)


@app.get("/")
def inicio():
    return render_template(
        "index.html",
        pendientes=logica.cola_pendientes,
        historial=logica.pila_historial
    )


@app.post("/registrar")
def registrar():
    logica.registrar_solicitud(
        request.form.get("cliente", ""),
        request.form.get("asunto", "")
    )
    return redirect(url_for("inicio"))


@app.post("/atender")
def atender():
    logica.atender_siguiente()
    return redirect(url_for("inicio"))


@app.post("/deshacer")
def deshacer():
    logica.deshacer_ultima_atencion()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)