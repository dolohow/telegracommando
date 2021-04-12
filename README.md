Telegracommando
===============

Run predefineed bash scripts and get output in telegram.


## Running
Configuration resides in file called `telegracommando.ini` which you must
edit.

### Docker (recommended)
I prefer to use podman instead of docker, which I highly recommend:
```
podman run -d \
    --name telegracommando \
    -v PATH_TO_CONFIG:/config \
    -v PATH_TO_COMMANDS:/usr/src/app/commands.d \
    dolohow/telegracommando
```

### PIP
You need Python 3 to run this program.

```
pip install -r requirements.txt
```

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
is the name of the script.  You can also pass arguments to script, they would
be available in bash as `$1`, `$2` and so on...  And don't forget to add
executable permission like that:

```
chmod +x commands.d/custom_script
```

## Security
You should probably not give access to this bot to people you don't trust. It
was not designed with security in mind.  However I implemented some
mitigation that might help a bit.
