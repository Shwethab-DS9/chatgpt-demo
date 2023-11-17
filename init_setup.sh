echo[$(date)]:  "START"
echo[$(date)]:"CREATING CONDA VIRTUAL ENV WITH PYTHON=3.11"
conda create --prefix ./venv python=3.11 -y
echo[$(date)]: "Activating virtula env"
source activate ./venv
echo[$(date)]:" Install Project requirements"
pip install -r requirements.txt
echo[$(date)]:"END"