# from flask import Blueprint, jsonify, request
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime
# from .models import db, bcrypt, User, Event, RSVP, ContactMessage
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# # Define blueprints for different functionalities
# main_bp = Blueprint('main', __name__)
# auth_bp = Blueprint('auth', __name__)
# event_bp = Blueprint('events', __name__)
# contact_bp = Blueprint('contact', __name__)
# user_bp = Blueprint('user', __name__)

# # Authentication routes
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('email', 'password')):
#         return jsonify({'error': 'Invalid input'}), 400
#     user = User.query.filter_by(email=data['email']).first()
#     if user and bcrypt.check_password_hash(user.password, data['password']):
#         access_token = create_access_token(identity=user.id)
#         return jsonify({'access_token': access_token}), 200
#     else:
#         return jsonify({'error': 'Invalid credentials'}), 401

# @auth_bp.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200

# # Main routes (user management)
# @main_bp.route('/test', methods=['GET'])
# def test_route():
#     return jsonify({'message': 'Blueprint is working!'}), 200

# @main_bp.route('/register', methods=['POST'])
# def register_user():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('username', 'email', 'password')):
#         return jsonify({'error': 'Invalid input'}), 400
#     hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
#     new_user = User(username=data['username'], email=data['email'], password=hashed_password)
#     try:
#         db.session.add(new_user)
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({'error': 'Username or email already exists'}), 409
#     return jsonify(new_user.as_dict()), 201

# # Event routes
# @event_bp.route('/events', methods=['POST'])
# def create_event():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('title', 'description', 'date', 'location', 'medium', 'startDate', 'endDate', 'startTime', 'endTime', 'maxParticipants', 'category', 'acceptReservation')):
#         return jsonify({'error': 'Invalid input'}), 400
#     try:
#         startDate = datetime.strptime(data['startDate'], '%Y-%m-%d').date()
#         endDate = datetime.strptime(data['endDate'], '%Y-%m-%d').date()
#         event = Event(
#             title=data['title'],
#             description=data['description'],
#             date=data['date'],
#             location=data['location'],
#             medium=data['medium'],
#             startDate=startDate,
#             endDate=endDate,
#             startTime=data['startTime'],
#             endTime=data['endTime'],
#             maxParticipants=data['maxParticipants'],
#             category=data['category'],
#             acceptReservation=data['acceptReservation'],
#             imageUrl=data.get('imageUrl')
#         )
#         db.session.add(event)
#         db.session.commit()
#         return jsonify({'message': 'Event created successfully'}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# @event_bp.route('/events', methods=['GET'])
# def get_events():
#     events = Event.query.all()
#     event_list = [event.as_dict() for event in events]
#     return jsonify(event_list), 200

# # Contact Message routes
# @contact_bp.route('/contact', methods=['POST'])
# def create_contact_message():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('name', 'email', 'message')):
#         return jsonify({'error': 'Invalid input'}), 400
#     try:
#         new_message = ContactMessage(
#             name=data['name'],
#             email=data['email'],
#             message=data['message']
#         )
#         db.session.add(new_message)
#         db.session.commit()
#         return jsonify({'message': 'Contact message sent successfully'}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# # User management routes
# @user_bp.route('/users/<int:user_id>', methods=['DELETE'])
# @jwt_required()
# def delete_user(user_id):
#     current_user_id = get_jwt_identity()
#     if current_user_id != user_id:
#         return jsonify({'error': 'Unauthorized'}), 401

#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     try:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({'message': 'User deleted successfully'}), 200
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# # Blueprint registration
# def register_blueprints(app):
#     app.register_blueprint(main_bp, url_prefix='/api')
#     app.register_blueprint(auth_bp, url_prefix='/api/auth')
#     app.register_blueprint(event_bp, url_prefix='/api')
#     app.register_blueprint(contact_bp, url_prefix='/api')
#     app.register_blueprint(user_bp, url_prefix='/api')
