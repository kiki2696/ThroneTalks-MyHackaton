from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Casas, Miembros
from dialogos import generar_dialogo
import openai
openai.api_key="INGRESE-SU-KEY"

# Instancia de la clase Flask de la biblioteca Flask.
app = Flask(__name__)

# Configuramos la base de datos 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

### RUTAS ###

# Ruta principal - Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar las casas - Homepage
@app.route('/home')
def home():

    # Traemos todas las casas de la base de datos
    casas = Casas.query.all()

    # Renderizamos la plantilla home.html y le pasamos la lista de casas
    return render_template('home.html', casas=casas)

# Ruta para mostrar los miembros de una casa
@app.route('/miembros/<int:id>')
def miembros(id):
    
        # Traemos la casa de la base de datos
        casa = Casas.query.get(id)
    
        # Traemos los miembros de la casa
        miembros = Miembros.query.filter_by(casa_id=id).all()
    
        # Renderizamos la plantilla miembros.html y le pasamos la casa y los miembros
        return render_template('miembros.html', casa=casa, miembros=miembros)

# Ruta para generar dialogos de personajes
@app.route('/dialogo', methods=['GET','POST'])
def dialogo():

    # Inicializar la variable de diálogo con una cadena vacía
    dialogo = ""

    # Realiza una consulta que obtenga todos los miembros de las 3 casas
    todos_los_miembros = Miembros.query.join(Casas, Miembros.casa_id == Casas.id).all()

    def generar_dialogo(cond1, cond2, personaje1_id, personaje2_id):
        personaje1 = Miembros.query.get(personaje1_id)
        personaje2 = Miembros.query.get(personaje2_id)

        # Funcion para obtener la respuesta de la API de OpenAI
        def get_completion(prompt, model="gpt-3.5-turbo"):
            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=0.8, # this is the degree of randomness of the model's output
            )
            return response.choices[0].message["content"]

        prompt= f""" Instrucciones:
        1. Crear un generador de dialogos entre dos personajes de la base de datos. 
        2. El usuario debe elegir dos personajes que se encuentre en la base de datos.
        3. El usuario Puedes establecer parámetros para el tono de la conversación 
        (serio, humorístico, tenso, etc.) y la longitud de los diálogos generados. 
        4. El dialogo debe ser generado por la API de OpenAI, relacionado con el mundo de Game of Thrones

        El usuario pondra estas preferiencias {cond1}, {cond2}
        Vienen de la base de datos, aqui se tienen todos los personajes {todos_los_miembros}
        El usuario escoge los personajes {personaje1.nombre}, {personaje2.nombre}
        

        Cond1: tipo de humor que tendra el dialogo (humoristico, serio, tenso, etc.)
        Cond2: longitud del dialogo (cantidad de palabras)

        Esto podría dar lugar a conversaciones segun cond1 y cond2 entre personajes,
        dados por personaje1 y personaje2.  

        Respuesta:
        Dialogo generado: 
        Obs: No quiero que la respuesta diga cuentos caracteres se han generado o algo relacionado a esto (cond2)
        Obs: Lo personjes deben ser los que el usuario escogio {personaje1.nombre} y {personaje2.nombre})
        Obs: No quiero que la respuesta tenga las instrucciones, solo el dialogo generado
        """

        # Obtener la respuesta de la API de OpenAI
        response = get_completion(prompt)
        return response


    # Si el método es GET, renderizamos la plantilla dialogos.html
    if request.method == 'POST':

        # Obtener los datos del formulario
        cond1 = request.form['cond1']
        cond2 = request.form['cond2']
        personaje1_id = int(request.form['personaje1'])
        personaje2_id = int(request.form['personaje2'])

        # Llamar a la función que genera el diálogo con personaje1, personaje2, cond1 y cond2
        dialogo = generar_dialogo(cond1, cond2, personaje1_id, personaje2_id)
    

    return render_template('dialogos.html', dialogo=dialogo, todos_los_miembros=todos_los_miembros)
    














### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)