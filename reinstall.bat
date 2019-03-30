cat files.txt | xargs rm -rf 
python setup.py build
python setup.py install --record files.txt