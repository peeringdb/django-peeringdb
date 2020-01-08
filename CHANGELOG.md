
# django-peeringdb changelog

## [Unreleased]
### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security


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
