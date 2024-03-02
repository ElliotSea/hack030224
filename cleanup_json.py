import json
import sys

# fields to remove
notneeded_fields = ['size', 'gender']

fields_to_keep = ['product title', 'review title', 'review contents']


# parse the input json file and remove unnecessary fields and write to the output json file
def remove_fields(inpath, outpath):
	with open(inpath, 'r') as orig:
		data = json.load(orig)
		print("Original data", data)
		cleared_data = {}

	for key, value in data.items():
		if key not in notneeded_fields:
			cleared_data[key] = value

	with open(outpath, 'w') as modif:
		json.dump(cleared_data, modif)


def take_only_needed_fields(inpath, outpath):
	with open(inpath, 'r') as orig:
		data = json.load(orig)
		print("Original data", data)
		all_crealed_reviews = []

	for review in data:

		print(review.items())
		cleared_review = {}
		for key, value in review.items():
			if key in fields_to_keep:
				cleared_review[key] = value
		all_crealed_reviews.append(cleared_review)

	with open(outpath, 'w') as modif:
		json.dump(all_crealed_reviews, modif, ensure_ascii=False)


#remove_fields(sys.argv[1], sys.argv[2])
take_only_needed_fields(sys.argv[1], sys.argv[2])

#parse("sample_jsons/sample1.json", "cleaned_json.json")
#python json_parser.py sample_json/sample1.json cleaned_json.json
