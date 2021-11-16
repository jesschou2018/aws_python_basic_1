import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--val")

args = parser.parse_args()
val = args.val


def clean_text(i):
    all_words=i.split()
    lower_text=i.lower()
    size_text=len(i)
    word_count=len(all_words)
    return(lower_text, size_text, all_words, word_count)
    
print(clean_text(val))



        
