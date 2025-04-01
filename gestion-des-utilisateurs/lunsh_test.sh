#!/bin/bash

hurl --no-output test_api_bon.hurl

hurl --no-output test_api_vide.hurl

hurl --no-output test_api_errors.hurl

# docker-compose down && docker-compose up -d --build