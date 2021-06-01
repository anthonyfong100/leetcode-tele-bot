import argparse
import os

from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="Load the right env file")
parser.add_argument(
    "-E",
    "--env",
    type=str,
    help="Set env variable to prod or dev",
    default="dev",
)
args = parser.parse_args()

if args.env.lower() == "prod":
    print("loading env variable from prod.env")
    load_dotenv(verbose=True, dotenv_path="prod.env")
else:
    print("loading env variable from dev.env")
    load_dotenv(verbose=True, dotenv_path="dev.env")
