from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
myApp=Flask(__name__)
myApp.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
db=SQLAlchemy(myApp)
class Blog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    intro=db.Column(db.Text, nullable=False)
    data_=db.Column(db.DateTime,default=datetime.utcnow())
    main_text=db.Column(db.Text, nullable=False)
    def __repr__(self):
        return 'Blog %r'%self.id


@myApp.route('/')
def index():
    notes = Blog.query.all()
    return render_template('index1.html',notes=notes)
@myApp.route('/my_adress')
def addr():
    names = [{'name': 'Алекс Масловський', 'e-mail': 'alexus450@gmail.com', 'cell number': '0973410024'},
             {'name': 'Ivan', 'email': '12354@gmail.com', 'call number': '0664297574'},
             {"name": "Антон Юксін", "e-mail": 'qpowertrain@gmail.com', "number": "06668*****"},
             {'name': 'Dennis', 'e-mail': 'bachynskyi.denys@pml.if.ua', 'phone-number': '3001113344'},
             {'name': 'Стефунін Арсен', 'email': 'stefunin.arsen@pml.if.ua', 'cell number': '+380672925255'}
             ]

    return render_template("my_address.html",dnames=names)
@myApp.route('/articles',methods=["POST","GET"])
def article():
    if request.method=='POST':
        title=request.form['title']
        intro=request.form['intro']
        main_text=request.form['main_text']
        blog=Blog(title=title, intro=intro, main_text=main_text)

        try:
            db.session.add(blog)
            db.session.commit()
            return redirect('/')
        except:
            return 'error'
    else:
         return render_template('articles.html')



@myApp.route('/about1')
def about():
    variable="Віталій Романюк"
    return render_template("about.html",taka=variable)

@myApp.route('/sign_in',methods=["POST","GET"])
def sign():
    if request.method=="POST":
        nik=request.form["nik"]
        pasw=request.form['psw']
        return nik + pasw
        return "<h2>'Ok'</h2>"
    return render_template("sign_in.html")
@myApp.route('/link/<int:id>')
def det_post(id):
    lb=Blog.query.get(id)

    return render_template('post_det.html',lb=lb)
@myApp.route("/post_det/<int:id>/Delete")
def delete(id):

   delete_articles=Blog.query.get_or_404(id)
   try:
      db.session.delete(delete_articles)
      db.session.commit()
      return redirect('/')
   except:
      return('Error')





if __name__ == '__main__':
    myApp.run(debug=True)