"""
An RFC-4217 asynchronous FTPS server supporting both SSL and TLS.
Requires PyOpenSSL module (http://pypi.python.org/pypi/pyOpenSSL).
"""

from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    authorizer.add_anonymous("/home/sunny/Downloads", perm="elradfmw")
    handler = TLS_FTPHandler
    handler.certfile = 'keycert.pem'
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    #handler.tls_control_required = True
    #handler.tls_data_required = True
    server = FTPServer(('0.0.0.0', 1027), handler)
    server.serve_forever()


if __name__ == '__main__':
    main()