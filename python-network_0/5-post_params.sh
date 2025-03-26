#!/bin/bash
#send a POST request to the passed UR and display response
curl -sb -X POST --data "email=test@gmail.com&subject=I will always be here for PLD" $1
