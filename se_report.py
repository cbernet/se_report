import xml.etree.ElementTree as ET

import pprint
import re 

class SEReport(object):
    
    def __init__(self, path):
        self.root = None
        self.entries = None
        self.userpattern = re.compile('user/([^/]+)')
        self._parse(path)
        
    def _parse(self, path):
        print 'parsing xml...'
        tree = ET.parse(path)
        self.root = tree.getroot()
        self.entries = []
        print 'translating data structure...'
        for i, entry in enumerate(self.root.iter('entry')):
            if i % 10000 == 0:
                print 'entries processed', i
            entry_dict = dict()         
            name = entry.attrib['name']
            m = self.userpattern.search(name)
            user = m.group(1)
            keys = ['size', 'ctime', 'atime', 'mtime']
            for child in entry:
                if child.tag in keys:
                    entry_dict[child.tag] = int(child.text)
            self.entries.append((user,
                                 entry_dict['size'],
                                 name,
                                 entry_dict['ctime'],
                                 entry_dict['mtime'],
                                 entry_dict['atime']))
        
    def print_entries(self, nentries=100, *args, **kwargs):
        for entry in sorted(self.entries, *args, **kwargs):
            print entry
        
        
