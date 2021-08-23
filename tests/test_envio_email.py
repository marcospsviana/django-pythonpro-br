from send_email import Enviador


def test_envio_email_spam():
    enviador = Enviador()
    assert enviador is not None


def test_enviar_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        "marcospaulo.silvaviana@gmail.com",
        "samaralivia.tomesousa@gmail.com",
        "teste de envio de email",
        "se vc recebeu esta mensagem é pq o teste foi bem sucedido",
    )
    assert "marcospaulo.silvaviana@gmail.com" in resultado
