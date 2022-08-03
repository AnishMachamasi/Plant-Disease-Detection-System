<div align="center">

## Tomato Leaf Disease Detection System Using CNN
 
 Paper: "https://drive.google.com/file/d/1NI8EzbmoG11RTdeX_3bkLFGLvSiXtruC/view?usp=sharing" \
 pptx : "https://docs.google.com/presentation/d/1QXeXSAYMIoBL_p7uB9oz4vsLHysP1r51/edit?usp=sharing&ouid=113979974867999383936&rtpof=true&sd=true"

<!-- ### <a href="https://plant49-ai.herokuapp.com/" target="_blank">https://plant49-ai.herokuapp.com/</a> -->

<!-- ## <img src="./Assets/web.gif" alt="demo"/> -->

 </div>
<div align="justify">
 
## Project Outcome
![1](https://user-images.githubusercontent.com/98002255/180613185-733083fe-8aed-41b9-8fc6-65d27b8ff2a2.JPG)
![2](https://user-images.githubusercontent.com/98002255/180613203-88dd158a-9d4a-4894-9d4c-cd8bfee34797.JPG)
![3](https://user-images.githubusercontent.com/98002255/180613242-7e0e3c57-6b24-4906-ab6c-5221a0c469d9.JPG)


## Description

Timely detection of diseases of the crop is necessary for the food security of billions of people around the globe. It serves the dual purpose of increasing crop yield and reducing pesticide use without knowing about the disease that are caused to the plant. In the present time, Plant disease detection is important goal for achieving food security. The traditional method of disease detection has been to use manual examination by either farmers or experts, which can be time consuming and costly, proving infeasible for millions of small and medium sized farms around the world.

This project is an approach to the development of Tomato plant disease detection model using CNN. Using the model, it can predict 10 different disease of tomato plant.

<br>
<hr>

Major procedure for creating model and use it for detection of plant disease are:

1. Data gathering

   The dataset taken was **"Tomato Dataset"**. It can be downloaded through the link "https://www.kaggle.com/anishmachamasi/new-tomato-dataset". It is an Image dataset containing images of different disease of tomato plant.

2. Model building

   - I have used CNN (transfer learning) for building the model.
   - I have three models by:-
     1. Transfer learning model
     2. Using Transfer learning VGG16 Architecture.
     3. Resnet architecture\
     Model link: "https://drive.google.com/drive/folders/1AC-ti4An3sed2WDGEU7qZUD8SPNV8jEe?usp=sharing" \
 Save those model inside main

3. Training

   The model was trained by using variants of above layers mentioned in model building and by varying hyperparameters. The best model was able to achieve 98.42% of test accuracy.

4. Testing

   The model was tested on total 18,160 images of 10 classes.<br/>
   The model used for prediction on sample images.

5. Various Model Architecture tried along with Learning Rate and Optimizer and various accuracy obtained with different models.

## Details about the model

### The model will be able to detect 10 different of `diseases` of `tomato plants`.

<BR>

## HOW TO RUN THE FILE?

To run the `leaf.py`, initially install all the packages of `requirements.txt`. It is suggested to use `virtual environment` while installing all packages from requirements.txt. To install, use following command:
<br>
`pip install requirements.txt`
 
Note: Library may get updated with time. So make changes accordingly.

<br>

I have used python version of 3.10 . So use accordingly.

<br>

After that, use following command to run:

`python leaf.py`

<br>

For further info, you can use `stackoverflow` as well.
Note: Replace following in leaf.py if internal server error occurs:\
 if __name__ == "__main__":\
    app.run(debug=True)\
    app.run(threaded=False, port=8080) 
</div>
