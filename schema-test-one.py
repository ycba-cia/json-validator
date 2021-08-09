
import json
import jsonschema
import os

from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError
import json
from pathlib import Path

#to fix hardcoded in this Rob Sanderson repo:
#sed -i -- 's*rs2668/Development/other/linked-art*ermadmix/documents/github_clones*g' *.json

model_dirs = {
	"activity": "event",
	"digital": "digital",
	"group": "group",
	"object": "object",
	"person": "person",
	"place": "place",
	"provenance": "provenance",
	"set": "set",
	"text":"text",
	"visual": "image"
}


base_instance_dir = "/home/ec2-user/reconciliation/data/ycba/linked_art/activity"

schema_dir = "schema/event.json"

schemafn = os.path.join(schema_dir)
fh = open(schemafn)
schema = json.load(fh)
fh.close()
v = Draft7Validator(schema)
exampledir = os.path.join(base_instance_dir)
for path in Path(exampledir).rglob('*.json'):
	f = str(path)
	if f.endswith('.json'):
		fn = path
		print("-"*120)
		print("Processing: %s" % fn)
		fh = open(fn)
		data = json.load(fh)
		fh.close()
		errs = []
		for error in v.iter_errors(data):
			errs.append(error)
			# 	print(error.absolute_schema_path) <-- this is the current path through the schema 
			print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message} ")
		if not errs:
			print("  Validated!")
