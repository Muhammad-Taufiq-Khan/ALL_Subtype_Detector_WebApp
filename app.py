from flask import Flask, render_template, request#redirect, flash
# from keras.models import load_model
# from keras.preprocessing import image
# from werkzeug.utils import secure_filename
# import os
from main import getPrediction
# from flask import Flask, render_template, request, redirect, flash
# from werkzeug.utils import secure_filename
# from main import getPrediction   ****
# import os

#Save images to the 'static' folder as Flask serves images from this directory
UPLOAD_FOLDER = 'static/images/'

#Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")
app.debug=False 

# app.secret_key = "secret key"

# #Define the upload folder to save images uploaded by the user. 
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# #Define the route to be home. 
# #The decorator below links the relative route of the URL to the function it is decorating.
# #Here, index function is with '/', our root directory. 
# #Running the app sends us to index.html.
# #Note that render_template means it looks for the file in the templates folder. 
# @app.route('/')
# def index():
#     return render_template('index.html')

# #Define the route to be home. 
# #The decorator below links the relative route of the URL to the function it is decorating.
# #Here, index function is with '/', our root directory. 
# #Running the app sends us to index.html.
# #Note that render_template means it looks for the file in the templates folder. 
# #Add Post method to the decorator to allow for form submission. 
# @app.route('/', methods=['POST'])
# def submit_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No file selected for uploading')
#             return redirect(request.url)
#         if file:
#             filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             #getPrediction(filename)
#             label = getPrediction(filename) #Prediction Function
#             flash(label)
#             full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             print(full_filename)
#             flash(full_filename)
#             l2=label
#             flash(l2)
#             # New custom code
#             return redirect('/')
#             # return render_template("index.html", prediction = label, img_path = full_filename)

# --------------------NEW
# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index2.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = UPLOAD_FOLDER + img.filename	
		img.save(img_path)

		p = getPrediction(img_path)
		if p == 0:
			result = "The ALL sybtype of blood smear sample is: 'Bening'"
		elif p == 1:
			result= "The ALL sybtype of blood smear sample is: 'Early Pre-B'"
		elif p ==2:
			result= "The ALL sybtype of blood smear sample is: 'Pre-B'"
		else: 
			result= "The ALL sybtype of blood smear sample is: 'Pro-B'"



	return render_template("index2.html", prediction = result, img_path = img_path)

if __name__ == "__main__":
    app.run()

