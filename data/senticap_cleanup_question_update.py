import json

with open('senticap_dataset.json') as senticap_dataset:
    senticap_dataset = json.load(senticap_dataset)

for image in senticap_dataset["images"]:
    for sentence in image["sentences"]:
        if sentence["raw"].find("girl is") != -1:
            sentence["question"] = "What is the girl doing?"
        elif sentence["raw"].find("boy is") != -1:
            sentence["question"] = "What is the boy doing?"
        elif sentence["raw"].find("man is") != -1:
            sentence["question"] = "What is the man doing?"
        elif sentence["raw"].find("woman is") != -1:
            sentence["question"] = "What is the woman doing?"
        elif sentence["raw"].find("people are") != -1:
            sentence["question"] = "What are the people doing?"
        elif sentence["raw"].find("lady is") != -1:
            sentence["question"] = "What is the lady doing?"
        else:
            sentence["question"] = "What is in this image?"

with open('senticap_dataset_with_updated_questions.json', 'w') as file:
    json.dump(senticap_dataset, file)