import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

class Preprocess:
    '''This class contains methods for text preprocessing.  '''
    tri = []
    def __init__(self,filename):
        ''' This constructor creates a list of triagrams which is used for comparion'''
        init_token = self.readFile(filename)
        clean_token = self.remove(init_token)
        trig_list = self.makeTrigram(clean_token)
        #store in text file
        self.tri = trig_list

    def remove(self,ini_token):
        ''' This function removes the stop words and punctuation from the given the tokens that are passed into it and also converts text to lowercase'''
        #lowerCase
        tokens = [t.lower() for t in ini_token]
        stop_words=set(stopwords.words('english'))
        punctuation=['"','(',')',',','?',';',':','.',"''",'``']
        filtered = [x for x in tokens if not x in stop_words and not x in punctuation]
        return filtered

    def makeTrigram(self,token):
        ''' This function is used to make triagrams of the tokens that are passed into it '''
        trigram=[]
        for i in range(len(token)-2):
            tt=(token[i],token[i+1],token[i+2])
            trigram.append(tt)
        return trigram

    def readFile(self,file):
        ''' This function reads text from file and removes the endlines and numbers and also tokenizes the text and returns tokens '''
        f = open(file,"r")
        o = f.read().replace("\n"," ")
        o = re.sub(r'[0-9]+', '', o)
        o = re.sub(r'[^\w\s]', '', o)
        return word_tokenize(o)
