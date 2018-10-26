from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# es nuestra abstracción de la base de datos
# en general, no vamos a laburar contra el engine, sino que se va a usar tras bambalinas
engine = create_engine("mysql+pymysql://root:@localhost:4000/dns_mapping", echo=True)
# este objeto va a contener la meta-información de nuestros mapeos
Base = declarative_base()
# este objeto session va a ser nuestro contrato con el ORM, va a ser el objeto por el cual nos vamos a comunicar
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    fullname = Column(String(150))
    password = Column(String(32))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


# crear la base
# ej.Base.metadata.create_all(ej.engine)

#new_user = ej.User(name='juan', fullname='pepe', password='perepepre')
#ej.session.add(new_user)
#ej.session.new
#ej.session.dirty
#ej.session.commit()


