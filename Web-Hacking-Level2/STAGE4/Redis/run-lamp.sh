#!/bin/bash

redis-server &
&>/dev/null /usr/sbin/apachectl -DFOREGROUND -k start