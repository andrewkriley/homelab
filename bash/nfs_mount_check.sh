#!/bin/bash

# Define the NFS server and share details
NFS_SERVER=$1
#NFS_SHARE=$2
NFS_PORT=2049

# Use 'nc' to check if the NFS mount is available
if nc -w 1 ${NFS_SERVER} ${NFS_PORT}; then
  echo "NFS service is available on ${NFS_SERVER}"
else
  echo "NFS service is NOT available on ${NFS_SERVER}"
fi
