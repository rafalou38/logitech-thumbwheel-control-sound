#!/usr/bin/env python3

import pulsectl

import os

os.environ['PULSE_SERVER'] = 'unix:/run/user/1000/pulse/native'
os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'

INCREMENT = 1
FIFO_PATH = "/tmp/volume_control_fifo"


def increment_volume(increment=5):
    with pulsectl.Pulse("volume-increment") as pulse:

        sink = pulse.get_sink_by_name("@DEFAULT_SINK@")

        current_volume = (
            sink.volume.values[0] * 100
        )

        new_volume = max(
            0, min(current_volume + increment, 100)
        )

        pulse.volume_set_all_chans(sink, new_volume / 100)

        print(f"Volume increased to {new_volume}%")


if not os.path.exists(FIFO_PATH):
    os.mkfifo(FIFO_PATH)
try:
    while True:
        with open(FIFO_PATH, "r") as fifo:
            mode = fifo.read().strip()

        if mode == "up":
            increment_volume(INCREMENT)
        elif mode == "down":
            increment_volume(-INCREMENT)
except KeyboardInterrupt:
    print("User script terminated.")