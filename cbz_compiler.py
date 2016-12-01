import getopt
import os
import shutil
import sys
import zipfile

BASE_DIR = '_tmp'

def get_all_files(directory):
    files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            files.append((root, filename))
    return files

def compile_zip(name, files):
    compilation_contents = {}

    for file in files:
        book = file.split('/')[-1].replace('.cbz', '')
        directory = '{}/{}'.format(BASE_DIR, book)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with zipfile.ZipFile(file, 'r') as bookfile:
            bookfile.extractall(path=directory)
            bookfile.close()
            compilation_contents[book] = get_all_files(directory)

    with zipfile.ZipFile('{}.cbz'.format(name), 'w') as compilation:
        for book in sorted(compilation_contents):
            page_list = compilation_contents[book]
            for page in page_list:
                filename = os.path.join(page[0], page[1])
                arcname = '--'.join([book, page[1]])
                compilation.write(filename, arcname=arcname)
        compilation.close()

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:", ["name="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if len(args) == 0:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-n', '--name'):
            if not os.path.exists(BASE_DIR):
                os.makedirs(BASE_DIR)
            compile_zip(arg, args)
            shutil.rmtree(BASE_DIR)
