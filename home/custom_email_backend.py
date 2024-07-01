import ssl
from django.core.mail.backends.smtp import EmailBackend
import smtplib


class CustomEmailBackend(EmailBackend):
    """
    Custom email backend for SMTP connections with extended functionality.

    This backend inherits from Django's built-in `EmailBackend` and provides
    additional methods and configuration options for handling SMTP connections
    with SSL/TLS encryption and authentication.

    Attributes:
        host (str): The SMTP host to connect to.
        port (int): The port number to use for the SMTP connection.
        username (str, optional): The username for SMTP authentication.
        password (str, optional): The password for SMTP authentication.
        use_tls (bool): Whether to use TLS encryption (default is False).
        ssl_certfile (str, optional):
        Path to the SSL certificate file (PEM format).
        ssl_keyfile (str, optional): Path to the SSL key file (PEM format).
        fail_silently (bool): Whether errors should be silently ignored.

        Methods:
            open():
                Ensure a connection is open to the email server.
    """

    def open(self):
        """Ensure a connection is open to the email server."""
        if self.connection:
            return False

        try:
            self.connection = smtplib.SMTP(
                self.host, self.port, **self.connection_params
            )
            self.connection.ehlo()
            if self.use_tls:
                context = ssl.create_default_context()
                if self.ssl_keyfile or self.ssl_certfile:
                    context.load_cert_chain(
                        certfile=self.ssl_certfile, keyfile=self.ssl_keyfile
                    )
                self.connection.starttls(context=context)
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if self.fail_silently:
                return False
            raise
