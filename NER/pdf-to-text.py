import requests
import ast
import glob

def convert_pdf_to_text_pdfbox_api(filename):
    url = "https://chat.findmind.in:8445/pdf-to-text"
    file = {'file': open(filename,'rb')}
    response = requests.post(url, files=file)
    data = response.text
    data = ast.literal_eval(response.text)["data"]
    return data

if __name__=='__main__':
    f=1
    for i in glob.glob('pdfs/*.pdf'):
        text = convert_pdf_to_text_pdfbox_api(i)
        file = open(i+'.txt', 'w')
        file.write(text)
        file.close()
        print(f)
        f+=1
