#!/bin/bash
cd /var/www/app/pokemon_manager

uwsgi --emperor /etc/uwsgi.d \
      --die-on-term \
      --log-date