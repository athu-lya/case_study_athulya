from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
  picked_model = pickle.load(open("model.pkl","rb"))
  if request.method=='POST':
    gender = request.form['Gender']
    print(gender)
    age = request.form['Age']
    print(age)
    estimated_salary = request.form['EstimatedSalary']
    print(estimated_salary)
    model = pickle.load(open('model.pkl','rb'))
    prediction=model.predict([[bool(gender),int(age),float(estimated_salary)]])
    if prediction[0] == 1:
        print('Purchase')
    else:
        print('Non Purchase')

if __name__=='__main__':
    app.run()


