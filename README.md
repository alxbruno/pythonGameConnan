# Development Containers - pythonGameConnan

https://www.youtube.com/watch?v=SDa3v4Quj7Y

https://github.com/devcontainers

https://github.com/devcontainers/templates/tree/main/src/python

### Git
It comes with git. After the container is created and running, go to the terminal and
`git config --global user.email "alexbrunoalves2011@gmail.com" &&  git config --global user.name "aba"` in order to set git config.
This is the git installed inside the container, not in the OS itself `git config --global --list`.

Run `cat /etc/issue` in order to check the container OS (`Debian GNU/Linux 11 \n \l`)

`cd '/vscode/vscode-server/extensionsCache' && ls -t | tail -n +50 | xargs rm -f`

### Libraries installed by default with `mcr.microsoft.com/devcontainers/python:1-3.12-bullseye`
- `which pip`
    - `/usr/local/bin/pip`
    - `pip list`
        ```
        Package    Version
        ---------- -------
        gitdb      4.0.11
        GitPython  3.1.41
        pip        24.0
        setuptools 69.0.3
        smmap      5.0.1
        wheel      0.42.0
        ```

- `which pip3`
    - `/usr/local/bin/pip3`
    - `pip3 list`
        ```
        Package    Version
        ---------- -------
        gitdb      4.0.11
        GitPython  3.1.41
        pip        24.0
        setuptools 69.0.3
        smmap      5.0.1
        wheel      0.42.0
        ```


## [Development Containers - Using Images, Dockerfiles, and Docker Compose](https://containers.dev/guide/dockerfile)

### [Using a Dockerfile](https://containers.dev/guide/dockerfile#docker)
> First, add a file named `Dockerfile` next to your `devcontainer.json` inside the `.devcontainer` folder. For example:

```
Dockerfile
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
# Install the xz-utils package
RUN apt-get update && apt-get install -y xz-utils
```

> Next, remove the image property from `devcontainer.json` (if it exists) and add the build and dockerfile properties instead:
```
"build": {
        // Path is relative to the devcontainer.json file.
        "dockerfile": "Dockerfile"
    }
```

### [Using Docker Compose](https://containers.dev/guide/dockerfile#docker-compos)
> ... to be continued





### Resources
- https://github.com/alxbruno/template-starter

- https://github.com/devcontainers

- https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md

- https://github.com/microsoft/vscode-dev-containers/tree/main/containers

- https://github.com/docker-library/official-images/blob/master/library/python


- [GitHb - microsoft/vscode-dev-containers](https://github.com/microsoft/vscode-dev-containers)
    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

- [Development Containers](https://containers.dev/)