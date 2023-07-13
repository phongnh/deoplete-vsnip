import json
import re
from deoplete.source.base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'vsnip'
        self.mark = '[v]'
        self.rank = 1000
        self.input_pattern = r'\w\+$'
        self.min_pattern_length = 1
        self.vars = {}

    def gather_candidates(self, context):
        snippets = []
        for item in self.vim.call('vsnip#get_complete_items', context['bufnr']):
            snippets.append({
                'word': item['word'],
                'abbr': item['abbr'],
                'menu': re.sub('^\[.*\]', self.mark, item['menu']),
                'info': "\n".join(json.loads(item['user_data'])['vsnip']['snippet']),
                'dup': item['dup']
            })
        return snippets
