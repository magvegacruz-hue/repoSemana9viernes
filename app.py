from flask import Flask, render_template, request, redirect, url_for
import logica


app = Flask(__name__)


@app.get("/")
def inicio():
    siguiente = logica.consultar_siguiente()
    pendientes, atendidas, total_unicas = logica.obtener_estadisticas()

    return render_template(
        "index.html",
        pendientes=logica.cola_pendientes,
        historial=logica.pila_historial,
        siguiente=siguiente,
        cantidad_pendientes=pendientes,
        cantidad_atendidas=atendidas,
        total_unicas=total_unicas,
        mensaje=request.args.get("mensaje", "")
    )


@app.post("/registrar")
def registrar():
    cliente = request.form.get("cliente", "")
    asunto = request.form.get("asunto", "")

    resultado = logica.registrar_solicitud(cliente, asunto)

    if resultado is None:
        mensaje = "No se registró: datos inválidos o la solicitud ya está pendiente."
    else:
        mensaje = "Solicitud registrada correctamente."

    return redirect(url_for("inicio", mensaje=mensaje))


@app.post("/atender")
def atender():
    resultado = logica.atender_siguiente()

    if resultado is None:
        mensaje = "No hay solicitudes pendientes."
    else:
        mensaje = "Se atendió la solicitud de " + resultado["cliente"] + "."

    return redirect(url_for("inicio", mensaje=mensaje))


@app.post("/deshacer")
def deshacer():
    resultado = logica.deshacer_ultima_atencion()

    if resultado is None:
        mensaje = "No hay atenciones para deshacer."
    else:
        mensaje = "Se restauró la solicitud de " + resultado["cliente"] + "."

    return redirect(url_for("inicio", mensaje=mensaje))


@app.post("/deshacer_varias")
def deshacer_varias():
    texto_cantidad = request.form.get("cantidad", "").strip()

    if not texto_cantidad.isdigit():
        mensaje = "Debes digitar un número entero positivo."
    else:
        cantidad = int(texto_cantidad)

        if cantidad <= 0:
            mensaje = "La cantidad debe ser mayor que cero."
        else:
            recuperadas = logica.deshacer_varias(cantidad)
            mensaje = "Se recuperaron " + str(recuperadas) + " solicitud(es)."

    return redirect(url_for("inicio", mensaje=mensaje))


@app.post("/buscar")
def buscar():
    texto_id = request.form.get("id_solicitud", "").strip()

    if not texto_id.isdigit():
        mensaje = "Debes digitar un ID numérico."
        return redirect(url_for("inicio", mensaje=mensaje))

    id_solicitud = int(texto_id)
    resultado = logica.buscar_solicitud(id_solicitud)

    if resultado is None:
        mensaje = "No se encontró la solicitud con ID " + texto_id + "."
    else:
        solicitud, ubicacion = resultado
        mensaje = "Solicitud encontrada en " + ubicacion + ": " + solicitud["cliente"] + " - " + solicitud["asunto"]

    return redirect(url_for("inicio", mensaje=mensaje))


@app.post("/cancelar")
def cancelar():
    texto_id = request.form.get("id_solicitud", "").strip()

    if not texto_id.isdigit():
        mensaje = "Debes digitar un ID numérico."
        return redirect(url_for("inicio", mensaje=mensaje))

    id_solicitud = int(texto_id)
    resultado = logica.cancelar_pendiente(id_solicitud)

    if resultado is None:
        mensaje = "No se puede cancelar: la solicitud no está pendiente."
    else:
        mensaje = "Se canceló la solicitud de " + resultado["cliente"] + "."

    return redirect(url_for("inicio", mensaje=mensaje))


if __name__ == "__main__":
    app.run(debug=True)