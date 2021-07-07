# LatinBERT

### Clone the Repo
git clone https://github.com/dbamman/latin-bert.git

### Create the VirtualEnv
python3 -m venv latinbert

### Activate the VirtualEnv
source /home/pietro/latinbert/bin/activate
# Install requirements
pip install -r requirements.txt


from cltk.data.fetch import FetchCorpus
corpus_downloader = FetchCorpus(language="lat")
corpus_downloader.list_corpora
corpus_downloader.import_corpus("lat_models_cltk")


in github folder
./scripts/download.sh


from cltk.sentence.lat import LatinPunktSentenceTokenizer
from cltk.tokenizers.word module import WordTokenizer

for using virtual env in jupyter 
pip install --user ipykernel
python -m ipykernel install --user --name=latinbert

then choose the kernel for jupyter
