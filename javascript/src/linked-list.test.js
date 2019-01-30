const { Element, LinkedList } = require("./linked-list");

function make(value) {
  return new Element(value);
}

test("all", () => {
  let l1 = new LinkedList(make(1));
  expect(l1.head.value).toBe(1);

  expect(() => l1.insert(make(2), 0)).toThrow(/invalid/i);

  l1 = new LinkedList(make(1));
  l1.append(make(2));
  expect(l1.head.value).toBe(1);
  expect(l1.head.next.value).toBe(2);

  l1 = new LinkedList(make(1));
  l1.insert(make(2), 1);
  expect(l1.head.value).toBe(2);
  expect(l1.head.next.value).toBe(1);

  l1 = new LinkedList(make(1));
  l1.insert(make(2), 10);
  expect(l1.head.value).toBe(1);
  expect(l1.head.next.value).toBe(2);

  // l1 = new LinkedList(make(1));
  // l1.insert(make(2), 2);
  // l1.insert(make(3), 3);
  // expect(l1.head.value).toBe(1);
  // expect( l1.head.next.value).toBe(2);
});
