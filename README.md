# [Aplikacja do analizy opinii](https://github.com/JokeUrSelf/msi-opinion-rating)

## Project setup with Nix
Install [nix](https://nixos.org/download/) package manager and enable [flakes](https://wiki.nixos.org/wiki/Flakes)

In the project root run the command to setup the project:
```sh
nix-shell
```

## Project setup with pip
Install [python](https://www.python.org/downloads/)

### Linux setup
In the project root run the command to setup the project:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

In the project root run the command to run the project:
```sh
python main.py
```


### Windows setup
In the project root run the command to setup the project:
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

In the project root run the command to run the project:
```sh
python main.py
```
