# -*- coding: utf-8 -*-
'''
Authors: Shravan Chintha and Adithya Job
Date: 03/23/2018
Assignment 3: POS Tagger, file: scorer.py

This program will compare the "pos-test-with-tags.txt" (output of tagger.py) with golden 
standard key "pos-test-key.txt" file and calculates the accuracy and provide the
confusion matrix for the same. 

The program should be run from command prompt/ terminal, once the path of the python file is specified
the below line should be typed:
    
python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-taggingreport.txt

once the above command is run, a text file pos-taggingreport.txt is created in the
directory location. This file will contain accuracy and confusion matrix computed for
the above tag comparisons.

Algorithm:

Step 1 : Accept the sys arguments which are the tagger program output file and test key 

Step 2: Read the output file and clean the unwanted characters from the file 

Step 3: Read the POS tagged Key file and put them in a list after tokenizing, remove unwanted characters. 

Step 4: Match corresponding words from the model output to the test key and increment a counter each time when there is a match

Step 5: Find the accuracy of the model by dividing the count of matched words with the len of the model out file.

Step 6: Create a confusion matrix by comparing the tagged  key  POS list file tokens  with the model output tagged POS tokens 

Step 7: END

'''

import scipy
import sys
import nltk
import pandas as pd
from sklearn.metrics import confusion_matrix
if __name__ == "__main__":
    
    #train_file = sys.argv[1]
    #test_file = sys.argv[2]
    #test_output_file = sys.argv[3]
    
    output_file = sys.argv[1]
    test_key = sys.argv[2]
    tagger_report= sys.argv[3]
    
    #output_file = "pos-test-with-tags.txt"
    #test_key = "pos-test-key.txt" 

    with open(output_file) as f:
        model_output = f.read().replace('\n', '')
        model_output_tokens = [nltk.tag.str2tuple(t) for t in model_output.split() if t.strip() 
        not in ['[',']','#','$',"''",'(',')',',','.',':','``']]
    
    with open(test_key) as f:
        input_key = f.read().replace('\n', '')
    
        temp = input_key.replace("[","")
        final_key=temp.replace("]","") 
        final_key_tokens = [nltk.tag.str2tuple(t) for t in final_key.split()if t.strip()
        not in ['[',']','#','$',"''",'(',')',',','.',':','``']]
    #for value in model_output_tokens:
    
    tag_key_list= [x[1] for x in final_key_tokens]
    model_tag_list = [x[1] for x in model_output_tokens]
    count=0
    
    for word in tag_key_list:
        pos=tag_key_list.index(word)
        if ( word== model_tag_list[pos]):
            count= count+1
    
    accuracy = count/ len(final_key_tokens) #gives the accuracy by comparing with key.
    
    pos_key = set(tag_key_list)
    list(pos_key)
    model_key = set(model_tag_list)
    list(model_key)
    #creates confusion matrix
    df1 = pd.Series( (v for v in tag_key_list) )
    df2 = pd.Series( (v for v in model_tag_list) )
    
    df_confusion = pd.crosstab(df1, df2) 
    
    print("Please open the file pos-taggingreport.txt created in the directory for accuracy and confusion matrix")
    
    with open(tagger_report,'w') as f:
        f.writelines("Accuracy is: ")
        f.writelines(str(accuracy))
        f.writelines('\n')
        f.writelines('\n')
        f.writelines("Confusion Matrix: ")
        f.writelines('\n')
        f.writelines('\n')
        f.writelines(str(df_confusion))
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
