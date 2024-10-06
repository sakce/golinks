# lightweight golinks

incredibly lightweight golinks implementation that relies on using a Chromium-based browser and an API that redirects traffic to pre-configured [*golinks*](https://golinks.github.io/golinks/). Inspired by [Ian Fisher](https://iafisher.com/blog/2020/10/golinks).

Much more to come:
- a more appropriate Control Panel
- better deployment
- simplified addition of new golinks (mb `/go/add/this/new/nested/shortcut`?)
- visualizing nested golinks properly
- storing the golinks data someplace cosy (not a JSON file..)
- add usage tracking (pipe this data to a realtime dash?)

## Usage

Make sure Poetry is installed.

1. Set up the Chrome Extension that will redirect all your requests to `go/{*}` to the lightweight FastAPI by navigating to Chrome Extensions (`chrome://extensions`), enabling `Developer mode`, and then `Load unpacked` selecting the [`chrome-extension`](./chrome-extension/) directory of this repository.

2. Run the FastAPI application locally.
```sh
poetry install
poetry run fastapi dev src/app.py
```

3. In your browser, navigate to the Control Plane by searching for `go/cp` in your browser, and add your golinks.
4. Search for one of your golinks! ☑️
