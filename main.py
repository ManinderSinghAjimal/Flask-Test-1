from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so so secret'

posts = [
    {
        'name': "maninder",
        'address': "602 of testing street",
        'phone': 'not given'
    },
    {
        'name': "maninder singh",
        'address': "802 of testing street",
        'phone': 'not given noo noo'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="homepage")

@app.route('/posts')
def posts():
    post = posts
    return render_template('posts.html',title="posts", post=post)


if __name__=="__main__":
    app.run(debug=True)