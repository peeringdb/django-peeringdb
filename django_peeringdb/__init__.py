import pkg_resources

__version__ = pkg_resources.require("django_peeringdb")[0].version
