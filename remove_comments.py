#!/bin/env
import os

def remove_comments(read_file: str, write_file: str) -> str:

    with open(read_file) as fp:
        print(fp.buffer, flush=True)

    no_comment_code = ''

    with open(read_file) as fp:
        for line in fp:
            if '#' not in line:
                no_comment_code += line
            else:
                code, _ = line.split(sep='#')
                no_comment_code += code

    with open(write_file, 'w+') as fp:
        fp.write(no_comment_code)


read_file = os.path.join(os.getcwd(), 'tests', 'test_comment.txt')
write_file = os.path.join(os.getcwd(), 'tests', 'test_code.txt')
remove_comments(read_file, write_file)
