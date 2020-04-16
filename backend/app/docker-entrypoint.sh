#!/bin/bash
cd /var/www/app

uwsgi --emperor /etc/uwsgi.d \
      --die-on-term \
      --log-date