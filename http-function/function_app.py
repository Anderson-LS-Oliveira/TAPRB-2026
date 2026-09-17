import logging
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