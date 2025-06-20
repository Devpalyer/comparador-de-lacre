from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter dados das listas
        lista1 = request.form.get('lista1', '').split('\n')
        lista2 = request.form.get('lista2', '').split('\n')
        
        # Processar as listas
        lista1 = [item.strip() for item in lista1 if item.strip()]
        lista2 = [item.strip() for item in lista2 if item.strip()]
        
        # Calcular resultados
        resultados = {
            'comuns': list(set(lista1) & set(lista2)),
            'adicionar': list(set(lista1) - set(lista2)),
            'excluir': list(set(lista2) - set(lista1)),
            'repetidos_lista1': encontrar_repetidos(lista1),
            'repetidos_lista2': encontrar_repetidos(lista2)
        }
        
        return jsonify(resultados)
    
    return render_template('index.html')

def encontrar_repetidos(lista):
    unicos = set()
    repetidos = set()
    for item in lista:
        if item in unicos:
            repetidos.add(item)
        else:
            unicos.add(item)
    return list(repetidos)

if __name__ == '__main__':
    app.run(debug=True)