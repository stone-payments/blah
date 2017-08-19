# blah
Blah.


## Virtual environment

### Setting up the virtual environment

`python3 -m venv venv`

### Using the virtual environment

To activate on UNIX-based systems: `source venv/bin/activate`.
To deactivate: `deactivate`.

## Requirements

`pip install -r requirements.txt`


## Authentication


Authentication is typically done through Application Default Credentials
which means you do not have to change the code to authenticate as long as
your environment has credentials. You have a few options for setting up
authentication:

### When running locally, use the Google Cloud SDK


        gcloud auth application-default login


### When running on App Engine or Compute Engine, 
credentials are already set-up. However, you may need to configure your Compute Engine instance with additional scopes

### You can create a Service Account key file. This file can be used to
   authenticate to Google Cloud Platform services from any environment. To use
   the file, set the ``GOOGLE_APPLICATION_CREDENTIALS`` environment variable to
   the path to the key file, for example:


        export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json


## Running the project

`python src/run.py`
