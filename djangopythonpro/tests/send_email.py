class Enviador:
    def enviar(self, remtente_address, destinatario, assunto, corpo_email):
        if "@" not in destinatario:
            raise EmailInvalido(f"Email {destinatario} é inválido")
        return destinatario


class EmailInvalido(Exception):
    pass
