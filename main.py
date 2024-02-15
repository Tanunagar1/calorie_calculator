from flask import Flask, render_template,request
from flask.views import MethodView
from wtforms import Form, StringField, FloatField, IntegerField, SubmitField
import function

app = Flask(__name__)


class Homepage(MethodView):
    def get(self):
        return render_template("index.html")


class UserForm(Form):
    weight = FloatField('Weight (kg):')
    height = FloatField('Height (inch):')
    age = IntegerField('Age:')
    country = StringField('Country:')
    city = StringField('City:')
    button = SubmitField("Calculate")


class UserFormpage(MethodView):
    def get(self):
        user_form = UserForm()
        return render_template("userformpage.html", userform=user_form)

    def post(self):
        form = UserForm(request.form)
        if form.validate():
            country = form.country.data
            city = form.city.data
            weight = form.weight.data
            height = form.height.data
            age = form.age.data

            tempreture = function.temp.get_temprature(country=country, city=city)
            calculatecalorie = function.CalculateCalorie(weight=weight, height=height, age=age)

            result = calculatecalorie.calculate(tempreture)
            return render_template("userformpage.html", userform=form, result=result)
        else:
            message="Form validation failed"
            return render_template("userformpage.html", userform=form, result=None,message=message)



app.add_url_rule("/", view_func=Homepage.as_view("home_page"))
app.add_url_rule("/user_form_page", view_func=UserFormpage.as_view("user_form_page"))


app.run(debug=True)
