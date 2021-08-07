try:
    import importlib.metadata as importlib_metadata
# python < 3.8
except ImportError:
    import importlib_metadata


__version__ = importlib_metadata.version(__name__)
