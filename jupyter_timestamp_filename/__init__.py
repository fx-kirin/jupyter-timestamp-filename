__version__ = '0.1.1'
import re
import datetime


def patched_increment_filename(self, filename, path="", insert=""):
    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    if filename[0:9] == "Untitled.":
        filename = "%s_%s.%s" % (filename[0:8], now_string, filename[9:])
    if insert == "-Copy":
        if re.search(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", filename):
            filename = re.sub(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", "%s-Copy" % (now_string), filename)
        else:
            filename = re.sub(r"\.(\w+)$", r"_%s-Copy.\1" % (now_string), filename)

    return self.__original_increment_filename(filename, path, insert)


def load_jupyter_server_extension(nbapp):
    nbapp.contents_manager.__original_increment_filename = (
        nbapp.contents_manager.increment_filename
    )
    nbapp.contents_manager.__class__.increment_filename = patched_increment_filename
