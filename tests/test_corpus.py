# -*- coding: utf-8 -*-

import unittest

from nltk.corpus import wordnet as wn
from pythainlp.corpus import (
    conceptnet,
    countries,
    download,
    get_corpus_db_detail,
    provinces,
    remove,
    thai_female_names,
    thai_male_names,
    thai_negations,
    thai_stopwords,
    thai_syllables,
    thai_words,
    tnc,
    ttc,
    wordnet,
)


class TestCorpusPackage(unittest.TestCase):
    def test_conceptnet(self):
        self.assertIsNotNone(conceptnet.edges("รัก"))

    def test_corpus(self):
        self.assertTrue(isinstance(thai_negations(), frozenset))
        self.assertTrue(isinstance(thai_stopwords(), frozenset))
        self.assertTrue(isinstance(thai_syllables(), frozenset))
        self.assertTrue(isinstance(thai_words(), frozenset))

        self.assertTrue(isinstance(countries(), frozenset))
        self.assertTrue(isinstance(provinces(), frozenset))
        self.assertTrue(isinstance(thai_female_names(), frozenset))
        self.assertTrue(isinstance(thai_male_names(), frozenset))

        self.assertEqual(
            get_corpus_db_detail("XXX"), {}
        )  # corpus does not exist
        self.assertTrue(download("test"))  # download the first time
        self.assertTrue(download(name="test", force=True))  # force download
        self.assertTrue(download(name="test"))  # try download existing
        self.assertFalse(
            download(name="test", url="wrongurl")
        )  # URL not exist
        self.assertFalse(
            download(name="XxxXXxxx817d37sf")
        )  # corpus name not exist
        self.assertIsNotNone(get_corpus_db_detail("test"))  # corpus exists
        self.assertTrue(remove("test"))  # remove existing
        self.assertFalse(remove("test"))  # remove non-existing

    def test_tnc(self):
        self.assertIsNotNone(tnc.word_freqs())

    def test_ttc(self):
        self.assertIsNotNone(ttc.word_freqs())

    def test_wordnet(self):
        self.assertTrue(isinstance(wordnet.langs(), list))
        self.assertTrue("tha" in wordnet.langs())

        self.assertEqual(
            wordnet.synset("spy.n.01").lemma_names("tha"), ["สปาย", "สายลับ"]
        )
        self.assertIsNotNone(wordnet.synsets("นก"))
        self.assertIsNotNone(wordnet.all_synsets(pos=wn.ADJ))

        self.assertIsNotNone(wordnet.lemmas("นก"))
        self.assertIsNotNone(wordnet.all_lemma_names(pos=wn.ADV))
        self.assertIsNotNone(wordnet.lemma("cat.n.01.cat"))

        self.assertEqual(wordnet.morphy("dogs"), "dog")

        bird = wordnet.synset("bird.n.01")
        mouse = wordnet.synset("mouse.n.01")
        self.assertEqual(
            wordnet.path_similarity(bird, mouse), bird.path_similarity(mouse)
        )
        self.assertEqual(
            wordnet.wup_similarity(bird, mouse), bird.wup_similarity(mouse)
        )
        self.assertEqual(
            wordnet.lch_similarity(bird, mouse), bird.lch_similarity(mouse)
        )

        cat_key = wordnet.synsets("แมว")[0].lemmas()[0].key()
        self.assertIsNotNone(wordnet.lemma_from_key(cat_key))
