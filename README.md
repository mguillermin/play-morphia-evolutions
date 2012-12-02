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
	        artifact: http://cloud.github.com/downloads/cleverage/play-morphia-evolutions/[module]-[revision].zip
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
	
You can then check your database state using the `morphiaevolutions` command:

	$ play morphiaevolutions
	~        _            _ 
	~  _ __ | | __ _ _  _| |
	~ | '_ \| |/ _' | || |_|
	~ |  __/|_|\____|\__ (_)
	~ |_|            |__/   
	~
	~ play! 1.2.5, http://www.playframework.org
	~
	~ Application revision is 1 [432895f] and Database revision is 0 [da39a3e]
	~
	~ Your database needs evolutions!
	
	# ------------------------------------------------------------------------------
	
	// --- Rev:1,Ups - 432895f
	
	  db.foo.insert({a: 1})
	
	# ------------------------------------------------------------------------------
	
	~ Run `play morphiaevolutions:apply` to automatically apply this script to the database
	~ or apply it yourself and mark it done using `play morphiaevolutions:markApplied`
	~
	
In dev mode, if you launch your app using `play run` you will see this in your browser.

The other command `apply`, `markApplied`, `resolve` works as their standard Play evolutions equivalents. see [Play evolutions documentation](http://www.playframework.org/documentation/1.2.5/evolutions).
