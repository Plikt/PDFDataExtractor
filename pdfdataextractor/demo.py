from extraction import Reader
import json
import glob


def read_single(file):
    reader = Reader()
    pdf = reader.read_file(file)
    try:
        #print(pdf.plaintext())
        print(pdf.test())
        #print(pdf.keywords())
        
        metadata = {
            'journal': pdf.journal(), 
            'title': pdf.title(),
            'doi': pdf.doi(),
            'abstract': pdf.abstract(chem=False),
            'caption': pdf.caption(),
            'reference': pdf.reference()
            }
        """'author': pdf.author(),
        'keywords': pdf.keywords(),"""
        print(metadata)
        with open("metadata.json", "w") as write_file:
            json.dump(metadata, write_file, indent=4) 

        # print(pdf.section())
        # for i,j in pdf.reference().items():
        #     print(i)
        #     print(j)


    except:
        pass
    
    return metadata

def read_multiple(path):
    for seq, pdf in enumerate(path):
        read_single(pdf)
        print('-------------------', '\n')

# read_multiple(glob.glob(r'/Users/miao/Desktop/PDFDataExtractor/SI/Others/acs/*.pdf'))
read_single(r'/Users/desot1/Downloads/propermotions.pdf')
# read_single(r'/Volumes/Backup/PDE_papers/articles/Elesvier/dssc/The-effect-of-molecular-structure-on-the-properties-of-quinox_2020_Dyes-and-.pdf')
