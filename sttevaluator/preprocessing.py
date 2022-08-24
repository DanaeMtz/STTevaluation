import pandas as pd
import re
import spacy
import num2words

def preprocessing(phase: str) -> str:
    # Microsoft 
    transformed_phase = re.sub(r",00", "", phase.lower())  # eliminate the parsing of microsoft for integers 
    # Genesys
    transformed_phase = re.sub(r"euh", "", transformed_phase) 
    # reference 
    transformed_phase = re.sub(r"\Whésitation\W|\Wagent\sdit\sok\W", "", transformed_phase) 
    # [mot]|[agent dit hmh]|[agent dit: d'accord]|[agent dit: mhm]|[rire] to be considered in the computation 
    # Microsoft & Nuance 
    transformed_phase = re.sub(r"\$", " dollars", transformed_phase) # replace $ by the word dollars
    # Microsoft & Nuance & Reference 
    transformed_phase = re.sub(r"(?P<integer>\d+),(?P<decimal>\d+)", "\g<integer>.\g<decimal>", transformed_phase) # replace , by . for numbers
    transformed_phase = re.sub(r"\d+", lambda m: num2words.num2words(m.group(0), lang="fr").replace("-", " "), transformed_phase) # turn numbers into words
    transformed_phase = re.sub(r"(?P<last_int>\w+)\.(?P<first_dec>\w+)", "\g<last_int> et \g<first_dec>",transformed_phase) # replace de . by the word  "et"  
    # all 
    transformed_phase = re.sub(r"[.,]", "", transformed_phase) # similar to r"\.|,"
    transformed_phase = re.sub(r"-|\s+", " ", transformed_phase) # eliminate - for words such as compte-cheques
    return transformed_phase


preprocessing_all = lambda phase: preprocessing(phase)
