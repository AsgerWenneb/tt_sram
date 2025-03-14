# Attempt at including small prehardened macro in Openlane2

We have created an inverter in magic and attempted to include is as a macro in the Openlane2 flow. This is meant as a first step before attempting to use bigger macros (e.g. OpenRam).

## The setup

The mag, lef, gds and vh files for the inverter are located in src/invering_buffer (creative spelling...). They are included by the inverter_top.v file in src.

Some of the power routing issues have been fixed (like increasing die area), but other settings in config.json have been set in a desperate attempt to fix the issue.

Currently we manage to get the following error message:

![Openlane errors](image.png)
