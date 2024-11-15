==============
SentiSense Affective Lexicon in English WordNet 2.1

This document (October, 2014) is included in the SentiSense Affective Lexicon.

==============
Citation Info

The SentiSense Affective Lexicon was presented in the paper:

Jorge Carrillo-de-Albornoz, Laura Plaza, Pablo Gerv·s. 2012. SentiSense: An easily scalable concept-based affective lexicon for Sentiment Analysis. In proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012).

@inproceedings { 481,
	title = {SentiSense: An easily scalable concept-based affective lexicon for Sentiment Analysis},
	booktitle = {The 8th International Conference on Language Resources and Evaluation (LREC 2012). To appear},
	year = {2012},
	author = {Carrillo-de-Albornoz, Jorge and Plaza, Laura and Gerv√°s, Pablo}
}

Please see the paper for further details.

==============
Data Format

The SentiSense Affective Lexicon consists of 5,496 words and 2,190 synsets from WordNet 2.1 labeled with an emotional category. The main part of the lexicon consists of nouns and adjectives, followed by verbs and a small set of adverbs. SentiSense consists of two data files in XML:

    * The first file, Categories.xml, defines the emotional categories and the antonym relationship between them.
    * The second file, Synsets.xml, contains the WordNet synsets that make up the lexicon. In this file, each entry contains the WordNet synset identifier (SID), its part of speech (POS), its gloss or definition in WordNet and the emotional category assigned to it.

SentiSense has been developed semi-automatically using several semantic relations between synsets in WordNet. SentiSense is endowed with a set of tools that allow users to visualize the lexicon and some statistics about the distribution of synsets and emotions in SentiSense, as well as to easily expand the lexicon. SentiSense is available for research purposes.
==============
