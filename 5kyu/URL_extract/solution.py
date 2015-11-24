import re
def domain_name(url):
    return re.search('(//|\.)([a-z]+)', url).groups()[1]
