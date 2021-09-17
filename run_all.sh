#!/bin/sh
dir="output4"
python3 schema-test-one-invalids.py activity event > $dir/activity.log
python3 schema-test-one-invalids.py digital digital > $dir/digital.log
python3 schema-test-one-invalids.py group group > $dir/group.log
python3 schema-test-one-invalids.py object object > $dir/object.log
python3 schema-test-one-invalids.py person person > $dir/person.log
python3 schema-test-one-invalids.py place place > $dir/place.log
python3 schema-test-one-invalids.py provenance provenance > $dir/provenance.log
python3 schema-test-one-invalids.py set set > $dir/set.log
python3 schema-test-one-invalids.py text text > $dir/text.log
python3 schema-test-one-invalids.py visual image > $dir/visual.log
