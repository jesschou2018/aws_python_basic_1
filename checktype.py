import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--val")

args = parser.parse_args()
val = args.val


def clean_text(i):
    lower_text=i.lower()
    size_text=len(i)
    return(lower_text, size_text)
    
print(clean_text(val))



        
