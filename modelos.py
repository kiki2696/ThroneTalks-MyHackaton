from flask_sqlalchemy import SQLAlchemy

# Crear objeto SQLAlchemy
db = SQLAlchemy()

### MODELOS ###

# nullable=False: no puede ser nulo
# lazy=True: no se carga hasta que se accede a la propiedad
'''
Esto puede ahorrar recursos de la base de datos y mejorar el rendimiento si no siempre necesitas los datos relacionados.
Por ejemplo, si tienes un objeto Casa con una relación miembros y configuraste lazy=True, 
los datos de los miembros de esa casa no se cargarán automáticamente cuando recuperes un objeto Casa. 
Solo se cargarán cuando intentes acceder a la lista de miembros de esa casa, como casa.miembros
'''

# Crear modelo de la tabla Casas
class Casas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    casa = db.Column(db.String(30), nullable=False)
    lema = db.Column(db.String(30), nullable=False)
    logo = db.Column(db.String(30), nullable=False)
    historia = db.Column(db.String(30), nullable=False)
    # relaciones con otras tablas
    miembros = db.relationship('Miembros', backref='casa', lazy=True)

# Crear modelo de la tabla Miembros
class Miembros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apodo = db.Column(db.String(30), nullable=True)
    edad = db.Column(db.Integer, nullable=False)
    detalles = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(30), nullable=True)
    casa_id = db.Column(db.Integer, db.ForeignKey('casas.id'), nullable=False)
    
