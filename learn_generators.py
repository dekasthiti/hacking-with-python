import random
from timeit import timeit

# Comment from memory_profiler import profile out when
# running time based memory profiling with mprof
# See: Memory profiler documentation
from memory_profiler import profile
from glob import iglob
import os
import re

from pathlib import Path
import pprint
from collections import defaultdict


def random_iterator(limit):
    offset = 0
    while offset < limit:
        offset += random.random()
        yield offset
        
        
# # a is a generator object (i.e. an iterable)
# a = random_iterator(10)
#
# # You have to iterate over the iterable to get the values
# print([i for i in a])

def int_gen():
    # Infinite sequence of integers
    i = 1
    while True:
        yield i
        # This is how i is updated on next
        i += 1
        
def get(n, seq):
    """Returns first n values from the given sequence."""
    try:
        result = [next(seq) for _ in range(n)]
    except StopIteration:
        pass
    return result

@profile
def pythagorean_triplets():
    py_triplets = ((x, y, z) for z in int_gen() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
    return get(100, py_triplets)

def read_files(filenames):
    # generator
    for filename in filenames:
        try:
            with open(filename) as fp:
                if 'build' in filename or 'old' in filename:
                    continue
                line_num = 0
                for line in fp:
                    yield filename.replace('/Users/sthitid/software', '.') + ' L' + str(line_num) + ': ' + line
                    line_num += 1
        except IOError as err:
            print(f"Can't open {filename}. Reason: {err}")
                
def find_pattern(pattern, lines):
    # generator expression
    # lines = (line for line in lines if pattern in line)

    lines = (line for line in lines if re.search(pattern, line, re.IGNORECASE))
    return lines

def find_lines_of_len(length, lines):
    lines = [line for line in lines if len(line) > length]
    return lines

names_todos = defaultdict(list)
names_fixmes = defaultdict(list)
def printlines(lines):
    
    for line in lines:
        print(line,  end = "")
        names = line[line.find('(') + 1: line.find(')')].split(',')
        for name in names:
            if name in ['calvinq', 'zhuoc', 'tanl', 'jayw', 'boweny', 'chrisa', 'katiap', 'juny', 'qinghual',
                        'sthitid', 'venkats', 'vineeths', 'tejasn', 'jianz']:
                if re.search("TODO", line, re.IGNORECASE):
                    names_todos[name].append(line)
                if re.search("FIXME", line, re.IGNORECASE):
                    names_fixmes[name].append(line)
        
    for name, task_list in names_todos.items():
        print(f'{name} = {len(task_list)} | {task_list}')
        
    for name, task_list in names_fixmes.items():
        print(f'{name} = {len(task_list)} | {task_list}')
        
def printdict(line):
    names_tasks = defaultdict(list)
    
    name = line[line.find('(')+1: line.find(')')]
    names_tasks[name].append(line)
        
    print(names_tasks)

def find_pattern_in_files(pattern, filenames):
    lines = read_files(filenames)
    lines = find_pattern(pattern, lines)
    printlines(lines)
    
    
def find_lines_of_len_in_files(len, filenames):
    lines = read_files(filenames)
    lines = find_lines_of_len(len, lines)
    printlines(lines)
    
    
def gen_paths_of_files_in(dir):
    # files = (str(Path(file)) for root, dir, file in os.walk(dir))
    # pprint.pprint(next(file) for file in files))

    for dirName, subdirList, fileList in os.walk(dir):
        #print('Found directory: %s' % dirName)
        for fname in fileList:
            yield os.path.abspath('/'.join([dirName, fname]))
            # The print is executed when the generator object is iterated over in the calling function
            #print('\t%s' % fname)
            
            
def print_file_names(filenames):
    for fname in filenames:
        print('\t%s' % fname)
    
    # This yields a generator, why?
    # print('\t %s' % fname for fname in filenames)

@profile
def find_paths_of_files_in(dir):
    filenames = gen_paths_of_files_in(dir)
    [filename for filename in filenames]

def gen_python_files(filenames):
    for filename in filenames:
        # this, or, use filename.endswith('.py')
        name, ext = os.path.splitext(filename)
        if ext == ".py":
            yield filename
            
            
def print_python_files(pyfiles):
    for pyfile in pyfiles:
        print(pyfile)

        
def find_python_files_in(dir):
    filenames = gen_paths_of_files_in(dir)
    pyfiles = gen_python_files(filenames)
    print_python_files(pyfiles)
    
    
def gen_loc_in_python_files(pyfiles):
    for pyfile in pyfiles:
        try:
            with open(pyfile, 'r') as fp:
                for _ in fp:
                    yield 1
        except IOError:
            print(pyfile + " not found")

def get_loc_in_python_files_in(dir):
    filenames = gen_paths_of_files_in(dir)
    pyfiles = gen_python_files(filenames)
    loc = sum(gen_loc_in_python_files(pyfiles))
    
    print(loc)
    
    
def gen_loc_without_comments_or_empty_lines_in_python_files(pyfiles):
    for pyfile in pyfiles:
        try:
            with open(pyfile, 'r') as fp:
                for line in fp:
                    if line: # filter out empty lines
                        if line.startswith('#'):
                            continue  #filter out comments
                        yield 1
        except IOError:
            print(pyfile + " not found")
    
    
def get_loc_without_comments_or_empty_lines_in_python_files_in(dir):
    filenames = gen_paths_of_files_in(dir)
    pyfiles = gen_python_files(filenames)
    loc = sum(gen_loc_without_comments_or_empty_lines_in_python_files(pyfiles))
    print(loc)
    
def get_file_name(fp, n):
    i = 0
    if i < n:
        file_name = fp.name + "_" + i//n
        yield file_name
    
    
def write_n_lines(filename, n_lines):
    name, ext = os.path.splitext(filename)
    new_file_name = f"{name}_{write_n_lines.i}{ext}"
    with open(new_file_name, 'w') as write_fp:
        for line in n_lines:
            write_fp.write(line)
    write_n_lines.i += 1
    
    
def split_into_n_files(file, n):
    write_n_lines.i = 0
    with open(file, 'r') as read_fp:
        #while read_fp: # This becomes an infinite loop in python because read_fp has the
                       # byte position it is pointing to, and not the value, so no EOF detection.
                       # The correct check is while read_fp.read() or read_fp.readline()
                       # But when you do this, the current line or all of the next bytes
                       # get eaten in the check, so use tell and seek to set the file pointer
                       # in the right location
        try:
            curr_pos = read_fp.tell()
            data = read_fp.readline()
            
            while data:
                read_fp.seek(curr_pos)
                print(f"Start: {read_fp.tell()}")
                n_lines = (read_fp.readline() for _ in range(n))
                write_n_lines(file, n_lines)
                print(f"End: {read_fp.tell()}")
                curr_pos = read_fp.tell()
                data = read_fp.readline()
                
        except IOError:
            print("Oops!")
            
            
def delete_file_gen(pattern):
    for file in iglob(pattern):
        if os.path.exists(file):
            print(f"Deleting {file} ...")
            os.remove(file)
    
    
if __name__ == '__main__':
    # print(f"Pythagorean triplets: {timeit(pythagorean_triplets, number=10)} seconds")
    # print(pythagorean_triplets())

    # Anandology Problem 1: takes a list of filenames as arguments and prints
    # only the line which has a particular substring
    # find_pattern_in_files("dshim", ["./data/DDRStat.out", "./data/ddr_stat_working.out"])
    
    # Find ToDos in codebase
    for pattern in ["TODO", "FIXME"]:
        print(f"\n\nPending {pattern}\n\n")
        find_pattern_in_files(pattern,
                          iglob("/Users/sthitid/software/sambaflow/**/*.py", recursive = True))


    # Anandology Problem 2: Write a program that takes one or more filenames as arguments and prints
    # all the lines which are longer than 40 characters.
    # find_lines_of_len_in_files(40, iglob("/Users/sthitid/Desktop/*.txt", recursive=False))

    # Anandology Problem 3: Write a function findfiles that recursively descends the directory tree for
    # the specified directory and generates paths of all the files in the tree.
    # find_paths_of_files_in('/Users/sthitid/Desktop')

    # Anandology Problem 4: Write a function to compute the number of python files (.py extension)
    # in a specified directory recursively.
    # find_python_files_in('/Users/sthitid/Documents/my_python_projects')
    
    # Anandology Problem 5: Write a function to compute the total number of lines of code in
    # all python files in the specified directory recursively.
    # get_loc_in_python_files_in('/Users/sthitid/Documents/my_python_projects')
    
    # Anandology Problem 6: Write a function to compute the total number of lines of code, ignoring empty and
    # comment lines, in all python files in the specified directory recursively.
    # get_loc_without_comments_or_empty_lines_in_python_files_in('/Users/sthitid/Documents/my_python_projects')
    
    # Anandology Problem 7: Write a program split.py, that takes an integer n and a filename as command
    # line arguments and splits the file into multiple small files with each having n lines.
    # split_into_n_files("/Users/sthitid/Documents/my_python_projects/data/DDRStat.out", 100)
    
    
    # LEARNING 1: The thing about generators is they are pipelines - set them up for a single element and the final
    # consumer (for loop or print) will drive the pipeline for all the elements in the dataset
    # You can build data pipelines with multiple generators
    
    
    # LEARNING 2: None of this understanding about generators prepared me for the task of deleting 1.8 million files
    # that got generated from a wrong solution to Problem 7. above. I tried bash scripts which I just couldn't get to
    #  work, then I tried a python script with generator, which I just couldn't iterate over, only to realize
    # that iglob returns a generator, and all I needed to do is to iterate over iglob (i in iglob stands for iterator!)

    # delete_file_gen("/Users/sthitid/Documents/my_python_projects/data/DDRStat_*.out")
