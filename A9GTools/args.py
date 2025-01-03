import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="A9GTools improve the work with the AiThinker SDK for the creation of projects on the A9G board")
    subparsers = parser.add_subparsers(dest="command", required = True)

    parser_create = subparsers.add_parser("create", help = "Create a new A9G_SDK project")
    parser_create.add_argument("name", help = "Name or address for project")
    
    parser_build = subparsers.add_parser("build", help = "Build project")
    parser_build.add_argument("name", nargs="?", default=".", help= "Name or address for project")
    
    parser_clean = subparsers.add_parser("clean", help = "Delete project builds")
    parser_clean.add_argument("name", nargs="?", default=".", help= "Name or address for project")

    subparsers.add_parser("load", help = "Open coolwatcher")

    return parser.parse_args(args)
