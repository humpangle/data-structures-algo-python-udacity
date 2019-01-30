class Element {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor(head) {
    this.head = head;
  }

  append(el) {
    let current = this.head;

    while (current && current.next) {
      current = current.next;
    }

    current.next = el;
  }

  insert(el, position) {
    if (position < 1) {
      throw new Error("invalid position: " + position);
    }

    if (position === 1) {
      el.next = this.head;
      this.head = el;
      return;
    }

    let current = this.head;
    // let pos = 1

    while (current) {
      const next = current.next;

      if (!next) {
        current.next = el;
        return;
      }

      current = next;
    }
  }
}

module.exports = {
  Element,
  LinkedList
};

function solution1(words) {
  // write your code in JavaScript (Node.js 8.9.4)
  let lb = "";
  let lbc = 0;
  let lbw = "";

  const map = words.reduce((acc, w) => {
    const len = w.length - 1;
    const wo = w[0];
    let count = 0;

    for (let i of w) {
      if (wo === i) {
        ++count;
      } else {
        break;
      }
    }

    const we = w[len];
    let counte = 0;

    for (let index = len; index > -1; index--) {
      let i = w[index];

      if (we === i) {
        ++counte;
      } else {
        break;
      }
    }

    if (counte > lbc) {
      lbc = counte;
      lb = we;
      lbw = w;
    }

    acc[w] = { s: { l: wo, c: count }, e: { l: we, c: counte } };
    return acc;
  }, {});

  console.log(lb, lbc, lbw);

  delete map[lbw];

  function find(map1) {
    const f = Object.entries(map1)
      .filter(([e, x]) => x["s"]["l"] === lb)
      .sort(([e, x]) => x["s"]["c"]);
    return f;
  }

  // console.log(map);
  console.log(...find(map));

  return map;
}

function solution(words) {
  let pos = 2;
  let l = "";

  function check(ws) {}
}

// words = ["aabb", "aaaa", "bbab", "baabbaa"];
// s = solution(words);
// console.log(s);
