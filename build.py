#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import glob
import click
import simplejson
import yaml
from attrdict import AttrDict
from click.core import Context


def find_config_file():
    files = os.listdir(os.curdir)

    def _f(file_name):
        if re.match(r".*\.(?:json|yml|yaml)", file_name) is None:
            return False

        with open(os.path.join(os.curdir, file_name), "r") as f:
            if "runtime-version" not in f.read():
                return False

        return True

    cfg_files_iter = filter(_f, files)
    try:
        return os.path.join(os.curdir, next(cfg_files_iter))
    except StopIteration:
        raise FileNotFoundError()


def load_cfg_file(file_path):
    ext = os.path.splitext(os.fspath(file_path))[1]
    with open(file_path, "r", encoding="utf-8") as f:
        if ext == ".json":
            return simplejson.load(f)
        else:
            return yaml.safe_load(f)


@click.group()
@click.pass_context
def main(ctx: Context):
    """A simple program to make flatpak build and test easier"""
    obj = AttrDict()
    ctx.obj = obj

    obj.repo_dir = os.environ.get(
        "FLATPAK_REPO",
        os.path.expandvars(os.path.expanduser("~/.local/share/flatpak-repo")),
    )

    obj.build_dir = os.environ.get("FLATPAK_BUILD_DIR", "./.build")


@main.command()
@click.pass_obj
def run_sh(obj: AttrDict):
    """Run the 'sh' shell in the build environment
    """

    cfg_path = find_config_file()

    os.system("flatpak-builder --run %s %s sh" % (obj.build_dir, cfg_path))


@main.command()
@click.pass_obj
def build(obj: AttrDict):
    """Start a build
    """

    cfg_path = find_config_file()
    os.system(
        "flatpak-builder --ccache --force-clean --repo=%s %s %s"
        % (obj.repo_dir, obj.build_dir, cfg_path)
    )


@main.command()
@click.pass_obj
def bundle(obj: AttrDict):
    """Bundle the application
    """

    cfg_path = find_config_file()
    cfg = load_cfg_file(cfg_path)

    kwargs = {
        "repo_dir": obj.repo_dir,
        "build_dir": obj.build_dir,
        "app_id": cfg["app-id"],
    }

    click.echo("Clean old bundles ...")
    os.remove("{app_id}.flatpak".format(**kwargs))
    os.remove("{app_id}.Locale.flatpak".format(**kwargs))

    click.echo("Building bundles ...")
    os.system(
        "flatpak build-bundle "
        "{repo_dir} {app_id}.flatpak {cfg_path}".format(**kwargs)
    )

    os.system(
        "flatpak build-bundle --runtime "
        "{repo_dir} {app_id}.Locale.flatpak {cfg_path}".format(**kwargs)
    )

    click.echo("Bundle generate successed.")


if __name__ == "__main__":
    main()
