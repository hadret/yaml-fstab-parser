#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml


def main():
    # Grab YAML data from the file
    with open('fstab.yaml', 'r') as f:
        fstab = yaml.safe_load(f)

    # Load in the devices
    devices = fstab["fstab"]

    # Iterate through keys and values for each device
    for key, value in devices.items():

        """ Print options next to each other separated by a single comma when
        there are any options at all"""
        options = ",".join(value["options"])\
                  if "options" in value else "defaults"

        # Include export when printing value for NFS
        if "nfs" in value["type"]:
            print((
                f'{key}:{value["export"]}\t{value["mount"]}'
                f'\t{value["type"]}\t{options}'
                ))
        else:
            print(f'{key}\t{value["mount"]}\t{value["type"]}\t{options}')


if __name__ == "__main__":
    main()
