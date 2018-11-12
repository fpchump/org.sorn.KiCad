#!/bin/sh


docker exec -it -v$PWD:/w build-env "cd /w; $*"
