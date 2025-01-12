import sys
import os
from args import parse_args
from functions import build_project, create_project, clean_project, open_coolwatcher, create_fota_pack, update

def main():  
    args = parse_args(sys.argv[1:])
    if args.command == "create":
        create_project(args.name)
    elif args.command == "build":
        build_project(args.name)
    elif args.command == "clean":
        clean_project(args.name)
    elif args.command == "coolwatcher":
        open_coolwatcher()
    elif args.command == "fota":
        create_fota_pack(args.name)
    elif args.command == "update":
        update()
    return

if __name__ == "__main__":
    main()