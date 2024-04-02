from unstructured.partition.docx import partition_docx      #ignora
from multiprocessing import Process
import ast, glob, re


CWD = '/home/notebook-user/pyqt_project/utils'

def parseDocx(file):
    elements = partition_docx(filename=f'{file}', extra_whitespace=True)
    with open(f'{CWD}/output.py', 'a') as f:
        for i in range(len(elements)):
            f.write(f'{str(elements[i].to_dict())}\n')
    f.close()


def writeToFile():
    buffer = ""
    f = open(f'{CWD}/output.py', 'r')
    with open(f'{CWD}/output.txt', 'a') as out:
        for i in f: 
            element = ast.literal_eval(i)   
            cat = element['type']

            match cat:
                case 'Title':
                    out.write(f'{buffer}\n')
                    out.write(f'\n<h1>{element["text"]}</h1>\n')
                    buffer = ""

                case 'Table':
                    out.write(f'{buffer}\n')
                    tableContent = element.get('metadata')['text_as_html']
                    tableContent = re.sub(r'\s+', '', tableContent)
                    out.write(f'{tableContent}\n\n')
                    buffer = ""

                case _:
                    buffer = f'{buffer}{element["text"]}\n'

        out.write(f'{buffer}')
    out.close()
    f.close()


fileList = glob.glob(f'{CWD}/*.docx')

if len(fileList) == 1:
    parsing = Process(target=parseDocx(fileList[0]))
    parsing.start()
    parsing.join()

    writing = Process(target=writeToFile)
    writing.start()
    writing.join()
    print('done')