#!/usr/bin/node
const req = require('request');

const url = process.argv[2];
req(url, function (err, res, data) {
  if (err == null) {
    const allTodos = JSON.parse(data);
    const completedTodos = {};
    allTodos.forEach((todo) => {
      if (todo.completed && completedTodos[todo.userId] === undefined) {
        completedTodos[todo.userId] = 1;
      } else if (todo.completed) {
        completedTodos[todo.userId] += 1;
      }
    });
    console.log(completedTodos);
  }
});
