import re
from shutil import copyfile
from os import listdir
from os.path import isfile, join


def detected_image_in_md(line): 
    image_md_regex = r"\!\[.*\]\(.+\)"
    if re.match(image_md_regex, line) is not None:
        return "md"
    if "img" in line:
        return "html"
    return None

def find_image_path(line, type):
    if type == 'html':    
        tokens = line.split("\"")
        for token in tokens:
            if (".png" in token):
                return token
        return None 
    elif type == 'md':
        tokens = line.split("(")
        for token in tokens:
            if (".png" in token):
                return token.split(")")[0]
        return None
    return None    

def import_image(path, filename, id):
    if "http" in path:
        return 
    dst = "./_media/" + filename.replace(" ", "_")[:-3] + "__" + str(id) + ".png" 
    copyfile(path, dst)
    return dst

def main(): 

    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    files_to_avoid = ["LICENSE", "README.md", "test.md", "main.py"]

    for chapter in onlyfiles:

        if (chapter in files_to_avoid):
            continue
        
        if ("_" + chapter in onlyfiles):
            print("delete previous generated files")
            break

        file = open(chapter, "r+")
        new_file = open("_" + chapter, "w+")

        count = 0
        for x in file:
            
            ## controlla se la riga contiene una immagine 
            type = detected_image_in_md(x)

            if (type is not None):
                count += 1
                path = find_image_path(x, type)

                try:
                    dst_path = import_image(path, chapter, count)
                    if dst_path is not None:
                        x = x.replace(path, dst_path)
                except:
                    print("error while importing image. FILE: ", chapter)
                print(dst_path)

            new_file.write(x)

        print("imported images: ", count)
	print("\n")
        file.close()
        new_file.close()

if __name__ == "__main__":
    main()
