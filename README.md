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
1. Separated KiCad data so the user could update symbols/footprints/templates/packages3D easily
1. Updated to latest KiCad (5.1.0 currently)
1. Updated to latest flatpak runtime (org.gnome.Platform 3.30 currently)

## Installation

There have two ways to install this distribution:

1.  Build and install your flatpak
1.  Download and install the flatpaks I builded from Github [Releases](https://github.com/fpchump/org.sorn.KiCad/releases)

    (We only builded for arch x86_x64, if you want other arches, just build yourself)

    Download `org.sorn.KiCad.flatpak` and `org.sorn.KiCad.Locale.flatpak` to `/tmp` or where you like and follow similar instructions:

        $ cd /tmp
        $ flatpak install org.sorn.KiCad.flatpak
        $ flatpak install org.sorn.KiCad.Locale.flatpak

**NOTICE**: You must notice, this project not bundled with KiCad data, just as symbols/footprints/templates/packages3d/scripts. So you have to download and prepare them yourself.

## Configuration

The config directory flatpak wrapped KiCad not the same with normal KiCad's, it's follow the standard of flatpak how to store app's private data for security reasons.

The correct config directory is : `~/.var/app/org.sorn.KiCad/kicad/config` (Normal KiCad's config stored at `~/.config/kicad`)

If you want to make them unified, you could just remove the directory `~/.var/app/org.sorn.KiCad/kicad/config` and link it to `~/.config/kicad` .

## Scripts

Your custom python script could be place into `~/.kicad/scripting/plugins/`, they will discover by application during runtime.

## Application Data

Normal KiCad will install application data into `/usr/share/kicad/`, but that conflict with flatpak's security rules (We can't access `/usr` directory!).

Now you should download these git libraries and install them to you custom directory and modify the correct KiCad environments:

- https://github.com/KiCad/kicad-symbols
- https://github.com/KiCad/kicad-footprints
- https://github.com/KiCad/kicad-templates
- https://github.com/KiCad/kicad-packages3D

Use cmake to install them, blablabla...

Modify these environments in file `kicad_common` of config directory:

- KICAD_PTEMPLATES
- KICAD_SYMBOL_DIR
- KICAD_TEMPLATE_DIR
- KISYS3DMOD
- KISYSMOD

Point them to correct directory.

Then, add all libraries and symbols names to `fp-lib-table` and `sym-lib-table` .

## Know Issues

### Input Method

Flatpak only support iBus, so if you want to input foreign language text to KiCad, you must switch to iBus. Other input method just like xim/fcitx/scim/iiim are unsupported and you may meet crash or freeze problems with them.
