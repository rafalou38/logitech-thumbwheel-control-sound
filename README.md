# Linux Sound Volume Control

Simple script which translate thumb-wheel scroll on Logitech mouse to a volume increase.
There are two scripts: `sound_control_master.py` and `sound_control_slave.py`.


## Dependencies

```bash
sudo apt install python3-pulsectl python3-evdev 
```

## Usage

### Master

This file should be ran as root so check your permissions.
```
sudo chown root:root ./sound_control_master.py 
```

Edit `device_path`, you can find it with `evtest`.

```ini
[Unit]
Description=Root Script for Volume Control
After=network.target

[Service]
Type=simple
ExecStart=/home/rafael/scripts/mouse/sound_control_master.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Slave

This file is ran as the user to access the pulse server.

```ini
[Unit]
Description=User Script for Volume Control
After=network.target

[Service]
Type=simple
User=<Enter user here>
ExecStart=/home/rafael/scripts/mouse/sound_control_slave.py
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```