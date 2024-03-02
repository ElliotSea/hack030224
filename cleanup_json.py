import json
import sys

common_fields = ['product title', 'product description']
review_fields = ['review title', 'review contents']


def take_only_needed_fields(inpath, outpath):
	with open(inpath, 'r') as orig:
		data = json.load(orig)
		output_object = {}
		
		for common in common_fields:
			output_object[common] = data[0][common]
		all_crealed_reviews = []

	for review in data:

		print(review.items())
		cleared_review = {}
		for key, value in review.items():
			if key in review_fields:
				cleared_review[key] = value
		all_crealed_reviews.append(cleared_review)

	output_object['reviews'] = all_crealed_reviews

	with open(outpath, 'w') as modif:
		json.dump(output_object, modif, ensure_ascii=False)


#remove_fields(sys.argv[1], sys.argv[2])
take_only_needed_fields(sys.argv[1], sys.argv[2])

#parse("sample_jsons/sample1.json", "cleaned_json.json")
#python json_parser.py sample_json/sample1.json cleaned_json.json
