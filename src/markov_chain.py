# MIT License
# Copyright (c) 2024 rUv
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import markovify
import spacy

# Load the English tokenizer, tagger, parser, NER and word vectors from the spacy library
nlp = spacy.load("en_core_web_sm")

class POSifiedText(markovify.Text):
    """
    A class that extends markovify.Text to use spacy's POS tagging,
    allowing for more coherent generated sentences based on parts of speech.
    """
    def word_split(self, sentence):
        """
        Overrides the word_split method to include POS tags with each word.
        
        :param sentence: A string representing the sentence to be split.
        :return: A list of strings, each containing a word and its POS tag.
        """
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        """
        Overrides the word_join method to reconstruct a sentence from words and their POS tags.
        
        :param words: A list of strings, each containing a word and its POS tag.
        :return: A string representing the reconstructed sentence.
        """
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

def generate_markov_text(corpus_path, state_size=2):
    """
    Generates a sentence using Markov chains with optional POS tagging for coherence.
    
    :param corpus_path: Path to the text corpus file.
    :param state_size: The state size for the Markov model. Default is 2.
    :return: A string representing the generated sentence.
    """
    with open(corpus_path) as f:
        text = f.read()
    text_model = POSifiedText(text, state_size=state_size)
    return text_model.make_sentence()
