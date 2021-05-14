# PDF to CSV

## Install

Download and install [python3](https://www.python.org/downloads/)

In root folder run

```bash
python3 -m venv env
source env/bin/activate
pip3 install requirements.txt
```

## Run

```bash
python3 convert.py -i filename.pdf  -o nameforoutputfile.csv
```

Not working, something about virtualenv not being on path.

```bash
./convert.py -i 514PPR300.pdf  -o 514PPR300.csv
```
