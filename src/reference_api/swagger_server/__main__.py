#!/usr/bin/env python3

import connexion
import time

from swagger_server import encoder
from flask_cors import CORS

def main():
    options = {'swagger_path': '/app/src/reference_api/ssl-swagger-ui/dist/'}
    
    app = connexion.App(__name__, specification_dir='./swagger/',options=options)
    app.app.json_encoder = encoder.JSONEncoder
    # app.add_api('swagger.yaml', arguments={'title': 'ADDI Federated Data Sharing Common API Strawman'}, pythonic_params=True, validate_responses=True)
    app.add_api('swagger.yaml', arguments={'title': 'ADDI Federated Data Sharing Common API Strawman'}, pythonic_params=True)

    CORS(app.app)

    print("Running API....")
    app.run(host="0.0.0.0", port=8443,ssl_context="adhoc")


if __name__ == '__main__':
    main()
