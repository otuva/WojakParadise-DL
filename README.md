# WojakParadise-DL
Python script to easily batch download wojaks from wojakparadise.net

# Installation

```
git clone https://github.com/otuva/WojakParadise-DL
cd WojakParadise-DL
python -m venv venv
pip install -r requirements.txt
```

```
usage: WojakParadise-DL [-h] -a ACTION [-t TYPE] [-v VALUE] [-vv] [--min MIN] [--max MAX] [--all]

options:
  -h, --help  show this help message and exit
  -a ACTION   Action to perform. (list, download)
  -t TYPE     Call script with a type. (category, tag, ws)
  -v VALUE    Value to use with the type. Will be url encoded so type what you see in the site. Type 'ws' does not
              require a value and will be ignored.
  -vv         Set http logging level to verbose
  --min MIN   Minimum download range
  --max MAX   Maximum download range. If not supplied it will be limitless.
  --all       Download all

Examples:
  python main.py -a download -t "category" -v "Fallout : New Vegas" --min 2 --max 7 #  download 5 
  python main.py -a download -t "tag" -v "New California Republic" --all  # download all
  python main.py -a list -t "tag" -v "Militia Forces"  # list all wojaks with the tag
  python main.py -a list -t "ws" -vv  # list wojak studio made images with verbosity. Around ~2500 images
```

To bug report: https://github.com/otuva/WojakParadise-DL/issues
