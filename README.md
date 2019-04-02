# org.sorn.KiCad

This is a flatpak app build for KiCad.

There already have a standard flatpak version for KiCad [This](https://github.com/flathub/org.kicad_pcb.KiCad), but seems it have features missing and buggy:

1. No python support
1. BOM generation not working
1. There have other issues that happened during test

Seems they not actively work on that project and does not have well testing. And they does not pay close attention to the project and left issues die alone.

So I create this project for satisfy my needs until the standard project go further.

## Know Issues

### Input Method

Flatpak only support iBus, so if you want to input foreign language text to
KiCad, you must switch to iBus. Other input method framework just like
xim/fcitx/scim/iiim are unsupported and you may meet crash or freeze problems
with them.
