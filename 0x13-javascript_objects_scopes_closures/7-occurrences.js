#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((preVal, currentVal) => currentVal === searchElement ? preVal + 1 : preVal, 0);
};
