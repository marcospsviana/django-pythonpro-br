from send_email import Enviador, EmailInvalido
import pytest


def test_envio_email_spam():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    "destinatario", ["samaralivia.tomesousa@gmail.com", "teste@exemple.com"]
)
def test_enviar_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        "marcospaulo.silvaviana@gmail.com",
        destinatario,
        "teste de envio de email",
        "se vc recebeu esta mensagem é pq o teste foi bem sucedido",
    )
    assert destinatario in resultado


@pytest.mark.parametrize("destinatario", ["", "exemple.com"])
def test_enviar_email_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):

        enviador.enviar(
            "marcospaulo.silvaviana@gmail.com",
            destinatario,
            "teste de envio de email",
            "se vc recebeu esta mensagem é pq o teste foi bem sucedido",
        )
