from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        'artista': 'Jason Mraz',
        'titulo': '93 Million Miles'
    },
    {
        'artista': 'Coldplay',
        'titulo': 'Clocks'
    },
    {
        'artista': 'Diana Ross',
        'titulo': 'Thank You'
    }
]

# GET - http://localhost:5000/cancoes
@app.route('/cancoes')
def obter_musicas():
    return jsonify(musicas)

# GET com indice - http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['GET'])
def obter_musicas_por_indice(indice):
    return jsonify(musicas[indice])

# Criando nova musica com POST - http://localhost:5000/cancoes
@app.route('/cancoes', methods=['POST'])
def criar_nova_musica():
    musica = request.get_json()
    musicas.append(musica)

    return jsonify(musica, 200)

# Alterando musica existente com PUT - http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['PUT'])
def editar_musica_existente(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)

    return jsonify(musicas[indice], 200)

@app.route('/cancoes/<int:indice>', methods=['DELETE'])
def deletar_musica(indice):
    try:
        if musicas[indice] is not None:
            return jsonify(f'Excluindo a música {musicas[indice]}', 200)
    except:
        return jsonify('Não foi possível excluir a música, pois não foi encontrada', 404)


app.run(port=5000, host='localhost', debug=True)