import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

db = SQLAlchemy(app)

# News Model
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(300))
    video_url = db.Column(db.String(300))
    area = db.Column(db.String(100)) # User area
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<News {self.title}>'

# Create DB
with app.app_context():
    db.create_all()

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    # Get filters
    area = request.args.get('area')
    category = request.args.get('category')
    
    query = News.query
    if area:
        query = query.filter_by(area=area)
    if category:
        query = query.filter_by(category=category)
        
    news_list = query.order_by(News.created_at.desc()).all()
    # Areas and categories for the filter buttons
    areas = db.session.query(News.area).distinct().all()
    categories = db.session.query(News.category).distinct().all()
    
    return render_template('index.html', news_list=news_list, areas=[a[0] for a in areas if a[0]], categories=[c[0] for c in categories if c[0]])

@app.route('/news/<int:id>')
def news_detail(id):
    news = News.query.get_or_404(id)
    return render_template('article.html', news=news)

@app.route('/upload', methods=['GET', 'POST'])
def upload_news():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        category = request.form.get('category')
        area = request.form.get('area')
        
        image_file = request.files.get('image')
        video_file = request.files.get('video')
        
        image_url = ""
        video_url = ""
        
        if image_file:
            filename = secure_filename(f"{datetime.now().timestamp()}_{image_file.filename}")
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_url = f"/uploads/{filename}"
            
        if video_file:
            filename = secure_filename(f"{datetime.now().timestamp()}_{video_file.filename}")
            video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            video_url = f"/uploads/{filename}"
            
        new_news = News(
            title=title,
            content=content,
            author=author,
            category=category,
            area=area,
            image_url=image_url,
            video_url=video_url
        )
        db.session.add(new_news)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
