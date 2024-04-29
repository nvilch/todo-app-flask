from flask import jsonify, request, abort
from app import app, db
from app.models import TodoItem, User
from datetime import datetime


@app.route('/todo_items', methods=['GET'])
def get_todo_items():
    todo_items = TodoItem.query.all()
    return jsonify([item.to_dict() for item in todo_items])

@app.route('/todo_items', methods=['POST'])
def create_todo_item():
    # Ensure that the request is not empty
    if not request.json or 'title' not in request.json or 'category' not in request.json:
        abort(400)
    todo_item = TodoItem(title=request.json['title'], category=request.json['category'], completed=request.json['completed'])
    if 'due_date' in request.json:
        todo_item.due_date = datetime.strptime(request.json['due_date'], '%Y-%m-%d').date()
    db.session.add(todo_item)
    db.session.commit()
    return jsonify(todo_item.to_dict()), 201

@app.route('/todo_items/<int:item_id>', methods=['GET'])
def get_todo_item(item_id):
    """
        Returns the specific item by using the provided item_id
    """
    todo_item = TodoItem.query.get_or_404(item_id)
    return jsonify(todo_item.to_dict())

@app.route('/todo_items/<int:item_id>', methods=['PUT'])
def update_todo_item(item_id):
    todo_item = TodoItem.guery.get_or_404(item_id)
    if 'title' in request.json:
        todo_item.title = request.json['title']
    if 'completed' in request.json:
        todo_item.completed = request.json['completed']
    if 'due_date' in request.json:
        todo_item.due_date = request.json['due_date']
    db.session.commit()
    return jsonify(todo_item.to_dict())

@app.route('/todo_items/<int:item_id>', methods=['DELETE'])
def delete_todo_item(item_id):
    todo_item = TodoItem.query.get_or_404(item_id)
    db.session.delete(todo_item)
    db.session.commit()
    return jsonify({'result': True})

# @app.route('/register', methods=['POST'])
# def create_new_user():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
#     first_name = data.get('first_name')
#     last_name = data.get('last_name')

#     # Check if any of the required fields are missing
#     if not username or not password or not first_name or not last_name:
#         return jsonify({'error': 'All fields are required'}), 400
    
#     # Check if the username already exists
#     if User.query.filter_by(username=username).first():
#         return jsonify({'error': 'Username already exists'}), 400
    
#     # Create new user
#     new_user = User(username=username, first_name=first_name, last_name=last_name)
#     new_user.set_password(password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User registration successful'}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')

#     # Check if username or password is missing
#     if not username or not password:
#         return jsonify({'error': 'Username and password required'}), 400
    
#     # Find user by username
#     user = User.query.filter_by(username=username).first()

#     # Check if user exists and password is correct
#     if not user or not user.check_password(password):
#         return jsonify({'error': 'Invalid username or password'}), 401
    
#     # If login successful:
#     session['user_id'] = user.id
#     return jsonify({'message': 'Login successful'}), 200

# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return jsonify({'message': 'Logout successful'}), 200