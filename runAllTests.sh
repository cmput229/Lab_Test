#!/bin/sh
git submodule foreach git pull
for input in $(ls tests/*.in)
do
    test=${input%.in}
    output=$test.out
    echo "Test case: $test"
    ./runTest.sh $input $output
done
