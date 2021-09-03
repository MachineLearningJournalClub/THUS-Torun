# Abstract of Our Paper 
In the Middle Ages texts were learned by heart and spread using oral means of communication from generation to generation. Adaptation of the art of prose and poems allowed keeping particular descriptions and compositions characteristic for many literary genres. Taking into account such a specific construction of literature composed in Latin, we can search for and indicate the probability patterns of familiar sources of specific narrative texts. Consideration of Natural Language Processing tools allowed us the transformation of textual objects into numerical ones and then application of machine learning algorithms to extract information from the dataset. We carried out the task consisting of the practical use of those concepts and observation to create a tool for analyzing narrative texts basing on open-source databases. The tool focused on creating specific search tools resources which could enable us detailed searching throughout the text. The main objectives of the study take into account finding similarities between sentences and between documents. Next, we applied machine learning algorithms on chosen texts to calculate specific features of them (for instance authorship or centuries) and to recognize sources of anonymous texts with a certain percentage.

# Folders

- library_super_reduced database of txt files from Latin Text Library

- corpus2 contain similar text to Gallus, specific authors belonging to the same centuries of Gallus.

- pickle_gallus_related contain the processed vectors from the text 
of corpus2. How to use the pickle files is in 'analysis_from_pickles' notebook

- analysis contain different notebooks of analysis made for the paper.

- utils contains different python scripts 


# Files
- script_generator.py is a python script for generate the bash script that compute the bert representation of the given texts and it saves the representation in a convenient way that is pickle files.
in this file you have to set the source folder, the output folder and the folder in which the Bert Model is contained.

- latbert.py is another python file used for the preprocessing of the texts.

- script_generator_colab is the same python script but adapted for colab usage
- text_to_pickle.py is the python script that is called by the bash script.sh.
you dont have to set anything in this file.

- script.sh the bash script. it's automatically generated from the script_generator.py

# Pipeline

1. Edit the script_generator.py with the source folder, the output folder and the folder in which the Bert Model is contained.
Example:

        import os

        path='library_super_reduced' 
        bertpath='/latin_bert' 
        output='pickle'

  
2. Run the script_generator.py 

        python3 script_generator.py
    
    
3. Run the bash script.sh generated from the script_generator(after allowing to run it as executable)
        
        bash script.sh
        
4. You'll find the pickle databases in the output folder and from here you can start your analysis of the bert representations.

# How to manage the pickle files
The Bert representations are saved in a dictionary form and then stored in a pickle files for conveniency.
To use the pickle files you have to:
    
    import pickle
    data={}
    dbfile = open('picklefilename','rb')   
    data=pickle.load(dbfile)
    
    
# Notebooks 
In these notebooks there is the analysis of similarity and clustering and etc etc

1. Berts_model_colab.ipynb is the google Colab implementation of the python script_generator and the bash script. Moreover you can automatically download the pickle files.

2. analysis_from_pickles.ipynb is the first draft of analysis using cosine similarity


3. THUS_AUTHOR_RECOGNITION.ipynb

4. THUS-AUTHOR CLASSIFICATION.ipynb
  
  
  
  
  
  
  
  
  
  
