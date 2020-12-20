CURRENT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$CURRENT_PATH" 

python3 -m venv venv/
source venv/bin/activate

python -m pip install --upgrade pip
python -m pip3 install --upgrade pip

pip --version

pip3 install keras==2.4.3
pip3 install tensorflow==2.4.0

