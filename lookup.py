from flashtext import KeywordProcessor


def init(key_words):
    kw = KeywordProcessor()

    kw.add_keywords_from_list(key_words)

    return kw


def lookup(kw, text):
    sites = kw.extract_keywords(text)
    site=[]
    for i in sites:
        if(len(i)>2):
            site.append(i)
    return site


def get_sites(sites,key_words, web):
    ind = key_words.index(sites[0])
    return web[0][ind]

