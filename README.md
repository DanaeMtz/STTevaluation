This set of functions have been created in order to evaluate and compare speech-to-text engines attached to different conversational AI solutions. The metrics to be considered are described below. 

## Word Error Rate (WER)

Is a common metric for measuring speech-to-text accuracy of automatic speech recognition (ASR) systems. It is computed as the number of errors divided by the total number of words.

Word Error Rate = (Substitutions + Insertions + Deletions) / Number of Words Spoken in the reference transcript 

Where errors are:

- Substitution: when a word is replaced (for example, “shipping” is transcribed as “sipping”)
- Insertion: when a word that wasn't said is added (for example, “hostess” is transcribed as “host is”)
- Deletion: when a word is omitted from the transcript (for example, “get it done” is transcribed as “get done”)

## Entity evaluation

We seek to evaluate the ability of STT engines to correctly identify a certain set of entities. When making this evaluation, there are two different types of errors that can occur:

- The entity is in the reference, but it was missed by the system (mistranscribed or omitted).
- The entity appears incorrectly in the transcription.

In order to evaluate these two types of errors, we will consider the following performance measures:

- **Recall**: % of entities in the reference that were correctly transcribed.           
1- (number of entities in the transcript that were incorrectly transcribed or omitted/total number of entities in the reference)

- **Precision**: % of entities in the transcript that are in the reference.
1 - (number of erroneously added entities in the transcript / total number of entities in the transcript)

- **F1-score**: harmonic mean that combines precision and recall. Gives a measure of overall performance.
2( Precision x Recall / Precision + Recall )

The entities considered in this exercise are:

- Words that represent numbers: \{ zéro, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize, quatorze, quinze, seize, dix, vingt, trente, quarante, cinquante, soixante, cent, mille. \}
- Words specific to the banking industry: \{ celi, cri, reer, cpg, ferr, natgo, nip, reee, bni, rap, bnc. \}

### Results 

### Corpus 61, focus on numeric entities

| Engin     | Recall  | Precision | F1-score |
|-----------|---------|-----------|----------|
| Nuance    | 0.982   |  0.986    | 0.984    |
| Genesys   | 0.976   |  0.979    | 0.977    |
| Microsoft | 0.986   |  0.993    | 0.990    |

See the f1_score_numbers.xlsx file for details. 


### Corpus 670, focus on numeric entities

| Engin     | Recall | Precision | F1-score |
|-----------|--------|-----------|----------|
| Nuance    | 0.925  |  0.905    | 0.915    |
| Genesys   | 0.907  |  0.916    | 0.911    |
| Microsoft | 0.927  |  0.939    | 0.933    |

See the f1_score_numbers_corpusgen.xlsx file for details. 



### Overall performance on Corpus 670

| Engin    | WER (without lemmatization) |
|----------|-------|
| Nuance   | 0.088 |
| Genesys  | 0.142 |
| Microsoft| 0.075 |


### Corpus 670, focus on banking terms

| Engin     | Recall  | Precision | F1-score |
|-----------|---------|-----------|----------|
| Nuance    | 0.982   |  0.986    | 0.984    |
| Genesys   | 0.976   |  0.979    | 0.977    |
| Microsoft | 0.986   |  0.993    | 0.990    |

See the f1_score_banking_corpusgen.xlsx file for details. 


#### Examples of common mistakes 

| Engin      | Transcript Reference| Transcript Nuance | Transcript Genesys | Transcript Microsoft |
|------------|---------------------|-------------------|--------------------|----------------------|
| Reference  | compte d'épargne    | compte **départ** | **car départ**     | compte d'épargne     |    
|            | compte CELI         | compte CELI       | compte **celui**   | compte **celui**     |
|            | à mon compte REER   | à mon compte REER | **ramon contraire**| à mon compte **aéré**|
|            | mon CELI            | mon CELI          | mon **cédit**      | mon **CI**           |
|            | CELI                | **merci**         | **c'est lit**      | **ces lits**         |
|            | céduler             | **c'est Jul**     | cédule             | **c'est du lait**    | 
