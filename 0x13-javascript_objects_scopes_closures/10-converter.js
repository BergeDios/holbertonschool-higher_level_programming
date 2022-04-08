#!/usr/bin/node
exports.converter = function (base) {
  return function (numtoconvert) {
    return (numtoconvert.toString(base));
  };
};
