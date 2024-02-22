from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    ###  Request info
     
    #  print(request.headers)
    #  print(f'method:{request.method}')
    #  print(f'path:{request.path}')
    #  print(f'url:{request.url}')
    #  print(request.headers['Authorization'])
    #  print(request.headers['Content-Type'])
    #  print(request.json) - wyświetla body requesta
    #  print(request.json['name'])
    
    ### Response info
    # response = jsonify([{'id': 1, 'title': 'Title XXX'}])
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    return response

if __name__ == '__main__':
     app.run(debug=True)