from flask import Flask, render_template, url_for, request, redirect, config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/yevgeny/PycharmProjects/NoName/venv/articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/Poster')
def Poster():
    return render_template("Poster.html")

# Read All Articles
@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date).all()
    return render_template("posts.html", articles=articles)
# Delete Article
@app.route('/posts/<int:id>/delete')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "Delete article failed"
# Update Article
@app.route('/posts/<int:id>/update', methods=['POST','GET'])
def update_article(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return "Something gone wrong, Article update failed"
    else:
        return render_template("post_update.html", article=article)

# Open full article text
@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)

# Create New Article
@app.route('/create-article', methods=['POST','GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return "Something gone wrong, Article is not added, please check database is up,\n Error:, ",print(e)
    else:
        return render_template("create-article.html")

if __name__ == "__main__":
    app.run(debug=True, port=5007)