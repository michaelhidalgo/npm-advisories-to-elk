import requests,json
from Elastic_Search import ElasticSearch

# hack to fetch all the advisories in JSON format
NPM_ADVISORIES_URL = 'https://www.npmjs.com/advisories?page=0&perPage=100000'

# fetch NPM Security advisories from https://www.npmjs.com/advisories
def get_npm_advisors():
    r = requests.get(NPM_ADVISORIES_URL, headers={'X-Spiferack': '1'})
    return r.json()

# parses NPM security advisories and import them into Elastic
def import_npm_advisories_to_elk():
    print('Parsing and loading npm advisories')
    advisories          = get_npm_advisors()['advisoriesData']['objects']
    advisories_length   = len(advisories)
    print(f'Parsing {advisories_length} NPM advisories')
    advisory_index  = ElasticSearch('npm-advisories').delete_index().create_index()
    advisory_index.add_bulk(advisories, "advisories")
    print('NPM advisores imported into ELK')

import_npm_advisories_to_elk()