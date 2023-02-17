import os
import re
import socket
from collections import Counter
count=0
data_dir = "../home/data"
files=os.listdir(data_dir)

output_dir='../home/output'
output_file='result.txt'
output_file_dir=output_dir+"/"+output_file


if not os.path.exists(output_dir):
    os.makedirs(output_dir)
def read_file(fname):
    with open(fname) as file:
        content=file.read()
        return content
def word_count(content:str)->int:
    return len(content.split())
def get_top_3_words(content):
    word_counts=Counter(content)
    top_3_words=word_counts.most_common(3)
    return top_3_words
#for IF priting the top 3 common words
def get_top_k_words_for_file(filename):
    fp=f'{data_dir}/{filename}'
    f_content=read_file(fp)
    return get_top_3_words(f_content.split())
def get_ip():
    return socket.gethostbyname(socket.gethostname())
with open(output_file_dir,'w') as file:
    file.write("Files present in the /home/data are:\n")
    for fname in files:
        file.write("\t"+fname+"\n")
    for fname in files:
        if fname.endswith('.txt'):
            filepath=f'{data_dir}/{fname}'
            content=read_file(filepath)
            length=word_count(content)
            count=count+length
            file.write(f'Number of words in  {fname} are {length}\n')
    file.write(f'total word count in both files are {count}\n')
    top_3_words=get_top_k_words_for_file("IF.txt")
    file.write('top 3 words in IF.txt are\n')
    for word,count in top_3_words:
        file.write(f'\t{word}: {count}\n')
    file.write(f'IP Address: {get_ip()}\n')
result=read_file(output_file_dir)
print(result)
