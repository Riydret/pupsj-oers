from flask import Flask, render_template
from flask_wtf import Form
from wtforms import BooleanField, validators
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'STACKOVERFLOW'

class ExampleForm(Form):
    checkbox = BooleanField('Agree?', [validators.DataRequired(), ])
    equip = ["equip1","equip2","equip3"]
    fac = ["fac1","fac2","fac3"]
    for i in equip:
        i = BooleanField('Equipments',  [validators.DataRequired()])
    for j in fac:
        j = BooleanField('Facilities', [validators.InputRequired()])

@app.route('/', methods=['post', 'get'])
def home():
    form = ExampleForm()
    equip = ["equip1","equip2","equip3"]
    fac = ["fac1","fac2","fac3"]
    if form.validate_on_submit():
        for i in equip:
            return str(form.i.data)
        for j in fac:
            return str(form.j.data)
    else:
        return render_template('test.html', form=form,equip=equip,fac=fac)

if __name__ == '__main__':
    app.run(debug=True, port=5060)