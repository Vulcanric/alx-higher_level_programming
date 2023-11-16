#!/usr/bin/node
/* Even more scope */
module.exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
