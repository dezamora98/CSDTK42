import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="A9GTools improve the work with the AiThinker SDK for the creation of projects on the A9G board")
    subparsers = parser.add_subparsers(dest="command", required = True)

    parser_create = subparsers.add_parser("create", help = "Create a new A9G_SDK project")
    parser_create.add_argument("name", help = "Name or address for project")
    
    parser_build = subparsers.add_parser("build", help = "Build project")
    parser_build.add_argument("name", nargs="?", default=".", help= "Name or address for project")

    parser_build = subparsers.add_parser("fota", help = "Build project and create fota.pack (needs a previous compilation of the project in the hex folder)")
    parser_build.add_argument("name", nargs="?", default=".", help= "Name or address for project")
    
    parser_clean = subparsers.add_parser("clean", help = "Delete project builds")
    parser_clean.add_argument("name", nargs="?", default=".", help= "Name or address for project")

    subparsers.add_parser("coolwatcher", help = "Open coolwatcher")
    subparsers.add_parser("update", help = "Update A9Gtools through the https://github.com/dezamora98/CSDTK42")
    subparsers.add_parser("install", help = "Add A9Gtools to the environment variables so that it can be used from any path in the project")
    
    return parser.parse_args(args)
