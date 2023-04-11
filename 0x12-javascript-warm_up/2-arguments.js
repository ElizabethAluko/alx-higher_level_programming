#!/usr/bin/node

import { argv } from 'node:process';

if (!argv[2]) {
	console.log('No argument');
}; else {
	if (argv[3]) {
		console.log('Arguments found');
	}; else {
		console.log('Argument found');
	};
};
