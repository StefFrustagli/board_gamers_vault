import ssl
from django.core.mail.backends.smtp import EmailBackend
import smtplib


class CustomEmailBackend(EmailBackend):
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
