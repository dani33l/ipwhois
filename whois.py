from ipwhois import IPWhois

obj = IPWhois('74.125.225.229')

res=obj.lookup()

res["nets"][0]['country']
'US'

res["nets"][0]['abuse_emails']
'arin-contact@google.com'

from pprint import pprint

In [43]: pprint(res)
{'asn': '15169',
 'asn_cidr': '74.125.225.0/24',
 'asn_country_code': 'US',
 'asn_date': '2007-03-13',
 'asn_registry': 'arin',
 'nets': [{'abuse_emails': 'arin-contact@google.com',
           'address': '1600 Amphitheatre Parkway',
           'cidr': '74.125.0.0/16',
           'city': 'Mountain View',
           'country': 'US',
           'created': '2007-03-13T00:00:00',
           'description': 'Google Inc.',
           'misc_emails': None,
           'name': 'GOOGLE',
           'postal_code': '94043',
           'state': 'CA',
           'tech_emails': 'arin-contact@google.com',
           'updated': '2012-02-24T00:00:00'}],
 'query': '74.125.225.229',
 'raw': None}
