# LatinBERT

### Clone the Repo
git clone https://github.com/dbamman/latin-bert.git

### Create the VirtualEnv
python3 -m venv latinbert

### Activate the VirtualEnv
source /home/pietro/latinbert/bin/activate
# Install requirements
pip install -r requirements.txt


### Execute in shell for download the Bert Model
./scripts/download.sh


for using virtual env in jupyter 
pip install --user ipykernel
python -m ipykernel install --user --name=latinbert

then choose the kernel for jupyter
