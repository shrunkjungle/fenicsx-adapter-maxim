#!/bin/sh
set -e -u

while getopts ":dn" opt; do
  case ${opt} in
  d)
    python3 fenicsx_adapter_folder/tutorials/partitioned-heat-conduction/fenicsx/heat.py -d --error-tol 10e-3
    ;;
  n)
    python3 fenicsx_adapter_folder/tutorials/partitioned-heat-conduction/fenicsx/heat.py -n --error-tol 10e-3
    ;;
  \?)
    echo "Usage: cmd [-d] [-n]"
    ;;
  esac
done
