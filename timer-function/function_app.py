import logging
import urllib.request
import urllib.parse

import azure.functions as func

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="timer",
    run_on_startup=False,
    use_monitor=False
)
def TimerChamadaHttp(timer: func.TimerRequest) -> None:

    logging.info("Timer Trigger executado.")

    parametros = urllib.parse.urlencode({
        "nome": "Anderson"
    })

    url = f"http://localhost:7071/api/receber?{parametros}"

    try:
        with urllib.request.urlopen(url, timeout=10) as resposta:
            resultado = resposta.read().decode("utf-8")

        logging.info(f"Resposta da HTTP Function: {resultado}")

    except Exception as erro:
        logging.error(f"Erro ao chamar a HTTP Function: {erro}")