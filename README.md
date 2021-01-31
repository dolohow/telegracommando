Telegracommando
===============

Run predefineed bash scripts and get output in telegram.


## Installation
You need Python 3 to run this program.

```
pip install -r requirements.txt
```

Create configuration file

```
cp tdpt.ini.template tdpt.ini
```

Edit and save


## Running
```
python telegracommando.py
```

Id does not at the time run as daemon, so you can run it in `screen`, `tmux`
or create `systemd` service.

You can also use nohup
```
nohup python telegracommando.py &
```

## Custom scripts
You can put your custom scripts in `commands.d` directory.  There are few
already created for you to see how that works.  Command name in Telegram
is the name of the script.  And don't forget to add executable permission
like that

```
chmod +x commands.d/custom_script
```

## Security
You should probably not give access to this bot to people you don't trust. It
was not designed with security in mind.

## TODO
Add way to pass arguments in secure and easy manner.
