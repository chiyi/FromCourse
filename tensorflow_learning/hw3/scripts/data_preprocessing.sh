#!/bin/bash

SCFULLNAME=`realpath $0`
SCPATH=`dirname $SCFULLNAME`
PROJPATH=`realpath $SCPATH/..`
export TZ=Asia/Taipei

cd $SCPATH/../data
echo current pwd = $PWD

mkdir food-11_fortf
mkdir food-11_fortf/training
mkdir food-11_fortf/validation

#for labels='inferred'
ls food-11/training/*.jpg | awk -F '/' '{print $NF}' | awk -F '_' '{print $1}' | sort | uniq | awk '{print "mkdir food-11_fortf/training/"$1}' | awk '{system($0)}'
ls food-11/training/*.jpg | awk -F '/' '{print $NF}' | awk -F [_.] '{label=$1; ithfile=$2; filename=$0; tmpstr = sprintf("cp food-11/training/%s food-11_fortf/training/%s/%s_%04d.jpg", filename, label, label, ithfile); print tmpstr;}' | awk '{system($0)}'
#    
#    #for labels={a list/tuple of integer labels of the same size as the number of image files found in the directory}
#    #!ls food-11/training/*.jpg | awk -F '/' '{print $NF}' | awk -F [_.] '{label=$1; ithfile=$2; filename=$0; tmpstr = sprintf("cp food-11/training/%s food-11_fortf/training/%02d_%04d.jpg", filename, label, ithfile); print tmpstr;}' | awk '{system($0)}' >> tmp.log 2>&1



#for labels='inferred'
ls food-11/validation/*.jpg | awk -F '/' '{print $NF}' | awk -F '_' '{print $1}' | sort | uniq | awk '{print "mkdir food-11_fortf/validation/"$1}' | awk '{system($0)}'
ls food-11/validation/*.jpg | awk -F '/' '{print $NF}' | awk -F [_.] '{label=$1; ithfile=$2; filename=$0; tmpstr = sprintf("cp food-11/validation/%s food-11_fortf/validation/%s/%s_%04d.jpg", filename, label, label, ithfile); print tmpstr;}' | awk '{system($0)}'
#for labels={a list/tuple of integer labels of the same size as the number of image files found in the directory}
#!ls food-11/validation/*.jpg | awk -F '/' '{print $NF}' | awk -F [_.] '{label=$1; ithfile=$2; filename=$0; tmpstr = sprintf("cp food-11/validation/%s food-11_fortf/validation/%02d_%04d.jpg", filename, label, ithfile); print tmpstr;}' | awk '{system($0)}' >> tmp.log 2>&1

cd $PROJPATH
echo current pwd = $PWD
