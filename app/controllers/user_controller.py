from flask import Blueprint, render_template

login_route = Blueprint('login_route', __name__)
register_route = Blueprint('register_route', __name__)

@login_route.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']

    #     user = User.query.filter_by(email=email).first()
    #     if user and check_password_hash(user.password, password):
    #         login_user(user)
    #         flash('Login successful!', 'success')
    #         return redirect(url_for('dashboard'))  # Rediriger vers le tableau de bord après la connexion
    #     else:
    #         flash('Login failed. Check your email and/or password', 'danger')
    #         return redirect(url_for('login'))

    return render_template('login.html')

@register_route.route('/register', methods=['GET', 'POST'])
def register():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     email = request.form['email']
    #     password = request.form['password']

    #     # Vérifier si l'utilisateur existe déjà
    #     user_exists = User.query.filter_by(email=email).first()
    #     if user_exists:
    #         flash('Email already registered', 'danger')
    #         return redirect(url_for('register'))
        
    #     # Créer un nouvel utilisateur
    #     hashed_password = generate_password_hash(password, method='sha256')
    #     new_user = User(username=username, email=email, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()

    #     flash('Your account has been created!', 'success')
    #     return redirect(url_for('home'))
    return render_template('register.html')
