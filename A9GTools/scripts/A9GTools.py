import sys
import os
from args import parse_args
import shlex
import time
from datetime import datetime
import functions as fn
from update import update

def main():  
    start_time = time.time()
    # Check if the environment variable already exists and has the same value
    csdtk42_path = os.environ.get("GPRS_CSDTK42_PATH")
    if not os.path.exists(csdtk42_path) or csdtk42_path is None :
        fn.install()
        return
    
    if sys.argv[1] == "rshell":
        os.system(f"{csdtk42_path}\\A9GTools\\bin\\rshell.exe {shlex.join(sys.argv[2:])}")
        return
    
    args = parse_args(sys.argv[1:])
    
    if args.command == "create":
        fn.create_project(args.name, args.micropython)
    elif args.command == "build":
        fn.make(args.name, args.mode)
    elif args.command == "clean":
        fn.clean_project(args.name)
    elif args.command == "coolwatcher":
        fn.open_coolwatcher()
    elif args.command == "fota":
        fn.run_fota(args.old,args.new,args.out)
    elif args.command == "update":
        update(csdtk42_path)
    elif args.command == "install":
        fn.install()

    end_time = time.time()
    print("=================================================\n"\
          f"Start Time : {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}\n"\
          f"End Time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}\n"\
          f"Duration: {(end_time - start_time):.2f} s\n"\
          "=================================================")
    return

if __name__ == "__main__":
    main()