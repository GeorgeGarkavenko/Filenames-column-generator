from glob import glob
from sys import argv

def main(prefix_length=7):
    """
    Images reporter script
    Print out file names of *.jpg files in the current folder.
    File: xxxxxxx*.jpg, ( x is a digit)
    One row with one position.
    """
    with open('filenames_rows.txt', 'w') as f:
        prefix = ""
        for n in glob('*.jpg'):
            
            if prefix != n[:prefix_length]:
                f.write('\n')
            else:
                f.write(',')
            f.write("".join(n.split())[:-4])
            prefix = n[:prefix_length]
    
if __name__ == "__main__":
    main(*argv[1:])