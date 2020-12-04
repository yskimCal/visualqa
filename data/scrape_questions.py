import json

with open('VQA_dataset.json') as fileJSON:
    data = json.load(fileJSON)

# print([image["qa_pairs"] for image in data["images"]])
scrapedQuestions = []

keywords = ["man","woman","girl","boy","men","women","happy","sad","angry","surprise","disgust","fear","neutral","people","human","he","she","him","her"]

for image in data["images"]:
    # print(image)
    qa_pairs = image["qa_pairs"]
    for qa_pair in qa_pairs:
        if any(x in qa_pair["question"].split(" ") for x in keywords):
            scrapedQuestions.append(image)
        elif any(x in ' '.join(qa_pair["multiple_choices"]).split(" ") for x in keywords):
            scrapedQuestions.append(image)
        elif any(x in qa_pair["answer"].split(" ") for x in keywords):
            scrapedQuestions.append(image)
        break

# print(scrapedQuestions)

with open('result.json', 'w') as result:
    json.dump(scrapedQuestions, result)