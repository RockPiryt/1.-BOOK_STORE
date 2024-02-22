from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    ###  Request info
    
    #  różne headery
    #  print(request.headers)
    #  print(f'method:{request.method}')
    #  print(f'path:{request.path}')
    #  print(f'url:{request.url}')
    #  print(request.headers['Authorization'])
    #  print(request.headers['Content-Type'])
    
    #  wyświetla body requesta
    #  print(request.json) 
    #  print(request.json['name'])
    
    ### Response info
    # zwykła odpowiedź
    # response = jsonify([{'id': 1, 'title': 'Title XXX'}])
    
    # zmiana kodu odpowiedzi
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    return response

if __name__ == '__main__':
     app.run(debug=True)