#!/bin/bash

files=('train_file__2022Aug31_1100utc_24hr.tsv' 'train_fileshuffle__2022Aug31_1100utc_24hr.tsv')
outmodelname=('model.txt' 'model_shuffle.txt')

for ((idx=0; $idx<2; idx++))
do
 echo ${files[$idx]}
 echo ${outmodelname[$idx]}
 python train_lbfgs_cpu_pr2.py ${files[$idx]} ${outmodelname[$idx]} > train_lbfgs_cpu_pr2_log${idx}.log 2>&1
done
