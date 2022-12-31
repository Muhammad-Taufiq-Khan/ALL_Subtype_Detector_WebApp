from flask import Flask, render_template, request #,redirect, flash
from main import getPrediction
#Save images to the 'static' folder as Flask serves images from this directory
UPLOAD_FOLDER = 'static/images/'

#Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")
app.debug=True 

# routes
@app.route("/home")
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html")


@app.route("/notebook")
def notebook():
	return render_template("notebook.html")



@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = UPLOAD_FOLDER + img.filename	
		img.save(img_path)

		p = getPrediction(img_path)
		if p == 0:
			result = "Benign"
		elif p == 1:
			result= "Early Pre-B"
		elif p ==2:
			result= "Pre-B"
		else: 
			result= "Pro-B"



	return render_template("index_report.html", prediction = result, img_path = img_path)

if __name__ == "__main__":
    app.run()

