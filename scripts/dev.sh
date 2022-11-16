source env/bin/activate
cp -r gpzu_parser web/backend
cd web/backend
python app.py
rm -r gpzu_parser