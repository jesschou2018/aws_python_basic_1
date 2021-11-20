import argparse
# import regex module
import re

parser = argparse.ArgumentParser()
parser.add_argument("--val")
args = parser.parse_args()
val = args.val

def text_analysis(input_text):
# clean input and convert to list for # and @ extraction 
    #punctiontoreplace=[',','.','/',';','|','}','{','[',']','!','$','%','^','&','*','(',')']
    clean_text = input_text.replace(';'," ") 
    lower_text=clean_text.lower()
    all_words=lower_text.split()
# word count and text size
    size_text=len(lower_text)
    word_count=len(all_words)

# hashtag and @locations
    tag_locations=list(map(lambda x:x.find("#"),all_words))
    tag_list_loc = [i for i, e in enumerate(tag_locations) if e == 0]
    tag_values=[all_words[i] for i in tag_list_loc]
    at_locations=list(map(lambda x:x.find("@"),all_words))
    at_list_loc = [i for i, e in enumerate(at_locations) if e == 0]
    at_values=[all_words[i] for i in at_list_loc]
    return(all_words, size_text, word_count,tag_values, at_values)

results=text_analysis(val)
print(results)




        
