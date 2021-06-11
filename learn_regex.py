import functools
import re
import sys
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        for i in range(100):
            value = func(*args, **kwargs)
        stop = time.perf_counter()
        runtime = stop - start
        print(f'{func.__name__} took {runtime:.4f} seconds')
        return value
    return wrapper_timer
    
@timer
def findall_replace(args):
    infra_opts = args
    matches = re.findall(r'--snrdu-opts=.+', infra_opts)
    infra_opts = infra_opts.replace(matches[0], '')
    # print(infra_opts)
    
@timer
def compiled_regex_substitute(args):
    # Compiled regex
    regex = re.compile(r'--snrdu-opts=.+')
    infra_opts = regex.sub('', args)
    print(infra_opts)
    
    
@timer
def regex_substitute(args):
    # Even better way: re.sub
    infra_opts = re.sub(r'--snrdu-opts=.+', '', args)
    print(infra_opts)
    
    
def main():
    a_list = ['apple', 'banana', 'carrot', 'daikon']
    
    found = 'carrots' in a_list
    if found:
        print(f"'carrots' found in {a_list}")
        
    else:
        search_list = re.findall('carrot*', 'carrots')
        if search_list:
            print(f"'carrot found in {search_list}!")

    args = ' '.join(sys.argv[1:])
    findall_replace(args)
    regex_substitute(args)
    compiled_regex_substitute(args)
    
    
if __name__ == '__main__':
    main()