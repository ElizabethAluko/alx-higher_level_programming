#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    const completedTasksByUser = tasks.reduce((result, task) => {
      if (task.completed) {
        if (result.hasOwnProperty(task.userId)) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
      return result;
    }, {});

    console.log(completedTasksByUser);
  } else {
    console.error(`Failed to fetch tasks. Error: ${error}`);
  }
});
