from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# Initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = 'supersecretkey'

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100), nullable=False)
    phonenum = db.Column(db.String(15))  # You may want to adjust the length based on expected phone number formats
    country = db.Column(db.String(100))
    url = db.Column(db.String(200))
    address = db.Column(db.Text)
    skills = db.Column(db.String(200))  # Adjust the length depending on your expected input size
    certifications = db.Column(db.Text)
    languages = db.Column(db.String(200))
    job_title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    employment_dates = db.Column(db.String(100))
    work_experience = db.Column(db.Text)
    awards = db.Column(db.String(200))
    summary = db.Column(db.Text)

# Forms for login and registration
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration Successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login Successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        dob = request.form.get('dob')
        phonenum = request.form.get('phonenum')
        country = request.form.get('country')
        url = request.form.get('url')
        address = request.form.get('address')
        skills = request.form.get('skills')
        certifications = request.form.get('certifications')
        languages = request.form.get('languages')
        job_title = request.form.get('job_title')
        company = request.form.get('company')
        employment_dates = request.form.get('employment_dates')
        work_experience = request.form.get('work_experience')
        awards = request.form.get('awards')
        summary = request.form.get('summary')

        new_student = Student(name=name,
                               email=email,dob=dob,phonenum=phonenum,
                               country=country,url=url,
                               address=address,skills=skills,
                               certifications=certifications,languages=languages,
                               job_title=job_title,company=company,
                               employment_dates=employment_dates,work_experience=work_experience,
                               awards=awards,summary=summary)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return render_template('test.html')
    #students = Student.query.all()
    return render_template('dashboard.html')


@app.route('/level1')
def aptlevel():
    return render_template('testfiles/aptitude1.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # db.session.query(Student).delete()  # Clear all data in the Student table
    db.session.commit()
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))


# @app.route('/calculatelevel1',methods='POST')
# def rishana():
#     return render_template('rishan.html')


# Initialize the database
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
