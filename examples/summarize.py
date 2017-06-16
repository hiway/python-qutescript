# coding=utf-8
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import dominate
from ftfy import fix_text
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from dominate.tags import *

from qutescript import userscript

LANGUAGE = "english"
SENTENCES_COUNT = 10


def generate_html(sentences, title_text):
    doc = dominate.document(title='Summary')

    with doc.head:
        style("""\
            body {
                background-color: #F9F8F1;
                color: #2C232A;
                font-family: sans-serif;
                font-size: 2.6em;
                margin: 3em 1em;
            }
            
        """)

    with doc:
        div(id='header').add(h1(title_text))
        with div():
            attr(cls='body')
            for sentence in sentences:
                p(sentence)

    return doc


@userscript
def summarize_text(request):
    if request.html:
        parser = HtmlParser.from_file(file_path=request.html,
                                      url=request.url,
                                      tokenizer=Tokenizer(LANGUAGE))
    else:
        parser = PlaintextParser.from_file(file_path=request.html,
                                           tokenizer=Tokenizer(LANGUAGE))

    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    sentences = [fix_text(str(s)) for s in summarizer(parser.document, SENTENCES_COUNT)]
    html = generate_html(sentences, fix_text(request.title)).render()
    request.send_html(html)


if __name__ == "__main__":
    summarize_text()
