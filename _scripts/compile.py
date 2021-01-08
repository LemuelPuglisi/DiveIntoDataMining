from os import listdir
from os.path import isfile, join

chapters = [
    "0_Preface.md",
    "1_Market_Basket_Analysis.md",
    "2_Clustering.md", 
    "3_Classificazione.md", 
    "4_Predizione.md", 
    "5_Reti_e_modelli_random.md", 
    "6_Graph_matching.md", 
    "7_Graph_Mining.md", 
    "8_Catene_di_Markov_HMM.md", 
    "9_Sistemi_di_raccomandazione.md", 
    "10_Reti_neurali.md", 
    "extra_1_Cenni_di_analisi_testuale.md", 
    "extra_2_Rappresentazione_di_immagini.md", 
    "extra_3_Word_embedding_e_Sentiment_Analysis.md"
]

def write_chapter_page (file, chapter):
    file.write('\n <div style="page-break-after: always;"></div> \n')
    file.write('<div style="margin-top:300px;">')
    file.write("<h1> Capitolo " + str(chapter) + "</h1>")
    file.write('</div>')
    file.write('\n <div style="page-break-after: always;"></div> \n')    

chapter_counter = 1
outfile = open('../000_dive_into_data_mining.md', 'w+')

for fname in chapters:
    
    with open("../" + fname) as infile:

        if fname != "0_Preface.md":
            write_chapter_page(outfile, chapter_counter)
            chapter_counter += 1

        for line in infile:
            outfile.write(line)

    outfile.write('<div style="page-break-after: always;"></div> \n')
    if fname == '0_Preface.md':
        outfile.write("[TOC] \n")
        outfile.write('<div style="page-break-after: always;"></div> \n')