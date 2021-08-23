class Enviador:
    def __init__(
        self, remtente_address=None, destinatario=None, assunto=None, corpo_email=None
    ):
        self.remtente_address = remtente_address
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo_email = corpo_email

        self.parameter_list = (
            self.remtente_address,
            self.destinatario,
            self.assunto,
            self.corpo_email,
        )

    def enviar(self, *parameter_list):
        return parameter_list
