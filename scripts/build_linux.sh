source env/bin/activate
cp -r gpzu_parser web/backend
cd web/backend/
pyinstaller app.py --onefile
mkdir dist/public
cd ../frontend
npm run build
cd build
cp -r ./ ../../backend/dist/public
cd ../../backend
rm -r gpzu_parser
