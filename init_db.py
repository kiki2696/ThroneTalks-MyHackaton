from modelos import db, Casas, Miembros
from flask import Flask 

# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()

# Cargamos los datos en la base de datos
with app.app_context():

    ### cargar Casas ###
    casa_1 = Casas(casa='Stark', lema='The winter is coming', logo='/static/logo stark.svg', historia='La familia Stark gobernó en el Norte durante miles de años antes, extendiéndose su linaje hasta los Primeros Hombres. Tras el ascenso al poder de los Targaryens y su conquista de los Siete Reinos, los miembros de la Casa Stark fueron nombrados Señores de Invernalia y Guardianes del Norte.')
    casa_2 = Casas(casa='Lannister', lema='Un Lannister siempre paga sus deudas', logo='/static/lannister logo.svg', historia='La Casa Lannister de Roca Casterly es una de las Grandes Casas de Poniente y la más rica. Gobiernan desde su asiento en Roca Casterly y su emblema es un león rampante de oro sobre fondo carmesí.')
    casa_3 = Casas(casa='Targaryen', lema='Fire and Blood', logo='/static/targaryen logo.svg', historia='La Casa Targaryen de Rocadragón es una antigua familia de descendientes valyrios que una vez gobernó los Siete Reinos de Poniente. La Casa Targaryen reinó como familia real durante casi trescientos años, hasta la Guerra del Usurpador, que terminó con la rebelión que llevó a la dinastía a su fin.')
    ### cargar Miembros ###
    # casa 1 - Stark
    miembro_1 = Miembros(nombre='Eddard Stark', apodo='Ned', edad=35, detalles='Señor de Invernalia, Guardián del Norte, Mano del Rey Robert I',foto='/static/ned.png' , casa_id=1)
    miembro_2 = Miembros(nombre='Arya Stark', apodo='No one', edad=12, detalles='Hija menor de Eddard Stark y Catelyn Tully, hermana de Robb, Sansa, Bran y Rickon Stark, y medio hermana de Jon Snow.', foto='/static/arya.png', casa_id=1)
    miembro_3 = Miembros(nombre='Jon Snow', apodo='Lord Snow', edad=24, detalles='Lord Comandante de la Guardia de la Noche, Rey en el Norte', foto='/static/jon.png', casa_id=1)

    # casa 2 - Lannister
    miembro_4 = Miembros(nombre='Tywin Lannister', apodo='El león de Casterly Rock', edad=67, detalles='Señor de Casterly Rock, Guardián del Oeste, Mano del Rey Aerys II Targaryen', foto='/static/tywin.png', casa_id=2)
    miembro_5 = Miembros(nombre='Cersei Lannister', apodo='La leona Lannister', edad=42, detalles='Reina de los Siete Reinos, Reina consorte de los Siete Reinos, Reina madre de los Siete Reinos, Lady de Roca Casterly, Lady de Refugio Estival', foto='/static/cersei.png', casa_id=2)
    miembro_6 = Miembros(nombre='Tyrion Lannister', apodo='El gnomo', edad=39, detalles='Mano de la Reina Daenerys I Targaryen, Lord de Casterly Rock, Guardián del Oeste', foto='/static/tyrion.png', casa_id=2)

    # casa 3 - Targaryen
    miembro_7 = Miembros(nombre='Aerys II Targaryen', apodo='El Rey Loco', edad=39, detalles='Rey de los Siete Reinos, Señor de los Siete Reinos, Protector del Reino', foto='/static/loco.png', casa_id=3)
    miembro_8 = Miembros(nombre='Daenerys Targaryen', apodo='Madre de Dragones', edad=22, detalles='Reina de los Ándalos, los Rhoynar y los Primeros Hombres, Señora de los Siete Reinos, Protectora del Reino, Khaleesi del Gran Mar Dothraki, Rompedora de Cadenas, Madre de Dragones, La que no arde, La Reina Dragón, La Reina de Meereen, La Princesa que fue Prometida, La Reina de los Ándalos y los Primeros Hombres, La Primera de su Nombre', foto='/static/dani.png', casa_id=3)
    miembro_9 = Miembros(nombre='Daemon Targaryen', apodo='El Príncipe Negro', edad=36, detalles='Lord de Rocadragón, Comandante de los Hijos del Dragón, Maestro de los barcos y Marina Real', foto='/static/daemon.png', casa_id=3)

    ### Agregar a la base de datos ###
    db.session.add(casa_1)
    db.session.add(casa_2)
    db.session.add(casa_3)
    db.session.add(miembro_1)
    db.session.add(miembro_2)
    db.session.add(miembro_3)
    db.session.add(miembro_4)
    db.session.add(miembro_5)
    db.session.add(miembro_6)
    db.session.add(miembro_7)
    db.session.add(miembro_8)
    db.session.add(miembro_9)

    # Guardar cambios
    db.session.commit()

