#!/bin/bash
#display all HTTP methods
curl -sI $1 | grep Allow | cut -c 8-
