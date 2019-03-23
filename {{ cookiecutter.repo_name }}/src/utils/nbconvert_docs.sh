#!/bin/bash

# nbconvert_docs.sh
# Description: create .rst files from development notebooks.

set -u

function main() {
    proj_dir=$1
    for nb in $(ls ${proj_dir}/notebooks/dev | grep ipynb); do
        jupyter nbconvert --to rst --output-dir ${proj_dir}/docs \
            ${proj_dir}/notebooks/dev/${nb}
        done
}

main $1
