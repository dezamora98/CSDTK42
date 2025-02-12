import sys
import os
import shlex
import time
from datetime import datetime
import utils
from update import update
from args import parse_args


def main():  
    start_time = time.time()
    # Check if the environment variable already exists and has the same value
    config = utils.A9gtools()

    print(f"A9GTools {config.get('A9GTools')}")
    
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python {python_version}\n")
    
    csdtk42_path = config.get("CSDTK_PATH")
    
    if sys.argv[1] == "rshell":
        os.system(f"python {config.get('rshell')} {shlex.join(sys.argv[2:])}")
        return

    args = parse_args(sys.argv[1:], config.get("A9GTools"))

    if args.command == "create":
        config.create_project(args.name, args.micropython)
    elif args.command == "build":
        config.make(args.name, args.mode)
    elif args.command == "clean":
        config.clean_project(args.name)
    elif args.command == "coolwatcher":
        config.open_coolwatcher()
    elif args.command == "fota":
        config.run_fota(args.old, args.new, args.out)
    elif args.command == "update":
        update(csdtk42_path)
    elif args.command == "install":
        config.install()

    end_time = time.time()
    print("=================================================\n"\
          f"Start Time : {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}\n"\
          f"End Time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}\n"\
          f"Duration: {(end_time - start_time):.2f} s\n"\
          "=================================================")
    return

if __name__ == "__main__":
    main()