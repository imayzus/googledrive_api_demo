# googledrive_api_demo

This project demonstrates basic usage of Google Drive API using python.

Before running the code, the project requires creating a credentials file, credentials.json. 
This can be achieved by following the instructions in https://developers.google.com/drive/api/quickstart/python

The scripts in run_unit_tests.sh and run_integration_tests.sh demonstrate running unit and integration tests.
This project also uses FastAPI implementation to expose the functionality as REST endpoints
/files/list
/files/upload
/files/download
/files/delete

The application can be started using run_app.sh script.
Alternatively, it can be run from commandline as
export PYTHONPATH=.:gd_demo
uvicorn main:app --reload --host 0.0.0.0 --port 9000 --log-level debug
The script uses port 9000 as default to run the application. 
After starting the app, the endpoints can be accessed at 
http://localhost:9000/docs#


