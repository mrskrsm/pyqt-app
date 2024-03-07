from unstructured.partition.pdf import partition_pdf    #ignora
from multiprocessing import Process
import ast, os, glob


CWD = 'pyqt_project/utils'

def parsePdf(file):
    elements = partition_pdf(filename=f'{file}', 
                            extract_images_in_pdf=True, 
                            infer_table_structure=True,
                            strategy='hi_res')
    
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
                    out.write(f'{buffer}')
                    out.write(f'<h1>{element["text"]}</h1>\n')
                    buffer = ""

                case 'Table':
                    out.write(f'{buffer}')
                    out.write(f'\n{element["metadata"]["text_as_html"]}\n\n')
                    buffer = ""

                case 'Image':
                    out.write(f'{buffer}')
                    out.write(f'\n{element["metadata"]["image_path"]}\n')
                    buffer = ""

                case _:
                    buffer = f'{buffer}{element["text"]}\n'
        
        out.write(f'{buffer}')

    out.close()
    f.close()


fileList = glob.glob(f'{CWD}/*.pdf')
print(fileList)
if len(fileList) == 1:
    '''parsing = Process(target=parsePdf(fileList[0]))
    parsing.start()
    parsing.join()
    os.system(f'mv /home/notebook-user/figures {CWD}')'''
    writing = Process(target=writeToFile)
    writing.start()
    writing.join()
    print('done')