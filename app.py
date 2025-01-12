from flask import Flask, render_template, redirect, url_for, request, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pet(db.Model):
    petID = db.Column(db.Integer, primary_key=True, nullable=False)
    petType = db.Column(db.String(255))
    petBreed = db.Column(db.String(255))
    petAge = db.Column(db.Integer)
    isAdopted = db.Column(db.Boolean)

# home route
@app.route('/')
def index():
    return redirect(url_for('login'))

# login route
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        role = request.form['role']
        if role == "admin":
            return redirect(url_for('admin_pets'))
        elif role == "user":
            return redirect(url_for('user_pets'))

# routes of admin
@app.route('/admin/pets', methods=['GET','POST','PUT','DELETE'])
def admin_pets():
    if request.method == "GET":
        pets = Pet.query.all()
        return render_template('base.html', pets=pets)
    elif request.method == "POST":
        # pets = Pet.query.all()
        # return render_template('base.html', pets=pets)
        petType = request.form['type']  # Get form data
        petBreed = request.form['breed']
        petAge = request.form['age']
        isadopted = request.form['isAdopted']
        isAdopted = False
        if isadopted == "True":
            isAdopted = True

        print(petAge)
        print(isAdopted)

        pet = Pet(
            petType=petType,
            petBreed=petBreed,
            petAge=petAge,
            isAdopted=isAdopted
        )
        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('admin_pets'))
    elif request.method == "PUT":
        petId = request.form['id']
        pet = Pet.query.get_or_404(petId)

        pet.petType = request.form['type']
        pet.petBreed = request.form['breed']
        pet.petAge = request.form['age']
        isadopted = request.form['isAdopted']
        isAdopted = False
        if isadopted == "True":
            isAdopted = True
        if isAdopted :
            pet.isAdopted = True
        else :
            pet.isAdopted = False

        db.session.commit()
        return "Pet Updated", 200
    elif request.method == "DELETE":
        petId = request.form['id']
        pet = Pet.query.get_or_404(petId)
        db.session.delete(pet)
        db.session.commit()
        return "Pet Deleted !", 200

# routes of user
@app.route('/pets', methods=['GET', 'POST'])
def user_pets():
    if request.method == "GET":
        pets = list()
        return render_template('user_view.html', pets=pets)
    elif request.method == "POST":
        petType = request.form['type']
        pets = Pet.query.filter(Pet.petType.ilike(f'%{petType}%')).all()
        return render_template('user_view.html', pets=pets)
    
@app.route('/pets/adopt', methods=['GET','POST'])
def user_pets_adopt():
    if request.method == "GET":
        return render_template('user_adopt.html')
    elif request.method == "POST":
        petId = request.form['id']
        pet = Pet.query.get_or_404(petId)
        if pet.isAdopted == True:
            return "Pet is already adopted"
        else:
            pet.isAdopted = True
            db.session.commit()
            return 'Pet adopted successfully', 200
    
@app.route('/pets/return', methods=['GET','POST'])
def user_pets_return():
    if request.method == "GET":
        return render_template('user_return.html')
    elif request.method == "POST":
        petId = request.form['id']
        pet = Pet.query.get_or_404(petId)
        pet.isAdopted = False
        db.session.commit()
        return 'Pet returned successfully', 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)