#! /bin/bash

c_name=`ls -lt ./ | head -n 2 |awk '{print $9}'`
echo "$c_name"
`git add -A`
`git commit -m $c_name`
`git push`
