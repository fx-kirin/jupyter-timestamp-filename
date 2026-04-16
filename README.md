# jupyter-timestamp-filename

A Jupyter Server extension that adds timestamps to untitled notebook filenames.

## Install

```bash
pip install jupyter-timestamp-filename
jupyter server extension enable --sys-prefix --py jupyter_timestamp_filename
```

## What it does

New untitled notebook:

```text
Untitled_2026-04-16_13-24-55.ipynb
```

Duplicated notebook:

```text
Untitled_2026-04-16_13-24-55-Copy.ipynb
```
