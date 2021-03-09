
# django-peeringdb changelog

## [Unreleased]
### Added
- `name_long` field to `Network`
- `aka` field to `InternetExchange`
- `name_long` field to `Facility`
- `aka` field to `Facility`
- `name_long` field to `Organization`
- `aka` field to `Organization`
- github workflow for tests 
### Fixed
### Changed
### Deprecated
### Removed
### Security


## [2.5.0]
### Added
- `suite` and ``floor` fields to `AddressModel`
- better tooltip/help text for phone fields


## [2.4.0]
### Added
- "Government" network type
- "Network Services" network type
- "Route Collector" network type
- django3.1 tests
### Changed
- improve network.info_prefixes4 help text
- improve network.info_prefixes6 help text
### Removed
- django1.11 support (end of life Apr 2020)
- django2.0 support (end of life Apr 2019)
- django2.1 support (end of life Dec 2019)
- python3.5 support (end of life Sep 2020)


## [2.3.0]
### Added
- django3.0 support


## [2.2.0]
### Added
- add `ixf_last_import` to InternetExchangeBase (peeringdb/peeringdb#683)
- add `ixf_net_count` to InternetExchangeBase (peeringdb/peeringdb#683)
- add `ixf_ixp_member_list_url` to IXLanBase (peeringdb/peeringdb#249)
- add `ixf_ixp_member_list_url_visible` to IXLanBase (peeringdb/peeringdb#249)
### Fixed
- fix issue in setup.py for test requirements


## [2.1.1]
### Fixed
- remove verbose_name migrations (#45)


## [2.1.0]
### Added
- add `in_dfz` field to IXLanPrefixBase (peeringdb/peeringdb#352)
### Changed
- Make spelling of traffic levels consistent (peeringdb/peeringdb#519)


## [2.0.0]
### Added
- add py3.7, py3.8 to tox and travis tests
- add django 2.2, 3.0 to tests
### Changed
- Explicitly set TIME_ZONE='UTC' (#38)
### Removed
- remove py2.7 support (#36)
- remove py3.4 tests (py3.4 EOL reched)


## [1.1.0]
### Added
- add `info_never_via_route_servers` to `NetworkBase` (peeringdb/394)
- set help text for irr_as_set, info_prefixes4 and info_prefixes6 (peeringdb/228)
### Fixed
### Changed
### Deprecated
### Removed
### Security


## [1.0.0]
### Added
- Client adaptor to work with the new peeringdb client
- Django 2.0, 2.1 support (thanks @paravoid)
- Improved py3 support (thanks @paravoid)
- #22 - use django gettext on choices

### Removed
- `pdb_sync` command, peeringdb client now implements sync logic


## [0.8.0]
### Added
- Django 1.11 migration

### Fixed
- cleaned up sync
- #17 - skip None deletes on related


## [0.7.0]
### Added
- py3 compatibility


## [0.6.1]
### Fixed
- fixed issue with longitude / latitude validation errors during sync (#10)


## [0.6.0]
### Added
- latitude and longitude fields added to AddressModel


## [0.5.0]
### Added
- support for django 1.10, 1.11


## [0.4.0]
### Added
- --limit option to sync

### Fixed
- use calendar.timegm instead of time.mktime so there isn't timezone skew


## [0.3.1]
### Fixed
- fix sync via call_command


## [0.3.0]
### Added
- Route Server network type
- Maintenance contact type
- standalone URLField
- better testing options


## [0.2.2]
### Added
- CHANGELOG!
- docs for adding XK country code for Kosovo 

### Fixed
- beta URL changed to www
- cascade delete for relational tables
- fixed foreign key related names

### Removed
- poc list tests
