from unstructured.partition.docx import partition_docx
from multiprocessing import Process
import ast, glob, os


CWD = 'pyqt_project/utils'

def parseDocx(file):
    elements = partition_docx(filename=f'{file}', extra_whitespace=True)
    with open(f'{CWD}/output.py', 'a') as f:
        for i in range(len(elements)):
            f.write(f'{str(elements[i].to_dict())}\n')


def writeToFile():
    buffer = ""
    f = open(f'{CWD}/output.py', 'r')
    with open(f'{CWD}/output.txt', 'a') as out:
        for i in f: 
            element = ast.literal_eval(i)   
            cat = element['type']

            match cat:
                case 'Table':
                    out.write(f'{buffer}\n')
                    tableContent = element.get('metadata')['text_as_html']
                    tableContent = tableContent.replace(tableContent[tableContent.find('\n')], '')
                    out.write(f'\n{tableContent}\n\n')
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