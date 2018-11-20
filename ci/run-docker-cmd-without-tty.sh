#!/bin/sh

rm cmd-run.log
docker exec -i build-env bash -c "cd /w; $*" 1>>cmd-run.log 2>>cmd-run.log &
