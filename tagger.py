
'''
Authors: Shravan Chintha and Adithya Job
Date: 03/23/2018
Assignment 3: POS Tagger, file: tagger.py
1. Introduction:
This is a program that will tag parts of speech in a given text input file. The program will take
an input file pos-train.txt (which has words and tags to train a model) and pos-test.txt file (which contains
words that are to be tagged) and generates an output text file containing tags besides the words that
are present in the test file. The output file generated will have the tags that have maximum probability to 
be the tagged to the words that are present in training data. And if there are words in test data that are 
not present in train data, they will be tagged as nouns. 

There are 8 types of parts of speech, namely, Noun, Pronoun, Verb, Adverb, Adjective,
Preposition, Conjunction and Interjection. Based on the word that is present and its context based on 
the training file input, tags are added next to the words in the output file. The tags are usually of the form:
NN	Noun, singular or mass
NNS	Noun, plural
NNP	Proper noun, singular
NNPS	Proper noun, plural
PDT	Predeterminer
POS	Possessive ending
PRP	Personal pronoun
PRP$	Possessive pronoun
RB	Adverb
RBR	Adverb, comparative etc.,

So output file will have words with tags in the format of :
No/RB ,/, 
[ it/PRP ]
[ was/VBD etc.,

2. Example input/output:

The program should be run from command prompt/ terminal, once the path of the python file is specified
the below line should be typed:

python tagger.py pos-train.txt pos-test.txt pos-test-with-tags.txt
(make sure that the folder which contains the python file should also contain the train, test and key files)

this will run the file tagger.py with input files pos-train.txt and pos-test.txt and will generate an output file
pos-text-with-tags.txt in the same folder where the tagger.py file is located.

once it is run, check the folder and look for the file pos-text-with-tags.txt and open it. It will contain
tags besides the words that are present in test data based on the train data.

3. Algorithm:

Start
    
Step 1 : Accept the sys arguments which are the train , test and output file name 

Step 2: Read the train file and clean the unwanted characters from the file 

Step 3: Read the POS tagged training dataset words and put them in a list after tokenizing

Step 4: Find the conditional distribution of the word and POS tag combination from the training dataset

Step 5: In the tagged word list create a new tag called NN for the class unidentified.

Step 6: Read the test file and clean the unwanted characters from the file

Step 7: Tokenize the test file words in the test file

Step 8: Match the  tagged words/tokens from the train with the tokens in the test.

Step 9: If the token in the train has been associated with more than one POS tag then  pick the POS tag with the highest occurrence
        If no match found then use NN.

Step 10:If there is match then write that matched POS tag and the word into the output file. 

Step 11: Write the Output file into the working directory. 

End

'''
import sys
import nltk
if __name__ == "__main__":
    
    #train_file = "pos-train.txt"
    #test_file = "pos-test.txt"
    #test_output_file = "pos-test-with-tags.txt"
    train_file = sys.argv[1]
    test_file = sys.argv[2]     # accepting the arguments
    test_output_file = sys.argv[3]
    
    tagged_tokens = None 
    input_train = None
    
    with open(train_file) as f:
        input_train = f.read().replace('\n', '')
    
    temp = input_train.replace("[","")
    final_train=temp.replace("]","") 
    
    
    if final_train is not None:    
        train_tagged_tokens = [nltk.tag.str2tuple(t) for t in final_train.split()] # tokenizing the train file 
        tagged_tokens = nltk.ConditionalFreqDist(train_tagged_tokens) # finding the frequency distribution
    
    test_tokens = None  
    input_test = None
    
    
    with open(test_file) as f:
        input_test = f.read().replace('\n', '')
        
    temp_1 = input_test.replace("[","")  # remove [ ,]
    final_test=temp_1.replace("]","")     # remove [ , ] 
        
    if final_test is not None and tagged_tokens is not None:
        final_test = " "+final_test+" "  #  add temp spaces starting and ending to replace first and last words   
        test_tokens = [t for t in final_test.split()] 
        for test_token in test_tokens:
            matched_pos_final = 'NN'  # if word in  not existed in training (Unknown word) use NN
            matched_pos = tagged_tokens[test_token].most_common()
            if matched_pos:
                matched_pos_final = matched_pos[0][0]
            
            test_tagged_token = test_token+"/"+matched_pos_final
            final_test = final_test.replace(" "+test_token+" "," "+test_tagged_token+" ")
            final_test = final_test.replace("\n"+test_token+" ","\n"+test_tagged_token+" ")
            final_test = final_test.replace(""+test_token+"\n",""+test_tagged_token+"\n")
            
    final_test = final_test[1:-1]  # remove previously added temp spaces 
    with open(test_output_file,'w') as f: #write output to the text file parsed initially.
        f.write(final_test)
print("Please open the file pos-test-with-tags.txt created in the directory for tags beside the words/tokens")
  