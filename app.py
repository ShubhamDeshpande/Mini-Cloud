from flask import Flask,abort,render_template,request,redirect,url_for,send_file
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config['FOLDER_NAME'] = './uploads' 
@app.route('/')
def index():
    pass

@app.route('/login',methods=['GET','POST'])
def login():
    print(str(request.form))
@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['FOLDER_NAME'],filename))
        return render_template("success.html")
    return render_template('upload.html')

@app.route("/download",methods=['GET','POST'])
def download():
    if request.method=='GET':
        file_list=os.listdir(app.config['FOLDER_NAME'])
        return render_template('get_files.html',file_list=file_list)
    print(request.method)
    print(str(request.form))
    file_name=request.form['selected_file']
    return send_file(os.path.join(app.config['FOLDER_NAME'],file_name),as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
