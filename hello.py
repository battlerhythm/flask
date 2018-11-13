from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User {username}'.format(username=username)

@app.route('/post/<int:id_post>')
def show_post(id_post):
    return 'Post {id_post}'.format(id_post=id_post)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath {subpath}'.format(subpath=subpath)

# Converter types:
# string   (default) accepts any text without a slash
# int	   accepts positive integers
# float	   accepts positive floating point values
# path	   like string but also accepts slashes
# uuid	   accepts UUID strings

if __name__ == '__main__':
    app.run()