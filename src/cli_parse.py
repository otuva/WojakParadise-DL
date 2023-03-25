import argparse

epilog = """
Examples:
  python main.py -a download -t "category" -v "Fallout : New Vegas" --min 2 --max 7 #  download 5 
  python main.py -a download -t "tag" -v "New California Republic" --all  # download all
  python main.py -a list -t "tag" -v "Militia Forces"  # list all wojaks with the tag
  python main.py -a list -t "ws" -vv  # list wojak studio made images with verbosity. Around ~2500 images

To bug report: https://github.com/otuva/WojakParadise-DL/issues"""

parser = argparse.ArgumentParser(
    prog='WojakParadise-DL',
    description='Python script to easily batch download wojaks from wojakparadise.net',
    epilog=epilog,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-a",
                    metavar="ACTION",
                    help="Action to perform. (list, download)",
                    required=True,
                    choices=["list", "download"])

parser.add_argument("-t",
                    metavar="TYPE",
                    help="Call script with a type. (category, tag, ws)",
                    choices=["category", "tag", "ws"])

parser.add_argument("-v",
                    metavar="VALUE",
                    help="Value to use with the type. \
                    Will be url encoded so type what you see in the site. \
                    Type 'ws' does not require a value and will be ignored.")

parser.add_argument("-vv",
                    help="Set http logging level to verbose",
                    action="store_true"
                    )

parser.add_argument("--min",
                    help="Minimum download range",
                    type=int,
                    )

parser.add_argument("--max",
                    help="Maximum download range. If not supplied it will be limitless.",
                    type=int,
                    )

# parser.add_argument("--range",
#                     help="Download a range. Use it with --min and --max",
#                     action="store_true")

parser.add_argument("--all",
                    help="Download all",
                    action="store_true")


# parser.add_argument("--download-range",
#                     action="store_true",
#                     help="Download a given range. Used with --min and --max")
