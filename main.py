from flask import Flask, jsonify
from flask_cors import CORS
from model.model import db, Pedalboard, Pedal
from schemas.schema import (
    PedalboardBase, PedalboardCreateSchema, PedalboardSchema,
    PedalBase, PedalCreateSchema, PedalSchema,
    PedalboardPathSchema, PedalPathSchema
)

# Criar aplicação Flask
app = Flask(__name__)

# Configurar CORS
CORS(app)

# Configurar banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedalboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy com a app
db.init_app(app)

# Criar tabelas
with app.app_context():
    db.create_all()

# Rotas para pedalboards
@app.route('/api/pedalboards', methods=['GET'])
def list_pedalboards():
    """Lista todos os pedalboards"""
    pedalboards = Pedalboard.query.all()
    return jsonify([pb.to_dict() for pb in pedalboards])

@app.route('/api/pedalboards', methods=['POST'])
def create_pedalboard():
    """Cria um novo pedalboard"""
    from flask import request
    data = request.get_json()
    
    pedalboard = Pedalboard(
        name=data['name'],
        description=data.get('description'),
        user_id=data['user_id']
    )
    db.session.add(pedalboard)
    db.session.commit()
    return jsonify(pedalboard.to_dict()), 201

@app.route('/api/pedalboards/<int:pedalboard_id>', methods=['GET'])
def get_pedalboard(pedalboard_id):
    """Obtém um pedalboard específico"""
    pedalboard = Pedalboard.query.get_or_404(pedalboard_id)
    return jsonify(pedalboard.to_dict())

@app.route('/api/pedalboards/<int:pedalboard_id>', methods=['PUT'])
def update_pedalboard(pedalboard_id):
    """Atualiza um pedalboard"""
    from flask import request
    pedalboard = Pedalboard.query.get_or_404(pedalboard_id)
    data = request.get_json()
    
    pedalboard.name = data['name']
    pedalboard.description = data.get('description')
    db.session.commit()
    return jsonify(pedalboard.to_dict())

@app.route('/api/pedalboards/<int:pedalboard_id>', methods=['DELETE'])
def delete_pedalboard(pedalboard_id):
    """Deleta um pedalboard"""
    pedalboard = Pedalboard.query.get_or_404(pedalboard_id)
    db.session.delete(pedalboard)
    db.session.commit()
    return jsonify({'message': 'Pedalboard deletado com sucesso'}), 200

# Rotas para pedais
@app.route('/api/pedals', methods=['GET'])
def list_pedals():
    """Lista todos os pedais"""
    pedals = Pedal.query.all()
    return jsonify([p.to_dict() for p in pedals])

@app.route('/api/pedals', methods=['POST'])
def create_pedal():
    """Cria um novo pedal"""
    from flask import request
    data = request.get_json()
    
    pedal = Pedal(
        name=data['name'],
        brand=data['brand'],
        category=data['category'],
        description=data.get('description'),
        pedalboard_id=data['pedalboard_id']
    )
    db.session.add(pedal)
    db.session.commit()
    return jsonify(pedal.to_dict()), 201

@app.route('/api/pedals/<int:pedal_id>', methods=['GET'])
def get_pedal(pedal_id):
    """Obtém um pedal específico"""
    pedal = Pedal.query.get_or_404(pedal_id)
    return jsonify(pedal.to_dict())

@app.route('/api/pedals/<int:pedal_id>', methods=['PUT'])
def update_pedal(pedal_id):
    """Atualiza um pedal"""
    from flask import request
    pedal = Pedal.query.get_or_404(pedal_id)
    data = request.get_json()
    
    pedal.name = data['name']
    pedal.brand = data['brand']
    pedal.category = data['category']
    pedal.description = data.get('description')
    pedal.pedalboard_id = data['pedalboard_id']
    db.session.commit()
    return jsonify(pedal.to_dict())

@app.route('/api/pedals/<int:pedal_id>', methods=['DELETE'])
def delete_pedal(pedal_id):
    """Deleta um pedal"""
    pedal = Pedal.query.get_or_404(pedal_id)
    db.session.delete(pedal)
    db.session.commit()
    return jsonify({'message': 'Pedal deletado com sucesso'}), 200

# Rota de teste
@app.route('/')
def home():
    return jsonify({
        'message': 'Pedalboard API está funcionando!',
        'endpoints': {
            'pedalboards': '/api/pedalboards',
            'pedals': '/api/pedals'
        }
    })

