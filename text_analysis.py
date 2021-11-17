import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--val")
args = parser.parse_args()
val = args.val


def text_analysis(input_text):
    clean_words=input_text.replace(";"," ")
    all_words=clean_words.split()
    lower_text=clean_words.lower()
    size_text=len(clean_words)
    word_count=len(clean_words)
    return(lower_text, size_text, all_words, word_count)

results=text_analysis(val)
print(results)




        
