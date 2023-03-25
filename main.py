from requests import Session
import json
import shutil
import asyncio

from src import cli_parse
from src import verbosity
from src.api import getList, download

# ------------------------------------

headers = {
    'User-Agent': 'Wojak Downloader 0.1',
}

def main():
    session = Session()
    session.headers = headers

    args = cli_parse.parser.parse_args()

    if args.vv:
        verbosity.set_logging()

    if args.a == "list":
        response_json = getList(session, args.t, args.v)
        print(json.dumps(response_json, indent=4, sort_keys=True))
        print(f"Total of '{len(response_json)}' wojaks")

    elif args.a == "download":
        if args.all:
            response_json = getList(session, args.t, args.v)
            print(f"Downloading {len(response_json)} wojaks (all)")
            download(session, response_json)
        # if min exists and gt 0 AND max doesn't exists or exists and greater than min
        elif ((args.min != None and args.min >= 0) and (args.max == None or (args.max != None and args.min < args.max))):

            response_json = getList(session, args.t, args.v)
            partial_json = response_json[args.min:args.max]
            print(f"Downloading {len(partial_json)} wojaks")
            download(session, partial_json)
        else:
            print(
                f"You have not supplied a valid minimum range ({args.min} < 0). \nTo download all please use --all otherwise use --min and --max")


if __name__ == "__main__":
    main()
