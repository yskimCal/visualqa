import json

with open('senticap_dataset.json') as senticap_dataset:
    senticap_dataset = json.load(senticap_dataset)

for image in senticap_dataset["images"]:
    for sentence in image["sentences"]:
        sentence["question"] = "What is in this image?"

with open('senticap_dataset_with_question.json', 'w') as file:
    json.dump(senticap_dataset, file)