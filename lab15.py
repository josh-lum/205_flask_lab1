from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


myapp = Flask(__name__)
bootstrap = Bootstrap5(myapp)


@myapp.route('/')
def hello_world():
    return '''
    <h1>Hello World</h1>
    <p>Genevieve M. : afaik </p>
    <p>Matthew G. : gtg </p>
    <p>Eric S. : lol </p>
    '''

@myapp.route('/josh')
def favorite_acronym():
    return render_template('template.html')

if __name__ == '__main__':
    myapp.run(debug=True)
