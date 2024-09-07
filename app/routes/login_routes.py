from flask import Blueprint, render_template

login_route = Blueprint('login_route', __name__)

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