export FLASK_ENV=development
export FLASK_APP=run.py
echo "Flask environment variable(s) added"
source /home/koenvs/Documents/coding/flask/flaskenv/bin/activate
echo "Python: flask environment loaded"
BASE=$(pwd)
export SQLALCHEMY_DATABASE_URI="test.db"
echo "DB environment variable(s) added"