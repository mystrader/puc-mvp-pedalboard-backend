from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializar SQLAlchemy
db = SQLAlchemy()

class Pedalboard(db.Model):
    """Modelo para pedalboards"""
    __tablename__ = 'pedalboards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamento com pedais
    pedals = db.relationship('Pedal', backref='pedalboard', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Pedalboard {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'pedals': [pedal.to_dict() for pedal in self.pedals]
        }

class Pedal(db.Model):
    """Modelo para pedais"""
    __tablename__ = 'pedals'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # ex: distortion, delay, reverb
    description = db.Column(db.Text)
    pedalboard_id = db.Column(db.Integer, db.ForeignKey('pedalboards.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Pedal {self.brand} {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'description': self.description,
            'pedalboard_id': self.pedalboard_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }