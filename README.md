# Django web app for my senior capstone project! Currently being served at www.fplpredictions.com

## To run this application locally, follow these steps:

`$ git clone https://github.com/PrestonMcIllece/FPL-Predictions`

[Make sure you have Python 3.7 installed.](https://www.python.org/downloads/)

Create a new virtual environment.

`$ pip install virtualenv`

`$ virtualenv name_of_virtualenv`

Switch into your virtual environment.

`$ source name_of_virtualenv`

From here, you can install all dependencies from the `requirements.txt` file.

`$ pip install -r requirements.txt`

Finally, `cd` into /FPL-Predictions and run:

`$ python3 manage.py runserver PORTNUMBER` where PORTNUMBER is the port you want to run it on.
  
You can now visit localhost:PORTNUMBER in the browser and see the application!
