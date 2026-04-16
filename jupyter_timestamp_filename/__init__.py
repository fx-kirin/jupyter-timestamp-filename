import datetime
import re

__version__ = "0.2.0"


def _jupyter_server_extension_points():
    return [{"module": "jupyter_timestamp_filename"}]


def patched_increment_filename(self, filename, path="", insert=""):
    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d_%H-%M-%S")

    if filename.startswith("Untitled."):
        filename = f"{filename[:8]}_{now_string}.{filename[9:]}"

    if insert == "-Copy":
        if re.search(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", filename):
            filename = re.sub(
                r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}",
                f"{now_string}-Copy",
                filename,
            )
        else:
            filename = re.sub(r"\.(\w+)$", rf"_{now_string}-Copy.\1", filename)

    return self.__original_increment_filename(filename, path, insert)


def _load_jupyter_server_extension(serverapp):
    cm = serverapp.contents_manager

    if not hasattr(cm, "__original_increment_filename"):
        cm.__original_increment_filename = cm.increment_filename

    cm.__class__.increment_filename = patched_increment_filename

    serverapp.log.info("jupyter_timestamp_filename loaded")


# backward compatibility
load_jupyter_server_extension = _load_jupyter_server_extension
