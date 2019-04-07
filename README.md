# org.sorn.KiCad

This is an unofficial flatpak app wrapper for KiCad.

There already have a official flatpak version for KiCad [This](https://github.com/flathub/org.kicad_pcb.KiCad), but seems it have features missing:

1. No python support
1. BOM generation not working

Seems they not actively work on that project. And they does not pay close attention to the project and left issues die alone.

So I create this project for satisfy my needs until the offical project go further.

## Features

1. Supported Python 2.7 with action scripts
1. BOM generation works (included libxslt)
1. Updated to latest KiCad (5.1.0 currently)
1. Updated to latest flatpak runtime (org.gnome.Platform 3.30 currently)

## Installation

There have two ways to install this distribution:

1. Build and install your flatpak
1. Download and install the flatpaks I builded from Github [Releases](https://github.com/fpchump/org.sorn.KiCad/releases)

## Know Issues

### Input Method

Flatpak only support iBus, so if you want to input foreign language text to KiCad, you must switch to iBus. Other input method just like xim/fcitx/scim/iiim are unsupported and you may meet crash or freeze problems with them.
