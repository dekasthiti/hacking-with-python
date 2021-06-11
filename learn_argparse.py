import argparse
import re
import shlex
import sys


def main(argv):
    parser = argparse.ArgumentParser("Infra Opts")
    parser.add_argument('--infra-opts', default='', type=str)
    infra_args = parser.parse_args()
    print(infra_args.i_opts)
    
    matches = re.findall(r'--sr-opts=+',infra_args.i_opts)
    print(matches)
    infra_args.i_opts = [infra_args.i_opts.replace(match, '') for match in matches]
    print(infra_args.i_opts)
    
    sr_parser = argparse.ArgumentParser()
    sr_parser.add_argument('--sr-opts', default='', type=str)
    sr_args, unknown = sr_parser.parse_known_args(shlex.split(infra_args.i_opts))
    print(sr_args.sr_opts)

    if 'timeout' in sr_args.sr_opts:
        old_string = f"{sr_args.sr_opts}"
        infra_args.i_opts = infra_args.i_opts.replace(old_string, '')
        infra_args.i_opts = infra_args.i_opts.replace('--sr-opts=', '')

    print(infra_args.i_opts)


if __name__=='__main__':
    main(sys.argv)
