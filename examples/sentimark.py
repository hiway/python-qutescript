#!/usr/bin/env python
# coding=utf-8
import dominate
from dominate.tags import *
from newspaper import Article
from textblob import TextBlob

from qutescript import userscript

polarity_map = {
    8: 'green',
    5: 'olive',
    2: '#333',
    0: '#777',
    -2: 'orange',
    -5: 'red',
    -8: 'brown',
}


def get_polarity_color(polarity):
    for thresh in reversed(sorted(polarity_map.keys())):
        if (polarity * 10) >= thresh:
            return polarity_map[thresh]
    else:
        return '#777'


def generate_html(paragraphs, title_text):
    doc = dominate.document(title='Summary: {}'.format(title_text))

    with doc.head:
        style("""\
            body {
                background-color: #F9F8F1;
                color: #2C232A;
                font-family: sans-serif;
                font-size: 1.2em;
            }

        """)

    with doc:
        div(id='header').add(h1(title_text))
        with div():
            attr(cls='body')
            for para in paragraphs:
                tb = TextBlob(para)
                with p():
                    for sentence in tb.sentences:
                        span(sentence, style="color: {}".format(get_polarity_color(sentence.polarity)))
    return doc


@userscript
def sentiment_markup(request):
    article = Article(request.url)
    # article.download(request.html, request.title)
    article.download()
    article.parse()
    html = generate_html(article.text.split('\n\n'), article.title).render()
    request.send_html(html)


if __name__ == '__main__':
    sentiment_markup()
