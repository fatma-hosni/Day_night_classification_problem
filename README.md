# Day_night_classification_problem
A Deep learning model for day night classification problem

#   Dataset
    Obtained from BDD A Large-scale Diverse Driving Video Database   
    dataset link:https://www.kaggle.com/solesensei/solesensei_bdd100k
    After dowunload dataset there is 2 step:
    1- go to : archive\bdd100k\bdd100k\images\100k\train
       in train file : testA,testB,trainA,trainB where testA ,trainA is images for day class, and trainB,testB is image for night class
    2- make 2 folder thier name is day,night and copy images from trainA, testA to day folder and copy images from trainB,testB to night folder
       and put those to folder in folder name "dataset" in app path
    now the dataset is ready to use in day_night_classification.ipynb !
# day_night_classification.ipynb
    inculde model starting from data prepration and visualization to model testing and validation  
# app.py 
    include model integration with flask API 
# uploads 
    contain images for testing api form test set to test your own images add them to this folder
#   saved_model:
    include trained model that app will use to test images in upload file
    must be unzip to one file (splited to 4 files as max file upload is 25 MB)
    path should be : saved_model//my_model
      
#   requirements.txt
   ## Problem for pip or python installation
          install python modules that used in full problem using command line tool called pip 
          pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by               virtualenv  or venv. Just make sure to upgrade pip.
          Step 1: Check if PIP is Already Installed
            Type in the following command at the command prompt:
            pip help
            Step 2: Verify Python Installation
            To determine whether you have Python installed:
            -  Open the Command Prompt window.
            -  When the console window opens, type in:
               python

         For Download PIP 
            - Before installing PIP, download the get-pip.py file:https://bootstrap.pypa.io/get-pip.py
              Download the file to the desired folder in Windows. You can save the file to any location, but remember the path so you can use it later.
            - check version again
   ##  cd to requirements.txt path and run this command line:
      pip install -r requirements.txt
      
      if error erase this because you alreaday have the module so remove module name that make error from requirements.txt 
 
   #  run app.py (server on local host)
   
      
