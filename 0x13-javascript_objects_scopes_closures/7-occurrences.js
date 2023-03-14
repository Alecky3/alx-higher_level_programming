#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, elem) => elem === searchElement ? count + 1 : count, 0);
};
