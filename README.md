# Survey Questionnaire

This is a multi page survey project, wherein 8 questions are field based & come one after the other, last 2 are file uploads. All the responses are stored in a Database table & for file uploads only location is stored in DB. Actual files are stored in some other directory/cloud (possible).

There is also API functionality to GET all/single survey record (by ID) & POST the same 

### Different views available 
 1. New Survey (homepage)
 2. Survey List
 3. Detailed Survey View
 4. Get Survey by ID
 5. Edit a survey record for any/all fields


### Dependencies include

`Django` 

`djangorestframework`

`Pillow`

Setting up environment (requires pipenv)
----------

    pipenv install django
    python3 -m pip install djangorestframework
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

## Running server locally
    
    python3 manage.py runserver <port>

_please provide port number to run the application, if left blank. It would default go to port 8000_

This will trigger the application to viewed in browser.
    
http://localhost:8000/

The landing page will have new survey to bew filled in 

## Screenshots of the Views

![Landing Page](/snapshots/Landing_Page.jpg)

![Screens](/snapshots/Screens.png)

![Image Uploads](/snapshots/Image_File_Upload.png)

![File Uploads](/snapshots/File_Upload_submit.png)


### View All Survey List

![All Survey](/snapshots/All_Survey_List.png)

### Survey by ID

![Survey by ID](/snapshots/Survey_By_Id.png)

### Survey Detail Record View

![Survey by ID](/snapshots/Survey_Detail.png)

### Edit Survey

![Edit Survey](/snapshots/Edit_Survey.png)

## API Points to GET & POST data

### getting all records

GET http://localhost:8000/api-view/

### getting one record via key

GET http://localhost:8000/api-view/?key=5


