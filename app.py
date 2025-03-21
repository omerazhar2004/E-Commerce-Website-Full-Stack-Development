from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "top secret password don't tell anyone this"

technologies = [
    { "name": "Stick Cooking Pan", "Price": "28 £", "description": "Effortlessly cook and clean with our premium non-stick pan. Even heat distribution for perfect meals every time.", "img_loc": "/static/Stick cooking pan.jpeg"},
    { "name": "Ski Jacket", "Price": "40 £", "description": "Stay warm and dry with our high-performance ski jacket. Advanced insulation and breathable waterproof design for ultimate comfort.", "img_loc": "/static/Ski Jacket.jpeg"},
    { "name": "Mountain Bike", "Price": "699.99 £", "description": "Explore rugged terrains with our durable mountain bike. Lightweight frame, responsive suspension, and precision gearing for total control.", "img_loc": "/static/Mountain Bike.jpeg" },
]
class OpinionForm(FlaskForm):
    opinion = StringField('Your Opinion: ',validators = [DataRequired(),Length(min=0,max=100)])
    submit = SubmitField('Submit')

@app.route('/')
def galleryPage():
    return render_template('index.html',technologies = technologies)



@app.route('/tech/<int:techId>', methods=['GET','POST'])
# def singleProductPage(techId):
#     return render_template('SingleTech.html', technology = technologies[techId])
def singleProductPage(techId):
    form = OpinionForm()
    if form.is_submitted():
        data = form.opinion.data
        return render_template('SingleTechOpinion.html', technology = technologies[techId],opinion = data)
    else:
        return render_template('SingleTech.html', technology = technologies[techId], form = form)

if __name__ == '__main__':
    app.run(debug=True)
