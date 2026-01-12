# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Usuario(db.Model):

    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)

    #__Usuario_FIELDS__
    nombre = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    telefono = db.Column(db.String(255),  nullable=True)
    imagen = db.Column(db.String(255),  nullable=True)
    direccion = db.Column(db.String(255),  nullable=True)
    ciudad = db.Column(db.String(255),  nullable=True)
    background = db.Column(db.String(255),  nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Usuario_FIELDS__END

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)


class Sliders(db.Model):

    __tablename__ = 'Sliders'

    id = db.Column(db.Integer, primary_key=True)

    #__Sliders_FIELDS__
    nombre = db.Column(db.String(255),  nullable=True)
    imagenes = db.Column(db.Text, nullable=True)
    descripcion = db.Column(db.String(255),  nullable=True)
    activo = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Sliders_FIELDS__END

    def __init__(self, **kwargs):
        super(Sliders, self).__init__(**kwargs)


class Mensajes(db.Model):

    __tablename__ = 'Mensajes'

    id = db.Column(db.Integer, primary_key=True)

    #__Mensajes_FIELDS__
    asunto = db.Column(db.String(255),  nullable=True)
    contendido = db.Column(db.Text, nullable=True)
    respuesta = db.Column(db.Boolean, nullable=True)

    #__Mensajes_FIELDS__END

    def __init__(self, **kwargs):
        super(Mensajes, self).__init__(**kwargs)


class Nota(db.Model):

    __tablename__ = 'Nota'

    id = db.Column(db.Integer, primary_key=True)

    #__Nota_FIELDS__
    icono = db.Column(db.String(255),  nullable=True)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Nota_FIELDS__END

    def __init__(self, **kwargs):
        super(Nota, self).__init__(**kwargs)


class Testimonio(db.Model):

    __tablename__ = 'Testimonio'

    id = db.Column(db.Integer, primary_key=True)

    #__Testimonio_FIELDS__
    contenido = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(255),  nullable=True)

    #__Testimonio_FIELDS__END

    def __init__(self, **kwargs):
        super(Testimonio, self).__init__(**kwargs)


class Post(db.Model):

    __tablename__ = 'Post'

    id = db.Column(db.Integer, primary_key=True)

    #__Post_FIELDS__
    titulo = db.Column(db.String(255),  nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    respuesta = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(255),  nullable=True)
    public_id = db.Column(db.String(255),  nullable=True)

    #__Post_FIELDS__END

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)


class Comentario(db.Model):

    __tablename__ = 'Comentario'

    id = db.Column(db.Integer, primary_key=True)

    #__Comentario_FIELDS__
    parent_id = db.Column(db.Integer, nullable=True)
    ceated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Comentario_FIELDS__END

    def __init__(self, **kwargs):
        super(Comentario, self).__init__(**kwargs)


class Notificacion(db.Model):

    __tablename__ = 'Notificacion'

    id = db.Column(db.Integer, primary_key=True)

    #__Notificacion_FIELDS__
    is_read = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Notificacion_FIELDS__END

    def __init__(self, **kwargs):
        super(Notificacion, self).__init__(**kwargs)


class Productos(db.Model):

    __tablename__ = 'Productos'

    id = db.Column(db.Integer, primary_key=True)

    #__Productos_FIELDS__
    nombre = db.Column(db.String(255),  nullable=True)
    precio = db.Column(db.Integer, nullable=True)
    provehedor = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=True)
    salida = db.Column(db.Integer, nullable=True)
    imagen = db.Column(db.String(255),  nullable=True)

    #__Productos_FIELDS__END

    def __init__(self, **kwargs):
        super(Productos, self).__init__(**kwargs)


class Sermones(db.Model):

    __tablename__ = 'Sermones'

    id = db.Column(db.Integer, primary_key=True)

    #__Sermones_FIELDS__
    titulo = db.Column(db.String(255),  nullable=True)
    descripcion = db.Column(db.String(255),  nullable=True)
    contendido = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(255),  nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    sitio = db.Column(db.String(255),  nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Sermones_FIELDS__END

    def __init__(self, **kwargs):
        super(Sermones, self).__init__(**kwargs)



#__MODELS__END
