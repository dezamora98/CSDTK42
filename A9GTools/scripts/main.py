import sys
import os
from args import parse_args
from functions import build_project, create_project, clean_project, open_coolwatcher, create_fota_pack, update, install

def main():  
    # Check if the environment variable already exists and has the same value
    if os.environ.get("GPRS_CSDTK42_PATH") != os.path.dirname(os.path.dirname((os.path.dirname(sys.executable)))).replace("/","\\"):
        install()
        return
    
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
    elif args.command == "install":
        install()
    return

if __name__ == "__main__":
    main()