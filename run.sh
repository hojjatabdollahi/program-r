#!/bin/bash

# Run programr majordomo client
# python ./src/programr/clients/events/majordomo/client.py --config ./bots/ryan/config.yaml --cformat yaml --logging ./bots/ryan/logging.yaml

# Run programr flask client
python ./src/programr/clients/restful/flask/client.py --config ./bots/ryan/config.yaml --cformat yaml --logging ./bots/ryan/logging.yaml