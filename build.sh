# build the project

echo "buidling the project...."
python3.9 -m pip install -r requirements.txt


echo "make migrations...."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static...."
python3.9  manage.py collectstatic --noinput --clear
