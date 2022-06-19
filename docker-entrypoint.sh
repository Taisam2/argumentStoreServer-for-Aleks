#!/bin/bash
set -e

./wait-for-it.sh "argumentstore.lkyrg.mongodb.net:27017"

exec "$@"