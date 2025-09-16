try:
    from importlib import metadata

    __version__ = metadata.version(__name__)
# python < 3.8
except ImportError:
    import importlib_metadata

    __version__ = importlib_metadata.version(__name__)
