from flask import Flask, jsonify, request

import requests

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {"@context": ["https://www.w3.org/2018/credentials/v1"], "credentialSubject": {"id": "did:web:community.veramo.io", "you": "Rock"}, "issuanceDate": "2023-05-05T19:18:50.000Z", "issuer": {"id": "did:peer:2.Ez6LSipvwXKgwsPBVppQ43tR9PPhu4Ecp5tm3QwBVr7sdBr1n.Vz6MkfwLPCoebAubMibA6dK1w2QE57ct3sfaaxRyK2yhSwjwT.SeyJpZCI6IjEyMzQiLCJ0IjoiZG0iLCJzIjoiZGlkOndlYjpkZXYtZGlkY29tbS1tZWRpYXRvci5oZXJva3VhcHAuY29tIiwiZGVzY3JpcHRpb24iOiJhIERJRENvbW0gZW5kcG9pbnQifQ"}, "proof": {"jwt": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSJdLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIl0sImNyZWRlbnRpYWxTdWJqZWN0Ijp7InlvdSI6IlJvY2sifX0sInN1YiI6ImRpZDp3ZWI6Y29tbXVuaXR5LnZlcmFtby5pbyIsIm5iZiI6MTY4MzMxNDMzMCwiaXNzIjoiZGlkOnBlZXI6Mi5FejZMU2lwdndYS2d3c1BCVnBwUTQzdFI5UFBodTRFY3A1dG0zUXdCVnI3c2RCcjFuLlZ6Nk1rZndMUENvZWJBdWJNaWJBNmRLMXcyUUU1N2N0M3NmYWF4UnlLMnloU3dqd1QuU2V5SnBaQ0k2SWpFeU16UWlMQ0owSWpvaVpHMGlMQ0p6SWpvaVpHbGtPbmRsWWpwa1pYWXRaR2xrWTI5dGJTMXRaV1JwWVhSdmNpNW9aWEp2YTNWaGNIQXVZMjl0SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpoSUVSSlJFTnZiVzBnWlc1a2NHOXBiblFpZlEifQ.4uPlCXRce1RpnEXYNfMblWnnaCtMMzU66b9hABeS1aueC6C33cez97BYoMhVUsDCSicfLMfmBf5d9dAnHy2-DQ", "type": "JwtProof2020"}, "type": ["VerifiableCredential"]}
    return jsonify(data)


@app.route('/createVC')
def create_vc():
    name = request.args.get('name')
    did = request.args.get('did')
    vc = {
            "credential": {
                "issuer": {
                "id": "did:ethr:goerli:0x039f2fe1775bb29c01d92f2366eb5c9ac56106d72c9048e7e12e1b9b5e22e3108b"
                },
                "credentialSubject": {
                "name": name,

                "id": did,
                },
                "type": [
                "string"
                ],
                "@context": "string",
                "issuanceDate": "string",
                "expirationDate": "string",
                "credentialStatus": {
                "id": "string",
                "type": "string"
                },
                "id": "string"
            },
            "proofFormat": "jwt",
            "keyRef": "string",
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
        }


    url = 'http://localhost:3332/agent/createVerifiableCredential'
    headers = {
        'Authorization': 'Bearer test123',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=vc)

    if response.status_code == requests.codes.ok:
        response_data = response.json()
        # Do something with the response data
        print(response_data)
    else:
        print(f'Request failed with status code {response.status_code}')

    
    return response_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
