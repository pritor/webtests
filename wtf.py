from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, request
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    file = FileField('Файл')



@app.route('/form_sample', methods= ['GET', 'POST'])
def form_sample():
    form = LoginForm()
    if request.method == "GET":
        return render_template('form.html', title='Пример формы', form=form)
    elif request.method == "POST":

        print(request.form['login'])
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['age'])
        print(request.form['about'])
        print(request.form.get('accept'))
        print(request.form['sex'])
        return redirect("/success")


@app.route('/success')
def success():
    return render_template('success.html', title='Ожидание')

@app.route('/file_sample', methods=["GET","POST"])
def f_samp():
    form = LoginForm()
    if request.method == "GET":
        return render_template('file.html', title="Секретные файлы")
    elif request.method == "POST":
        f = request.files['file']
        print(f.read())
        return "Файл отправлен"


if __name__ == '__main__':
    app.run(port=8000, host='192.168.0.44')
