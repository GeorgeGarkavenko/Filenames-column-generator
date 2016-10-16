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
        prefix = "".split()
        
        str_buffer = ""
        
        for n in glob('*.jpg'):
            
            if prefix != n[:prefix_length]:
                # f.write('\n')
                f.write((str_buffer + '\n')*8)
                str_buffer = ""
            else:
                # f.write(',')
                str_buffer += ','
                
            # f.write("".join(n.split()))
            str_buffer += "".join(n.split())
            prefix = n[:prefix_length]
            
        f.write((str_buffer + '\n')*8)

        
if __name__ == "__main__":
    main(*argv[1:])