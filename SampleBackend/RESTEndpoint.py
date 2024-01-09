from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/testEP/get_request', methods=['GET'])
def process_get_request():
    try:
        response_payload = {'message': 'Hello, this is a test!'}
        custom_headers = {'content-type': 'application/json'}

        response = jsonify(response_payload)
        response.headers = custom_headers
        response.status_code = 200

        return response
    
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500


@app.route('/testEP/post_request', methods=['POST'])
def process_post_request():
    try:
        post_response = request.json

        # Process the data (you can replace this with your logic)
        response_payload = {'message':'Received and processed the message',
                            'Message': post_response}
        custom_headers = {'content-type': 'application/json'}

        response = jsonify(response_payload)
        response.headers = custom_headers
        response.status_code = 200

        return response

    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500


if __name__ == '__main__':
    app.run(debug=True)