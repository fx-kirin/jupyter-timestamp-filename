## How to use

Add this file to your IPython library directory like `site-packages/IPython/extensions`.

And modify `~/.jupyter/jupyter_notebook_config.json` file like below.

```json:jupyter_notebook_config.json
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyter_nbextensions_configurator": true,
      "add_timestamp_to_filename":true
    }
  }
}
```

## What it looks like.

```
# Initial File Name
Untitled_2020-01-12_23:54:44.ipynb

# Copied File Name
Untitled_2020-01-12_23:54:52-Copy.ipynb
```
