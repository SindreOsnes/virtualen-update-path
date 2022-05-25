import argparse


def update_path():
    argument_parser = argparse.ArgumentParser(description="Add a path update to a virualenv")

    argument_parser.add_argument("EnvPath", metavar='env-path', type=str, help='The path to the environment')
    argument_parser.add_argument("PathAddition", metavar='path', type=str, help='The path to add to the environment variables')

    args = argument_parser.parse_args()

    env_path = args.EnvPath
    path_addition = args.PathAddition

    print(env_path)
    print(path_addition)



