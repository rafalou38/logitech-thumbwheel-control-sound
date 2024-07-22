#!/usr/bin/env python3

import os

from evdev import InputDevice, ecodes


device_path = "/dev/input/event8"
dev = InputDevice(device_path)

FIFO_PATH = '/tmp/volume_control_fifo'

def write_to_fifo(message):
    with open(FIFO_PATH, 'w') as fifo:
        fifo.write(message)

if not os.path.exists(FIFO_PATH):
    os.mkfifo(FIFO_PATH)


for event in dev.read_loop():
    if event.type == ecodes.EV_REL:
        if event.code == ecodes.REL_HWHEEL:
            if event.value > 0:
                write_to_fifo("down")
            elif event.value < 0:
                write_to_fifo("up")
