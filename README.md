[CORE Website](https://coreatcu.com)
====================================

The website for the Columbia Organization of Rising Entrepreneurs.

## Local Setup

Run the following commands:

```bash
#! /bin/bash
virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt
```

## Deployment

To update the live website to the latest version from GitHub:

```bash
ssh core@159.65.191.95                 # Ask website maintainers for password.
cd app
git pull                               # Pull latest changes from this repo.

# Optional, but HIGHLY RECOMMENDED TO AVOID SERIOUS HEADACHES
ufw allow 5000                         # Enable port 5000.
source <path-to-virtualenv>            # Activate virtual environment.
gunicorn --bind 0.0.0.0:5000 wsgi:app  # Test the app on port 5000.
ufw delete allow 5000

sudo systemctl restart app.service     # Restart systemd unit file.
```

## Material Design vs. Bootstrap

We're experimenting with Google's [Material Design](http://www.getmdl.io/index.html) library. This website uses a different global font scheme and color scheme from the default files in the Material Design Lite library. These changes are made to the `src/_variables.scss` file in the Material Design Lite [source code](https://github.com/google/material-design-lite).
