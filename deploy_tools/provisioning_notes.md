Provisioning a new site
=======================

## Required packages:

*nginx
*Python 3
*GIT
*pip
*virtualenv

e.g.,, on Ubuntu:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host Config

*see nginx.template.conf
*replace SITENAME with e.g. , staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
*replace SITENAME with e.g., stagign.my-domain.com

## Folder Structure
/home/username
|______sites
       |_____SITENAME
       		|---  database
		|---  source
		|---  static
		|---  virtualenv

