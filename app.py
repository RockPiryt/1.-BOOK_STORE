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

@app.route('/books', methods=['GET'])
def get_books():
    '''Show all books'''

    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
    }
    response_data['data'] = BOOKS
    return jsonify(response_data)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_single_book(book_id):
    '''Show single book'''

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

@app.route('/books', methods=['POST'])
def create_book():
    '''Add new book to list BOOKS'''

    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
    }
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


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    '''Update single book'''

    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
         'info': f'Book with id {book_id} has been updated'
    }

    #data from request body
    new_data = request.json

    ##tutaj chyba źle do analizy!!
    try:
        item = [book for book in BOOKS if book['id'] == book_id][0]
    except IndexError:
        response_data['success']= False
        response_data['error'] = "Not Found this book"
        response = jsonify(response_data)
        response.status_code = 404
    else:
        #aktualizacja schematu odpowiedzi
        item['id'] = new_data['id']
        item['title'] = new_data['title']
        item['author'] = new_data['author']
        response_data['data'] = BOOKS
        response = jsonify(response_data)
    return response


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    '''Delete single book'''
    
    #schemat odpowiedzi
    response_data ={
         'success': True,
         'data' : [],
         'info': f'Book with id {book_id} has been deleted.'
    }

    try:
        item = [book for book in BOOKS if book['id'] == book_id][0]
    except IndexError:
        response_data['success']= False
        response_data['error'] = "Not Found this book"
        response = jsonify(response_data)
        response.status_code = 404
    else:
        number = book_id - 1
        BOOKS.pop(number)
        response_data['data'] = BOOKS
        response = jsonify(response_data)
    return response



@app.errorhandler(404)
def not_found(error):
    '''For not existing url'''

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