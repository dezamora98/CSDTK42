import sys
import argparse

def parse_args(args, version):
    parser = argparse.ArgumentParser(
        description="A9GTools improve the work with the AiThinker SDK for the creation of projects on the A9G board"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser.add_argument("-v", "--version", action="version", version=f"A9GTools {version}")

    parser_create = subparsers.add_parser(
        "create",
        help="Create a C or MicroPython project (for micropython projects use -m or --micropython argument).",
        usage="A9GTools create -n <project_path> [-m]"
    )
    parser_create.add_argument("-n", "--name", required=True, help="Name or address for project")
    parser_create.add_argument("-m", "--micropython", action="store_true", help="Create a MicroPython project")

    parser_build = subparsers.add_parser(
        "build",
        help="Build project",
        usage="A9GTools build -n <project_path> -m <debug|release>"
    )
    parser_build.add_argument("-n", "--name", default=".", help="Name or address for project")
    parser_build.add_argument(
        "-m", "--mode", 
        default="debug", 
        choices=["debug", "release"],
        help="Select compile mode (debug or release)"
    )

    parser_fota = subparsers.add_parser(
        "fota",
        help="Build project and create fota.pack (needs a previous compilation of the project in the hex folder)",
        usage="A9GTools fota --old <old_lod> --new <new_lod> --out <output_pack>"
    )
    parser_fota.add_argument("--old", required=True, help="old .lod firmware file")
    parser_fota.add_argument("--new", required=True, help="new .lod firmware file")
    parser_fota.add_argument("--out", required=True, help="final .lod firmware file")

    parser_clean = subparsers.add_parser("clean", help="Delete project builds")
    parser_clean.add_argument("name", nargs="?", default=".", help="Name or address for project")

    subparsers.add_parser("coolwatcher", help="Open coolwatcher")
    subparsers.add_parser("rshell", help="Open rshell with specified arguments")
    subparsers.add_parser("update", help="Update A9Gtools through the https://github.com/dezamora98/CSDTK42")
    subparsers.add_parser("install", help="Add A9Gtools to the environment variables")

    if not args:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args(args)