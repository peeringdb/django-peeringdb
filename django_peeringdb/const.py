
MEDIA = (('Ethernet', 'Ethernet'),
         ('ATM', 'ATM'),
         ('Multiple', 'Multiple'))

POC_ROLES = (
    ('Abuse', 'Abuse'),
    ('Maintenance', 'Maintenance'),
    ('Policy', 'Policy'),
    ('Technical', 'Technical'),
    ('NOC', 'NOC'),
    ('Public Relations', 'Public Relations'),
    ('Sales', 'Sales')
)


POLICY_GENERAL = (('Open', 'Open'),
                  ('Selective', 'Selective'),
                  ('Restrictive', 'Restrictive'),
                  ('No', 'No'))
POLICY_LOCATIONS = (('Not Required', 'Not Required'),
                    ('Preferred', 'Preferred'),
                    ('Required - US', 'Required - US'),
                    ('Required - EU', 'Required - EU'),
                    ('Required - International',
                     'Required - International'))
POLICY_CONTRACTS = (('Not Required', 'Not Required'),
                    ('Private Only', 'Private Only'),
                    ('Required', 'Required'))

PROTOCOLS = (
    ('IPv4', 'IPv4'),
    ('IPv6', 'IPv6'),
)

RATIOS = (
    ('', 'Not Disclosed'),
    ('Not Disclosed', 'Not Disclosed'),
    ('Heavy Outbound', 'Heavy Outbound'),
    ('Mostly Outbound', 'Mostly Outbound'),
    ('Balanced', 'Balanced'),
    ('Mostly Inbound', 'Mostly Inbound'),
    ('Heavy Inbound', 'Heavy Inbound')
)

REGIONS = (('North America', 'North America'),
           ('Asia Pacific', 'Asia Pacific'),
           ('Europe', 'Europe'),
           ('South America', 'South America'),
           ('Africa', 'Africa'),
           ('Australia', 'Australia'),
           ('Middle East', 'Middle East'))

SCOPES = (
    ('', 'Not Disclosed'),
    ('Not Disclosed', 'Not Disclosed'),
    ('Regional', 'Regional'),
    ('North America', 'North America'),
    ('Asia Pacific', 'Asia Pacific'),
    ('Europe', 'Europe'),
    ('South America', 'South America'),
    ('Africa', 'Africa'),
    ('Australia', 'Australia'),
    ('Middle East', 'Middle East'),
    ('Global', 'Global')
)

TRAFFIC = (('', 'Not Disclosed'),
           ('0-20 Mbps', '0-20 Mbps'),
           ('20-100Mbps', '20-100Mbps'),
           ('100-1000Mbps', '100-1000Mbps'),
           ('1-5Gbps', '1-5Gbps'),
           ('5-10Gbps', '5-10Gbps'),
           ('10-20Gbps', '10-20Gbps'),
           ('20-50 Gbps', '20-50 Gbps'),
           ('50-100 Gbps', '50-100 Gbps'),
           ('100+ Gbps', '100+ Gbps'),
           ('100-200 Gbps', '100-200 Gbps'),
           ('200-300 Gbps', '200-300 Gbps'),
           ('300-500 Gbps', '300-500 Gbps'),
           ('500-1000 Gbps', '500-1000 Gbps'),
           ('1 Tbps+', '1 Tbps+'),
           ('10 Tbps+', '10 Tbps+'))

NET_TYPES = (
    ('', 'Not Disclosed'),
    ('Not Disclosed', 'Not Disclosed'),
    ('NSP', 'NSP'),
    ('Content', 'Content'),
    ('Cable/DSL/ISP', 'Cable/DSL/ISP'),
    ('Enterprise', 'Enterprise'),
    ('Educational/Research', 'Educational/Research'),
    ('Non-Profit', 'Non-Profit'),
    ('Route Server', 'Route Server')
)

VISIBILITY = (
    ('Private', 'Private'),
    #                   ('Peers', 'Peers'),
    ('Users', 'Users'),
    ('Public', 'Public'),
)
