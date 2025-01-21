import sys
import os
from args import parse_args
import shlex
from functions import build_project, create_project, clean_project, open_coolwatcher, create_fota_pack, update, install

def main():  
    # Check if the environment variable already exists and has the same value
    csdtk42_path = os.environ.get("GPRS_CSDTK42_PATH")
    if csdtk42_path != None:
        csdtk42_path.replace("\\","/")
        if csdtk42_path != os.path.dirname(os.path.dirname((os.path.dirname(sys.executable)))):
            install()
            return
    
    if sys.argv[1] == "rshell":
        os.system(f"{csdtk42_path}\\A9GTools\\bin\\rshell.exe {shlex.join(sys.argv[2:])}")
        return

    
    args = parse_args(sys.argv[1:])
    
    if args.command == "create":
        create_project(args.name, args.micropython)
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