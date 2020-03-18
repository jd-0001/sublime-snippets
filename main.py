import os, fileinput, re

def find_and_replace_in_dir(find, replace):
    for index, file in enumerate(os.listdir(os.getcwd())):
        with fileinput.FileInput(file, inplace=True, backup='.bak') as f:
            for line in f:
                print(line.replace(find, replace), end='')


def remove_all_bak():
    os.system("rm *.bak")

def replace_insensitive(find, replace, source):
    return re.compile(re.escape(find), re.IGNORECASE).sub(replace, source)

def split_uppercase(source):
    return re.findall('[A-Z][^A-Z]*', source)

def remove_starts_with(start, source):
    return source.replace(source, source[len(start):])

for file in os.listdir():
    # file_name, ext = os.path.splitext(file)
    # new_name = '-'.join([i.lower() for i in split_uppercase(file_name)])
    # if new_name:
    #     if not 'field' in new_name:
    #         new_name += '-field'
    #     os.rename(file, f"{new_name}{ext}")
    # # print(file[5:])
    # # os.rename(file, file[5:])

    if file.startswith('ws-portal-vue-'):
        os.rename(file, remove_starts_with('ws-portal-vue-', file))
    # os.rename(file, remove_starts_with('ws-portal-vue-', file))
    
    # if file.startswith('-'):
    #     os.rename(file, file[1:])
    #     print(file[1:])

