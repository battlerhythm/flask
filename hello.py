from flask import Flask
app = Flask(__name__)


# Routing

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World'


# Variable Rules

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


# Unique URLs / Redirection Behavior

@app.route('/projects/')
def projects():
    # It’s similar to a folder in a file system.
    # If you access the URL without a trailing slash,
    # Flask redirects you to the canonical URL with the trailing slash.
    return 'The project page'

@app.route('/about')
def about():
    # It’s similar to the pathname of a file.
    # Accessing the URL with a trailing slash produces a 404 “Not Found” error. 
    # This helps keep URLs unique for these resources, 
    # which helps search engines avoid indexing the same page twice.
    return 'The about page'


if __name__ == '__main__':
    app.run()