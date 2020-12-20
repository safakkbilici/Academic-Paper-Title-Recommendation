CURRENT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$CURRENT_PATH" 

conda create -n simpletransformers python pandas tqdm
conda activate simpletransformers
conda install pytorch cudatoolkit=10.1 -c pytorch

pip install simpletransformers
