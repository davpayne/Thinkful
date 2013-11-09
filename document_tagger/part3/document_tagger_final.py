# Extracts metadata and word counts from texts
import re
import sys
import os

def open_files(directory):
    """ Iterates over all .txt files in the directory and opens them.
        Returns a list with the text of each file """
    documents = []
    for fl in (os.listdir(directory)):
        if fl.endswith('.txt'):
            fl_path = os.path.join(directory, fl)
            with open(fl_path, 'r') as f:
                full_text = f.read()
                documents.append(full_text)
    return documents

def keywords_rege(keywords):
    """ Compiles a list of the keyword searches to be made """
    searches = {}
    for kw in keywords:
      searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
    return searches

def meta_extract(doc):
    """ Extracts and prints the metadata from the document - title, author, translator,
        and illustrator. """
    title_search = re.compile(r'(title:\s*)(?P<title>.*(\n *\w.*)*)(\nauthor:)', re.IGNORECASE)
    author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
    illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
    title = re.search(title_search, doc).group('title')
    author = re.search(author_search, doc)
    translator = re.search(translator_search, doc)
    illustrator = re.search(illustrator_search, doc)
    if author: 
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')
    print "Title: {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}\n".format(illustrator)
    # return title, author, illustrator, translator

def keyword_count(searches, doc):
    """ Takes a set of search terms and prints the count of each word in the 
        document """
    for search in searches:
        print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))

def main():
    directory = sys.argv[1]

    # Checks whether keywords were provided at run time. If not, prompts for them
    if sys.argv[2:]:
        keywords = sys.argv[2:]
    else:
        # Catches any break between words: spaces or commas can be used
        kw_search = re.compile(r'(?:\W*)', re.IGNORECASE)
        words = raw_input("Please provide keywords to count: ")
        keywords = re.split(kw_search, words)
    
    documents = open_files(directory)
    searches = keywords_rege(keywords)

    # Iterates over all read documents
    for i, doc in enumerate(documents):
        print "***" * 25
        print "Here's the info for doc {}:".format(i)
        meta_extract(doc)
        print "Here's the keyword info for doc {}:".format(i)
        keyword_count(searches, doc)

if __name__ == '__main__':
    main()
 