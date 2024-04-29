from app import db, app
from bcrypt import hashpw, gensalt

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'completed': self.completed,
            'due_date': self.due_date
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    
    def set_password(self, password):
        salt = gensalt()
        self.password_hash = hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        return hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8')) == self.password_hash
    

with app.app_context():
    db.create_all()