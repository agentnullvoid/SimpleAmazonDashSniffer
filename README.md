# Simple Amazon Dash Sniffer

This is a simple Amazon Dash Button sniffer that makes sure ARP messages were
received 60 seconds between each other to avoid firing duplicate events.

## Docker Version

To use the Docker version, just build and run the image via:

```
> docker build -t $YOUR_TAG .
> docker run $YOUR_TAG
```

You can follow the logs by doing:

`> docker logs -f $CONTAINER_ID`
