# Django web app for my senior capstone project! Currently being served at www.fplpredictions.com

## To run this application locally, follow these steps:

`$ git clone https://github.com/PrestonMcIllece/FPL-Predictions`

[Make sure you have Python 3.7 installed.](https://www.python.org/downloads/)

Install the Python fpl package.

`$ pip3 install fpl`

If this fails, try `$ pip install fpl` instead.

Next, install Django.

`$ python3 -m pip install Django` Again, if this fails try `$ python -m pip install Django` instead.

Finally, `cd` into /FPL-Predictions and run:

`$ python3 manage.py runserver PORTNUMBER` where PORTNUMBER is the port you want to run it on.
  
You can now visit localhost:PORTNUMBER in the browser and see the application!
