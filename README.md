# A minimal Flask application with Bootstrap Sass

## Install

First, clone this repository. Then run the following commands:

``` bash
# Setup virtual environment
virtualenv venv -p python3;
source venv/bin/activate;

# Install python dependencies
pip install -r requirements.txt;

# Install npm modules
cd application/static/assets;
npm install;
cd -;

# Run the application
export FLASK_APP="application.app";
export FLASK_DEBUG="True"
flask run;  # localhost:5000
```
