from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

def add_dummy_data():
    dummy_books = [
        Book(title='Cien años de soledad', author='Gabriel García Márquez', year=1967),
        Book(title='Don Quijote de la Mancha', author='Miguel de Cervantes', year=1605),
        Book(title='La sombra del viento', author='Carlos Ruiz Zafón', year=2001),
        Book(title='El amor en los tiempos del cólera', author='Gabriel García Márquez', year=1985),
        Book(title='La casa de los espíritus', author='Isabel Allende', year=1982),
        Book(title='Rayuela', author='Julio Cortázar', year=1963),
        Book(title='Ficciones', author='Jorge Luis Borges', year=1944),
        Book(title='Pedro Páramo', author='Juan Rulfo', year=1955),
        Book(title='El túnel', author='Ernesto Sabato', year=1948),
        Book(title='Crónica de una muerte anunciada', author='Gabriel García Márquez', year=1981),
        Book(title='La ciudad y los perros', author='Mario Vargas Llosa', year=1963),
        Book(title='El Aleph', author='Jorge Luis Borges', year=1949),
        Book(title='La tregua', author='Mario Benedetti', year=1960),
        Book(title='Sobre héroes y tumbas', author='Ernesto Sabato', year=1961),
        Book(title='La fiesta del chivo', author='Mario Vargas Llosa', year=2000),
        Book(title='El coronel no tiene quien le escriba', author='Gabriel García Márquez', year=1961),
        Book(title='Los detectives salvajes', author='Roberto Bolaño', year=1998),
        Book(title='2666', author='Roberto Bolaño', year=2004),
        Book(title='La invención de Morel', author='Adolfo Bioy Casares', year=1940),
        Book(title='Aura', author='Carlos Fuentes', year=1962),
        Book(title='La región más transparente', author='Carlos Fuentes', year=1958),
        Book(title='El otoño del patriarca', author='Gabriel García Márquez', year=1975),
        Book(title='La muerte de Artemio Cruz', author='Carlos Fuentes', year=1962),
        Book(title='El laberinto de la soledad', author='Octavio Paz', year=1950),
        Book(title='La casa verde', author='Mario Vargas Llosa', year=1966),
        Book(title='El reino de este mundo', author='Alejo Carpentier', year=1949),
        Book(title='El siglo de las luces', author='Alejo Carpentier', year=1962),
        Book(title='La guerra del fin del mundo', author='Mario Vargas Llosa', year=1981),
        Book(title='El amor loco', author='André Breton', year=1937),
        Book(title='El beso de la mujer araña', author='Manuel Puig', year=1976),
        Book(title='El cartero de Neruda', author='Antonio Skármeta', year=1985),
        Book(title='El entenado', author='Juan José Saer', year=1983),
        Book(title='El extranjero', author='Albert Camus', year=1942),
        Book(title='El general en su laberinto', author='Gabriel García Márquez', year=1989),
        Book(title='El hombre que amaba a los perros', author='Leonardo Padura', year=2009),
        Book(title='El libro de arena', author='Jorge Luis Borges', year=1975),
        Book(title='El llano en llamas', author='Juan Rulfo', year=1953),
        Book(title='El lugar sin límites', author='José Donoso', year=1966),
        Book(title='El obsceno pájaro de la noche', author='José Donoso', year=1970),
        Book(title='El olvido que seremos', author='Héctor Abad Faciolince', year=2006),
        Book(title='El otoño del patriarca', author='Gabriel García Márquez', year=1975),
        Book(title='El país de las últimas cosas', author='Paul Auster', year=1987),
        Book(title='El paraíso en la otra esquina', author='Mario Vargas Llosa', year=2003),
        Book(title='El reino de este mundo', author='Alejo Carpentier', year=1949),
        Book(title='El ruido de las cosas al caer', author='Juan Gabriel Vásquez', year=2011),
        Book(title='El siglo de las luces', author='Alejo Carpentier', year=1962),
        Book(title='El túnel', author='Ernesto Sabato', year=1948),
        Book(title='El vuelo de la reina', author='Tomás Eloy Martínez', year=2002),
        Book(title='En busca del tiempo perdido', author='Marcel Proust', year=1913),
        Book(title='Ensayo sobre la ceguera', author='José Saramago', year=1995)
    ]
    db.session.bulk_save_objects(dummy_books)
    db.session.commit()
