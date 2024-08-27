from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    # Obtener los datos del formulario
    nota1 = request.form['nota1']
    nota2 = request.form['nota2']
    nota3 = request.form['nota3']
    notaTotal = request.form['notaTotal']
    
    #Verificando que se ingreso dato.
    if (nota1=="" or nota2=="" or nota3=="" or notaTotal==""):
        return render_template('index.html', mensaje="Error: Debe ingresar una nota en todas las casillas")
    
    #Convertir dato en decimal 
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    notaTotal = float(notaTotal)

    # Validación básica
    if nota1 < 0 or nota2 < 0 or nota3 < 0 or notaTotal < 0 or notaTotal > 5 or nota1 > 5 or nota2 > 5 or nota3 > 5:
        return render_template('index.html', mensaje="Error: Debe ingresar una nota entre 0 y 5.")
    
    # Porcentajes Notas
    porcNota1 = 0.15
    porcNota2 = 0.20
    porcNota3 = 0.25
    porcNota4 = 0.4
    
    # Realizar el cálculo de las notas
    valorNota1 = nota1 * porcNota1
    valorNota2 = nota2 * porcNota2
    valorNota3 = nota3 * porcNota3
    calculo1 = valorNota1 + valorNota2 + valorNota3
    calculo2 = notaTotal - calculo1 
    calculo3 = calculo2 / porcNota4
    nota4 = round(calculo3, 2)
    estado = nota4
    print(calculo1)
    # Renderizar la plantilla `about.html` con los resultados
    return render_template('about.html', 
                           nota1=nota1, 
                           nota2=nota2, 
                           nota3=nota3,
                           notaTotal=notaTotal, 
                           nota4=nota4,
                           estado=estado)

if __name__ == '__main__':
    app.run(debug=True)
