# Torun Humanities and Social Sciences Summer Program

The code repository for project “Machine learning and digital humanities – new approach to old questions” developed by the group of [Machine Learning Journal Club](https://www.mljc.it/) composed by Pietro Sillano, Beatrice Villata, Simone Poetto and Arianna Di Bernardo in cooperation with [Neurotechtor Scientific Students Club](https://neurotech.umk.pl/) consisting of Weronika Sójka and Zofia Piętka-Danilewicz during Torun Humanities and Social Sciences Summer Program 2021. The project is focused on developing a Natural Language Processing (NLP) pipeline to extract information from ancient Latin documents. 

# Abstract

In the Middle Ages texts were learned by heart and spreaded using oral means of communicationfrom generation to generation. According to a specific lexical resource new texts were formulated. Adaptation of the art of prose and poems allowed keeping particular descriptions and compositionscharacteristic for many literary genres. Taking into account a specific construction of literaturecomposed in Latin we are able to search for and indicate the probability patterns of familiar sourcesof specific narrative texts. The task carried out consists of the practical use of those concepts and observation to create a toolfor analyzing narrative texts using similies for whole phrases. Based on open source databases the probability of the origin of specific text sources was calcualted. According to that we are focused on creating a specific search tools resources wich will enable us detailed searching throughout the text. The main objectives of this study take into account finding similarities between sentences and documents. Next we try to perform machine learning algorithms on chosen texts to calculate specific features of them, for instance authors, centuries or appearing words. One extra objective is to apply machine learnig algorithms to recognize sources of anymous texts with a certain probability. Consideration of Natural Language Processing tools, allowed us transformation of textual objects into numerical ones and then application of machine learning algorithms to extract information from the dataset.

# Folders
- latin_library_text bigger database of txt files

- library reduced and super_reduced smaller version of database

- corpus0 and corpus2 contain similar text to Gallus, specific authors

- pickle_gallus_related contain the processed vectors from the text 
of corpus2. how to use the pickle files is in Gallus Notebook.

- pickle_latin_library_text contain the processed vectors from the text of library_reduced.

- 

# Files
- script_generator.py is a python script for generate the bash script that compute the bert representation of the given texts and it saves the representation in a convenient way that is pickle files.
in this file you have to set the source folder, the output folder and the folder in which the Bert Model is contained.

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
