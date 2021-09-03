import os


def filename_append(filename: str, text: str) -> str:
    """Appends text after filename, before extension."""
    name, ext = os.path.splitext(filename)
    return "{name}{text}{ext}".format(name=name, text=text, ext=ext)
