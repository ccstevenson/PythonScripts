class NeedleStack(object):
    def __init__(self,url,max_level=3):
        self.url = url
        self.max_level = max_level        
        self.index, self.graph, self.ranks = dict(), dict(), dict()
        self.index, self.graph = self.crawl()
        self.ranks = self.compute_ranks()
     
    @staticmethod   
    def get_page(link):
        import urllib
        try:
            html = urllib.urlopen(link).read()
            return html
        except:
            return ""
        
    @staticmethod
    def get_all_links(html):       
        import re
        urls = re.findall(r' *href *= *[\'"]? *([^\'"> ]+)', html) 
        urls = {link for link in urls if link[0:7] == 'http://'}
        return urls
    
    def crawl(self):
        import re
        pagesToVisit, searched, depth = set([self.url]), set(), 0
        
        while depth <= self.max_level and len(pagesToVisit) != 0:
            for link in pagesToVisit:
                self.graph[link] = NeedleStack.get_all_links(NeedleStack.get_page(link))
                searched.update([link])
                text = re.split('<.*?>', NeedleStack.get_page(link)) # Doesn't allow for compound words (apostrophes not allowed per specifications) and doesn't parse out HTML character entities (not mentioned in specifications, included for simplicity).
                text = (''.join(text)).lower()
                text = re.findall(r'\w+', text)
                for word in text:
                    if word in self.index.keys():
                        self.index[word].update([link])
                    else:
                        self.index[word] = set([link])               
            pagesToVisit = set(page for page in self.graph[link] for link in pagesToVisit if page not in searched)
            depth += 1
        return self.index, self.graph
    
    def compute_ranks(self):       
        d = 0.85 # probability that surfer will bail
        numloops = 10
        
        ranks = {}
        npages = len(self.graph)
        for page in self.graph:
            ranks[page] = 1.0 / npages
            
        for i in range(0, numloops):
            newranks = {}
            for page in self.graph:
                newrank = (1 - d) / npages
                for url in self.graph:
                    if page in self.graph[url]: # this url links to "page"
                        newrank += d*ranks[url]/len(self.graph[url])
                newranks[page] = newrank
            ranks = newranks
        return ranks
    
    def lookup(self, keyword):
        if keyword in self.index.keys():
            sites = dict()
            for site in self.index[keyword]:
                sites[site] = 0
            for site in sites:
                for key, rank in self.ranks.items():
                    if site == key:
                        sites[site] = rank
            import operator    
            sites = sorted(sites.iteritems(), key=operator.itemgetter(1), reverse=True)
            sites = [site[0] for site in sites]
            return sites             
        else:
            print "That word was not found on any pages."