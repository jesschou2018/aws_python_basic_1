import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--val")

args = parser.parse_args()
val = args.val


def return_type(i):
    a=type(i)
    return(a)
    
print(return_type(val))



        
