#!/usr/bin/env bash
set -e

DOMAIN=$1
CERT_NAME=$2

if [ -z $DOMAIN ]
then
  echo "Please specify a domain"
  exit 1
fi

if [ -z $CERT_NAME ]
then
  echo "Please specify a name for your cert"
  exit 1
fi

CERT_PATH="/etc/letsencrypt/live/${DOMAIN}/"

if [ ! -e $CERT_PATH ]
then
  echo "There seems to be no certificate for that domain"
  exit 1
fi

/home/signal9/bin/doctl compute certificate create \
  --certificate-chain-path "${CERT_PATH}/chain.pem" \
  --private-key-path "${CERT_PATH}/privkey.pem" \
  --leaf-certificate-path "${CERT_PATH}/cert.pem" \
  --name "${CERT_NAME}"
