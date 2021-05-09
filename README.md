# Day_night_classification_problem
### A Deep learning model for day night classification problem:

    it contains 2 models:
    
        - Simple model which is depend only on brightness of image: 
            - Calculates average brightness for the whole image and takes a threshold to differentiate between day and night classes based on average brightness for the dataset.
            - Achvied 93.49% accuracy for test set
            
        - Deep network model:
            - Consists of 3 convolution neural networks  with maxpooling, elu activation function and one dense layer 
            - Validation accuracy: 99.937%, testing accuracy: 99.94%
            - It fits perfect so no need for transfer leraning as no need for complex network 
            
        - For more details please find day_night_classification.ipynb

# Dataset
    Obtained from BDD A Large-scale Diverse Driving Video Database   
    dataset link:https://www.kaggle.com/solesensei/solesensei_bdd100k
    After dowunloading the dataset there are 2 steps:
    1- Go to : archive\bdd100k\bdd100k\images\100k\train
       in train file : testA, testB, trainA, trainB where testA, trainA are images for day class, and trainB, testB are image for night class
    2- Make 2 folders. Thier names are day and night. Copy images from trainA, testA to day folder and copy images from trainB, testB to night folder
       and put those in a folder name "dataset" in app.py path
    now the dataset is ready to use in day_night_classification.ipynb !
# day_night_classification.ipynb
    It includes 2 models: simple model
    Deep network model: inculdes model starting from data prepration and visualization to model testing and validation  
# app.py 
    Tests the application that includes model integration with flask API 
# uploads 
    Contains images for testing api form test set to test your own images add them to this folder
# saved_model:
    The trained model which the app will use to test images in upload file
    must be unziped to one file (splited to 4 files as max file upload is 25 MB)
    The path should be : saved_model//my_model
      
# requirements.txt
   ## pip/python installation
          pip is used to facilitate the installation of the required libraries for running the application 
          pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by               virtualenv  or venv. Just make sure to upgrade pip.
          Check if PIP is Already Installed by typing "pip help" in the cmd
          Verify Python Installation by typing "python" in the cmd

         To install pip if not exist: 
            - Before installing PIP, download the get-pip.py file:https://bootstrap.pypa.io/get-pip.py
              Download the file to the desired folder in Windows. You can save the file to any location, but remember the path so you can use it later.
            - check version again
   ##  install the needed libraries by running the followig command after pip/python installation is done:
      pip install -r requirements.txt
      
      in case any of the libraries are already installed, remove them first from the list in requirements.txt, because this is going to cause errors while running the previous command
      you may directly check the list in requirements.txt and install them one by one manually in case the previous command is causing errors regarding the libraries existance/versions
 
 # steps to run/test the application
     1- unzip the saved_model to one part the path sould be saved_model/my_model 
     2- install required library 
     3- run app.py in command line (you should connect to server with local host)
     4- copy this local host to web page
     5- choose image from uploads folder (in case you need to test your own image put the image in uploads folder)
     6- click on predict image
     
 # steps to retrain model from scratch
    1- download dataset from ::https://www.kaggle.com/solesensei/solesensei_bdd100k
    2- go to : archive\bdd100k\bdd100k\images\100k\train
    3- make 2 folder day,night
    4- copy images from trainA, testA to day folder  
    5- copy images from trainB, testB to night folder
    6- put day folder,night folder in folder name called dataset
    7- dataset folder path is same with day_night_classification.ipynb path
    8- open day_night_classification.ipynb and start run cell by cell
      
