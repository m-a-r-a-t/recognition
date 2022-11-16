source ./env/Scripts/activate
cp -r gpzu_parser web/backend
cd web/backend/
pyinstaller app.py --onefile
cd dist
mkdir public
cd ..
cd ../frontend
npm run build
cd build
cp -r ./ ../../backend/dist/public
cd ../../backend
rm -r gpzu_parser
