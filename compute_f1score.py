from sttevaluator.preprocessing import preprocessing_all
from sttevaluator.tokenization import tokenize_all, clean_genesys_tokens
from sttevaluator.f1score import pseudo_recall, pseudo_precision, f1_score
from sttevaluator.wer import compute_wer

import pandas as pd


def main():
    df = pd.read_csv("data/transcripts_new.csv", encoding="utf-8")
    #df = df.iloc[:61, :]  # numbers only
    df = df.iloc[61:, :]  # general corpus

    nuance = df.loc[:, "nuance"].tolist()
    genesys = df.loc[:, "genesys"].tolist()
    reference = df.loc[:, "reference"].tolist()
    microsoft = df.loc[:, "microsoft"].tolist()
    file_id = df.loc[:, "file_id"].tolist()

    referen_clean = list(map(preprocessing_all, reference))
    nuance_clean = list(map(preprocessing_all, nuance))
    genesys_clean = list(map(preprocessing_all, genesys))
    microsoft_clean = list(map(preprocessing_all, microsoft))

    # tokenization
    referen_tokens = list(map(tokenize_all, referen_clean))
    nuance_tokens = list(map(tokenize_all, nuance_clean))
    genesys_tokens = clean_genesys_tokens(list(map(tokenize_all, genesys_clean)))
    microsoft_tokens = list(map(tokenize_all, microsoft_clean))

    # compute precision and recall

    with open("data/bank_entities.txt", encoding="utf-8") as f:
        bank_entities = [line.rstrip() for line in f]

    # with open("data/number_entities.txt", encoding="utf-8") as f:
    #     number_entities = [line.rstrip() for line in f]

    entities = bank_entities

    recall_nuance = pseudo_recall(referen_tokens, nuance_tokens, entities)
    recall_genesys = pseudo_recall(referen_tokens, genesys_tokens, entities)
    recall_microsoft = pseudo_recall(referen_tokens, microsoft_tokens, entities)

    df["entities_in_reference"] = recall_nuance[3]
    df["recall_nuance"] = recall_nuance[4]
    df["recall_genesys"] = recall_genesys[4]
    df["recall_microsoft"] = recall_microsoft[4]

    precision_nuance = pseudo_precision(referen_tokens, nuance_tokens, entities)
    precision_genesys = pseudo_precision(referen_tokens, genesys_tokens, entities)
    precision_microsoft = pseudo_precision(referen_tokens, microsoft_tokens, entities)

    df["precision_nuance"] = precision_nuance[4]
    df["precision_genesys"] = precision_nuance[4]
    df["precision_microsoft"] = precision_microsoft[4]

    f1_score_nuance = f1_score(precision_nuance[5], recall_nuance[5])
    f1_score_genesys = f1_score(precision_genesys[5], recall_genesys[5])
    f1_score_microsoft = f1_score(precision_microsoft[5], recall_microsoft[5])

    df = df.reindex(
        columns=[
            "file_id",
            "reference",
            "entities_in_reference",
            "nuance",
            "recall_nuance",
            "precision_nuance",
            "genesys",
            "recall_genesys",
            "precision_genesys",
            "microsoft",
            "recall_microsoft",
            "precision_microsoft",
        ]
    )

    df.to_excel("results/f1_score_banking_corpusgen.xlsx", index=False, encoding="utf-8")


if __name__ == "__main__":
    main()
