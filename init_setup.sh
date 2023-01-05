echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate environment"
source activate ./env
echo [$(date)]: "create folder and file structure"

for DIR in data_ingestion data_preparation data_validation model model_eval model_trainer

do  
    echo [$(date)]: "Creating", "src/NER_"$DIR
    mkdir -p "src/NER_"$DIR
    echo [$(date)]: "Creating __init__.py inside above folders"
    touch "src/NER_"$DIR/"__init__.py" "src/NER_"$DIR/$DIR".py"
    echo "from src.NER_"$DIR"."$DIR" import *" > "src/NER_"$DIR/"__init__.py"
done

echo [$(date)]: "install requirements"
pip install -r requirements.txt -q
echo [$(date)]: "installing pytorch dependency"
pip install torch --extra-index-url https://download.pytorch.org/whl/cu117 -q
echo [$(date)]: "END"

# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/