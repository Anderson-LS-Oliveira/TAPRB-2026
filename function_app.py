import logging
import os
import urllib.request
import urllib.parse

import azure.functions as func

app = func.FunctionApp()


@app.route(route="receber", auth_level=func.AuthLevel.ANONYMOUS)
def ReceberParametro(req: func.HttpRequest) -> func.HttpResponse:
    nome = req.params.get("nome")

    if not nome:
        return func.HttpResponse(
            "Informe o parametro 'nome' na URL.",
            status_code=400
        )

    mensagem = f"{nome} - informação recebida pela HTTP Function."

    logging.info(mensagem)

    return func.HttpResponse(
        mensagem,
        status_code=200
    )


@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="timer",
    run_on_startup=False,
    use_monitor=False
)
def TimerChamadaHttp(timer: func.TimerRequest) -> None:

    parametros = urllib.parse.urlencode({
        "nome": "Teste"
    })

    url_base = os.environ.get(
        "HTTP_FUNCTION_URL",
        "http://localhost:7071/api/receber"
    )

    url = f"{url_base}?{parametros}"

    try:
        with urllib.request.urlopen(url, timeout=10) as resposta:
            resultado = resposta.read().decode("utf-8")

        logging.info(
            f"Timer Trigger executado. Resposta da HTTP Function: {resultado}"
        )

    except Exception as erro:
        logging.error(
            f"Erro ao chamar a HTTP Function: {erro}"
        )