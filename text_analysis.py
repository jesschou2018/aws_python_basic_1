# Imports
import argparse
from sm_text import *

# Set up parser to take input variable as paremeter
parser = argparse.ArgumentParser()
parser.add_argument("--val")
args = parser.parse_args()
val = args.val

# run sm_text
text1 = sm_text(val)
print(sm_text.extract_at_tags(text1))
print(sm_text.extract_hashtags(text1))
