#Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np
import os

filepath = 'D:/Plant-Leaf-Disease-Prediction-system/model_resnet152V22.h5'
model = tf.keras.models.load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image =tf.keras.utils.load_img(tomato_plant, target_size = (224, 224)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = tf.keras.preprocessing.image.img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==5:
      return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
       
  elif pred==6:
      return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'
        
  elif pred==7:
      return "Tomato - Late Blight Disease", 'Tomato - Late_blight.html'
        
  elif pred==8:
      return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
       
  elif pred==9:
      return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
        
  elif pred==10:
      return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'
        
  elif pred==11:
      return "Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'
        
  elif pred==12:
      return "Tomato - Tomoato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
  elif pred==13:
      return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
        
  elif pred==14:
      return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'
  else:
      return "Tomato - Healthy and Fresh", 'notTL.html'
  

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index1.html')
    
@app.route('/team',methods=['GET', 'POST'])
def team():
    return render_template('Contact.html')



@app.route('/lateblight',methods=['GET', 'POST'])
def lateblight():
    return render_template('Tomato - Late_blight - nepali.html')

@app.route('/leafmold',methods=['GET', 'POST'])
def leafmold():
    return render_template('Tomato - Leaf_Mold - nepali.html')

@app.route('/septoria',methods=['GET', 'POST'])
def septoria():
    return render_template('Tomato - Septoria_leaf_spot - nepali.html')

@app.route('/targetspot',methods=['GET', 'POST'])
def targetspot():
    return render_template('Tomato - Target_Spot - nepali.html')

@app.route('/mosaic',methods=['GET', 'POST'])
def mosaic():
    return render_template('Tomato - Tomato_mosaic_virus - nepali.html')

@app.route('/yellowleaf',methods=['GET', 'POST'])
def yellowleaf():
    return render_template('Tomato - Tomato_Yellow_Leaf_Curl_Virus - nepali.html')

@app.route('/spidermite',methods=['GET', 'POST'])
def spidermite():
    return render_template('Tomato - Two-spotted_spider_mite - nepali.html')

@app.route('/bacteriaspot',methods=['GET', 'POST'])
def bacteriaspot():
    return render_template('Tomato-Bacteria Spot - nepali.html')

@app.route('/earlyblight',methods=['GET', 'POST'])
def earlyblight():
    return render_template('Tomato-Early_Blight - nepali.html')

@app.route('/healthy',methods=['GET', 'POST'])
def healthy():
    return render_template('Tomato-Healthy - nepali.html')

@app.route('/notTL',methods=['GET', 'POST'])
def notTL():
    return render_template('notTL - nepali.html')

@app.route('/index',methods=['GET', 'POST'])
def index():
    return render_template('index1 - Nepali.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('D:/Plant-Leaf-Disease-Prediction-system/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path, filename= filename)
    

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='upload/' + filename), code=301)

# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False, port=8080) 
    
    
