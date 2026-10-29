from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_project.db'
db=SQLAlchemy(app)

class UserSubmission(db.Model):

    __tablename__="user_submission"

    id=db.Column(db.Integer, primary_key=True)
    
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    message=db.Column(db.Text, nullable=True)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name=request.form.get('name')
    email=request.form.get('email')
    message=request.form.get('message')

    if not name or not email or not message:
        return "All Fileds Are Requied", 400

    new_entry=UserSubmission(name=name, email=email, message=message)
    db.session.add(new_entry)
    db.session.commit()

    return render_template('index.html', success=True)
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Now i want to check the stored data in the database
