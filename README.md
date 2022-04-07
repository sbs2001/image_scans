This repo contains vulnerability scans of various popular docker images.
The results are obtained by periodically running `docker scan <image_name> --json`.

The data can be leveraged to do interesting things. As a start I will be creating a browser extension which quickly gives summary of scan results in hub.docker.com itself.