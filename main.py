from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Harry Potter',
        'autor': 'J. K. Rowling'
    },
    {
            'id': 2,
            'título': 'Harry Potter - 2',
            'autor': 'J. K. Rowling'
        },
    {
            'id': 3,
            'título': 'Harry Potter 3 ',
            'autor': 'J. K. Rowling'
        },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def id_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def edit_livro(id):
    livro_aleatorio = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_aleatorio)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def new_livro():
    novo_livro =request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro():
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)

app.run(port=5000, host='localhost',debug=True)