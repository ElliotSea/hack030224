import json

# fields to remove
notneeded_fields = ['fruit', 'gender']

# parse the input json file and remove unnecessary fields and write to the output json file
def parse(inpath, outpath):
	with open(inpath, 'r') as orig:
		data = json.load(orig)
	for item in data:
		for field in notneeded_fields:
			if field in item:
				del item[field]

	with open(outpath, 'w') as modif:
		json.dump(data, modif)




parse("sample_jsons/sample1.json", "cleaned_json.json")