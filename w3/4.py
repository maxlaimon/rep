import json

with open("1.json", "r") as F:
	data = json.load(F)
	data1 = data.copy()
	print(json.dumps(data, indent = 4, sort_keys = True))
	temp = data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
	temp["week"] = 3


with open("1.json", "w") as F:
	json.dump(data, F, indent = 4)
'''
with open("1.json", "w") as F:
	F.write(json.dumps(data, indent = 4))
'''
with open("1.json", "r") as F:
	data2 = json.load(F)
	print(json.dumps(data2, indent = 4, sort_keys = True))