# Endpoint para OpenAPI JSON
@app.route('/openapi.json')
def openapi_json():
    """Especificação OpenAPI da API"""
    return jsonify({
        "openapi": "3.0.0",
        "info": {
            "title": "Pedalboard API",
            "version": "1.0.0",
            "description": "API para gerenciar pedalboards e pedais"
        },
        "servers": [
            {
                "url": "http://localhost:5002",
                "description": "Servidor de desenvolvimento"
            }
        ],
        "tags": [
            {
                "name": "Pedalboards",
                "description": "Operações relacionadas aos pedalboards"
            },
            {
                "name": "Pedais",
                "description": "Operações relacionadas aos pedais"
            }
        ],
        "paths": {
            "/api/pedalboards": {
                "get": {
                    "tags": ["Pedalboards"],
                    "summary": "Listar pedalboards",
                    "responses": {
                        "200": {
                            "description": "Lista de pedalboards",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Pedalboard"}
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "tags": ["Pedalboards"],
                    "summary": "Criar pedalboard",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/PedalboardCreate"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Pedalboard criado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedalboard"}
                                }
                            }
                        }
                    }
                }
            },
            "/api/pedalboards/{pedalboard_id}": {
                "get": {
                    "tags": ["Pedalboards"],
                    "summary": "Obter pedalboard",
                    "parameters": [
                        {
                            "name": "pedalboard_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Pedalboard encontrado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedalboard"}
                                }
                            }
                        }
                    }
                },
                "put": {
                    "tags": ["Pedalboards"],
                    "summary": "Atualizar pedalboard",
                    "parameters": [
                        {
                            "name": "pedalboard_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/PedalboardCreate"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Pedalboard atualizado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedalboard"}
                                }
                            }
                        }
                    }
                },
                "delete": {
                    "tags": ["Pedalboards"],
                    "summary": "Deletar pedalboard",
                    "parameters": [
                        {
                            "name": "pedalboard_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Pedalboard deletado",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/api/pedals": {
                "get": {
                    "tags": ["Pedais"],
                    "summary": "Listar pedais",
                    "responses": {
                        "200": {
                            "description": "Lista de pedais",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Pedal"}
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "tags": ["Pedais"],
                    "summary": "Criar pedal",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/PedalCreate"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Pedal criado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedal"}
                                }
                            }
                        }
                    }
                }
            },
            "/api/pedals/{pedal_id}": {
                "get": {
                    "tags": ["Pedais"],
                    "summary": "Obter pedal",
                    "parameters": [
                        {
                            "name": "pedal_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Pedal encontrado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedal"}
                                }
                            }
                        }
                    }
                },
                "put": {
                    "tags": ["Pedais"],
                    "summary": "Atualizar pedal",
                    "parameters": [
                        {
                            "name": "pedal_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/PedalCreate"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Pedal atualizado",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pedal"}
                                }
                            }
                        }
                    }
                },
                "delete": {
                    "tags": ["Pedais"],
                    "summary": "Deletar pedal",
                    "parameters": [
                        {
                            "name": "pedal_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Pedal deletado",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "Pedalboard": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "user_id": {"type": "integer"},
                        "created_at": {"type": "string", "format": "date-time"},
                        "updated_at": {"type": "string", "format": "date-time"},
                        "pedals": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Pedal"}
                        }
                    }
                },
                "PedalboardCreate": {
                    "type": "object",
                    "required": ["name", "user_id"],
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "user_id": {"type": "integer"}
                    }
                },
                "Pedal": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "brand": {"type": "string"},
                        "category": {"type": "string"},
                        "description": {"type": "string"},
                        "pedalboard_id": {"type": "integer"},
                        "created_at": {"type": "string", "format": "date-time"},
                        "updated_at": {"type": "string", "format": "date-time"}
                    }
                },
                "PedalCreate": {
                    "type": "object",
                    "required": ["name", "brand", "category", "pedalboard_id"],
                    "properties": {
                        "name": {"type": "string"},
                        "brand": {"type": "string"},
                        "category": {"type": "string"},
                        "description": {"type": "string"},
                        "pedalboard_id": {"type": "integer"}
                    }
                }
            }
        }
    })

# Endpoint para Swagger UI
@app.route('/swagger')
def swagger_ui():
    """Interface Swagger para documentação da API"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pedalboard API - Swagger UI</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" />
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
        <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-standalone-preset.js"></script>
        <script>
            window.onload = function() {
                const ui = SwaggerUIBundle({
                    url: '/openapi.json',
                    dom_id: '#swagger-ui',
                    deepLinking: true,
                    presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
                    layout: "StandaloneLayout"
                });
            };
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)