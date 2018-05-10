Final Exam: May 10, 2018
====

### Reference this project to answer questions on final exam.

# Start here then return to exam in D2L to begin answering questions
1. __clone__ this repository (https://github.com/rmedinahu/cs350-props-final-exam) to your machine.
2. create a virtual environment for this project
3. Run: `pip install -r requirements.txt` (will install django and geopy)
4. Setup the django app: `python manage.py migrate`
5. Load the database with sample data containing a set of real estate properties, transactions, and messages: 

`python manage.py loaddata property-testdata`

`python manage.py loaddata transaction-testdata`

`python manage.py loaddata message-testdata`

6. Run the test server: `python manage.py runserver` and make sure the page loads as expected.



