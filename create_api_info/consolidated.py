from flask import Flask,request, jsonify

BOOKS = [
     {
          'id': 1,
          'title': 'Harry Potter',
          'author': 'Hawkings',
     },
     {
          'id': 2,
          'title': 'Pan Tadeusz',
          'author': 'Mickiewicz',
     },
     {
          'id': 3,
          'title': 'Biblia',
          'author': 'Bóg',
     },

]
app = Flask(__name__)

@app.route('/books', methods=['GET', 'POST'])
def items():
    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
    }
    #show all books
    if request.method == 'GET':
        response_data['data'] = BOOKS
        return jsonify(response_data)
    #add book to all books
    elif request.method == 'POST':
        #data from request body
        new_data = request.json

        #sprawdzenie poprawności danych z request body
        if 'id' not in new_data or 'title' not in new_data or 'author' not in new_data:
            response_data['success'] = False
            response_data['error'] = 'Please provide all required information'
            response = jsonify(response_data)
            response.status_code = 400
        else:
            BOOKS.append(new_data)
            response_data['data'] = BOOKS
            response = jsonify(response_data)
            #change status code - create new element
            response.status_code = 201
        return response

@app.route('/books/<int:book_id>', methods=['GET'])
def item(book_id):
    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
    }

    try:
        item = [book for book in BOOKS if book['id'] == book_id][0]
    except IndexError:
        response_data['success']= False
        response_data['error'] = "Not Found"
        response = jsonify(response_data)
        response.status_code = 404
    else:
        #aktualizacja schematu odpowiedzi
        response_data['data'] = item
        response = jsonify(response_data)
    return response

    #########################################
    # #pętla po książkach w celu dopasowania id zamiast list comprehension
    # item = ''
    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         item = book
    

    # #aktualizacja schematu odpowiedzi
    # response_data['data'] = item
    # return jsonify(response_data)

@app.errorhandler(404)
def not_found(error):
    #schemat odpowiedzi
    response_data ={
         'success': False,
         'data' : [],
         'error': 'Not Found this products',
    }

    response = jsonify(response_data)
    response.status_code = 404
    return response
    




if __name__ == '__main__':
     app.run(debug=True)