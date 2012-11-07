# Play Morphia Evolutions

## Overview
This module is an adaptation of the native Play 1.2 Evolutions for Morphia.

It allows to manage evolution scripts (with "up" and "down" statements) and automatically checks if your database is up-to-date regarding this evolutions. If it is not the case, scripts can be applied :

- from the browser in dev mode
- via a dedicated command in prod mode

## Installation

Add the dependency for this module in your application `conf/dependencies.yml`

	require:
	    - play
	    - play -> morphia 1.2.9
	    - morphiaevolutions -> morphiaevolutions 0.1
	
	repositories:
	    - morphiaevolutions:
	        type: http
	        artifact: http://mguillermin.github.com/play-morphia-evolutions/releases/[module]-[revision].zip
	        containts:
	            - morphiaevolutions -> *
  
Then retrieve the module using

	play deps --sync

By default, evolutions are enabled in the plugin. If you want to disable evolutions, you can update your `conf/application.conf` :

	morphia.evolutions.enabled=false
	
## Usage

Once the module is installed, you can create evolution scripts in the directory `db/evolutions`

Evolution scripts should be name `1.js`, `2.js`,… in the order you want your evolutions to be applied.

The syntax of these scripts is quite similar to the standard Play evolution scripts syntax. Ex : 

	// Initializing Foo data
	// --- !Ups
	
	db.foo.insert({a: 1})
	
	// --- !Downs
	
	db.foo.remove({a: 1})	
	
if you create
	