from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone,timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

TIMEZONE = timezone(timedelta(hours=0))
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(TIMEZONE), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET','POST'])
def hello_world():
        if request.method=='POST':
            title = request.form['title']
            desc = request.form['desc']
            print(title)
            print(desc)
            print("post")
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        alltodo= Todo.query.all()
        return render_template('index.html',alltodo= alltodo)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'



@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        
        
        db.session.commit()
        return redirect('/') 
    todo = Todo.query.filter_by(sno=sno).first()
    
    
    # if request.method == 'POST':
    #     todo.title = request.form['title']
    #     todo.desc = request.form['desc']
    #     db.session.commit()
    #     return redirect('/')
    
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
   todo = Todo.query.filter_by(sno=sno).first()
   db.session.delete(todo)
   db.session.commit()
   return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)




     










  
