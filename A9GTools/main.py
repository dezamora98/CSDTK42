import sys

from args import parse_args
from functions import build_project, create_project, clean_project, load_project

def main():
    args = parse_args(sys.argv[1:])
    if args.command == "create":
        create_project(args.name)
    elif args.command == "build":
        build_project(args.name)
    elif args.command == "clean":
        clean_project(args.name)
    elif args.command == "load":
        load_project()
        
    return

if __name__ == "__main__":
    main()