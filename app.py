from flask import Flask, render_template, request , redirect
import os
from os.path import join, dirname, realpath
import pandas as pd
from VNS import *
from BB import *
from Clark_wright import *

#création de l'applcation web Flask 
app = Flask(__name__, template_folder='templates')

# activer le mode debugging 
app.config["DEBUG"] = True

# enregistrer le fichier csv 
UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

#exécution de la Home page 
@app.route("/")
def hello():
    return render_template('template1.html')

#choix de la méthode d'optimisation 
@app.route("/page2", methods=['GET','POST'])
def execution():
    if request.method=='POST':
        algo = request.form['algorithm']
        if algo=='VNS':
            return redirect('/page3')
        if algo=='BB':
            return redirect('/page5')
        if algo=='CW':
            return redirect ('/page7')
            
    return render_template('template1.html')
    
    
#exécution de la métaheuristique de VNS 
@app.route("/page3")
def VNS_before():
    return render_template('VNS.html')


@app.route("/page4", methods=['GET','POST'])
def VNS():
    if request.method=='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
        #VNS
        chemin= Variable_neighborhood_search(file_path).optimum
        distance_opt= Variable_neighborhood_search(file_path).optimum_dist

    return render_template('template2.html',  variable=chemin , variable2=distance_opt )

#Exécution de l'algorithme Branch and Bound 
@app.route("/page5")
def BB_before():
    return render_template('BB.html')

@app.route("/page6", methods=['GET', 'POST'])
def BB():
   if request.method=='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
            resultat=run()
            route= chemin()
            cities= villes(file_path)
           
        return render_template('template3.html', variable=resultat , variable2=route, var= cities )

#exécution de l'algorithme Clark and Wright
@app.route("/page7")
def CW_before():
    return render_template('CW.html')

@app.route("/page8", methods=['POST','GET'])
def CW():
    if request.method=='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
            result=arcs()
            C= Cities(file_path)
    return render_template('template4.html' , var=result , var2= C)



if (__name__ == "__main__"):
     app.run(port = 5000)
