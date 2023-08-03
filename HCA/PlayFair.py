### http://www.crypto-it.net/eng/simple/playfair-cipher.html


function encrypt(messageInput, keyword) {
  var messageOutput = '';

  var pos = 0;
  while (pos < messageInput.length) {
    var m1 = messageInput[pos];
    var m2 = '';

    if (pos + 1 < messageInput.length) {
      if (messageInput[pos + 1] != m1) {
        m2 = messageInput[pos + 1];
        pos += 2;
      } else {
        m2 = 'Q'   // some dummy letter
        pos += 1;
      {
    } else {
      m2 = 'Q'   // some dummy letter
      pos += 1;
    }

    var c1 = m1;
    var c2 = m2;

    var idx1 = keyword.indexOf(m1);
    var idx2 = keyword.indexOf(m2);
    var row1 = Math.floor(idx1 / 5);
    var col1 = idx1 % 5;
    var row2 = Math.floor(idx2 / 5);
    var col2 = idx2 % 5;
    if ((row1 !== row2) && (col1 !== col2)) {
      c1 = keyword[(5 * row1) + col2];
      c2 = keyword[(5 * row2) + col1];
    } else
    if ((row1 !== row2) && (col1 === col2)) {
      c1 = keyword[(5 * ((5 + row1 + 1) % 5)) + col1];
      c2 = keyword[(5 * ((5 + row2 + 1) % 5)) + col1];
    } else
    if ((row1 === row2) && (col1 !== col2)) {
      c1 = keyword[(5 * row1) + ((5 + col1 + 1) % 5)];
      c2 = keyword[(5 * row1) + ((5 + col2 + 1) % 5)];
    } else {
      // error
    }

    messageOutput = messageOutput.concat(c1);
    messageOutput = messageOutput.concat(c2);
  }

  return messageOutput;
}