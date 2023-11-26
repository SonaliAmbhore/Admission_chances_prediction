from flask import Flask,jsonify,request,render_template
import config
from Project_app.Utils import AdmissionChances



app = Flask(__name__)

#####################################################################################
###################################### Home API######################################
#####################################################################################
@app.route("/")
def name():
    print("Welcome to home API")
    return render_template("home.html")

@app.route("/predict",methods = ['POST'])
def Admission_pred():
    
     data = request.form
     
     GRE_Score = eval(data['GRE_Score'])
     TOEFL_Score = eval(data['TOEFL_Score'])
     University_Rating = eval(data['University_Rating'])
     SOP = eval(data['SOP'])
     LOR = eval(data['LOR'])
     CGPA = eval(data['CGPA'])
     Research = eval(data['Research'])
     

     Adm_chs = AdmissionChances(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
     chances = Adm_chs.get_predict_chances()
     return jsonify({"Result" : f"Predicted Admission Chances are {chances}"}) 
        
           
       
if __name__ == '__ main__':
    app.run(port = config.PORT_NUMBER,debug = True,host='0.0.0.0')   

