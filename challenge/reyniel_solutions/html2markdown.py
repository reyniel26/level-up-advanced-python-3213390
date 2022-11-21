import re

# Im trying to solve it without re, but i cant for urls Hahahah
URLS = re.compile(r'<a href="(.+?)">(.+?)</a>')

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    italics = ['<em>', '</em>']
    paragraphs = ['</p>', '<p>']

    markdown = html

    for italic in italics:
        markdown = markdown.replace(italic, '*')

    markdown = " ".join([word.strip() for word in markdown.split()])

    markdown = markdown.replace("".join(paragraphs), "\n\n")

    for paragraph in paragraphs:
        markdown = markdown.replace(paragraph, '')

    markdown = URLS.sub(r'[\2](\1)', markdown)

    return markdown

