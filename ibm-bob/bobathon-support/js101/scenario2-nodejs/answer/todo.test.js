const test = require('node:test');
const assert = require('node:assert');
const { addTodo, toggleTodo, removeTodo } = require('./todo');

const sample = () => [
  { id: 1, title: 'A', done: false },
  { id: 2, title: 'B', done: true },
  { id: 3, title: 'C', done: false },
];

// T1
test('T1: 空配列に追加すると件数が1増え、id は 1、done は false になる', () => {
  assert.deepStrictEqual(addTodo([], '牛乳'), [
    { id: 1, title: '牛乳', done: false },
  ]);
});

test('T1: 既存の要素があれば id は最大 id + 1 になる', () => {
  const result = addTodo(sample(), 'D');
  assert.strictEqual(result.length, 4);
  assert.deepStrictEqual(result[3], { id: 4, title: 'D', done: false });
});

// T2
test('T2: 空文字は追加されない', () => {
  assert.deepStrictEqual(addTodo(sample(), ''), sample());
});

test('T2: 空白のみは追加されない', () => {
  assert.deepStrictEqual(addTodo(sample(), '   '), sample());
});

// T3
test('T3: 前後の空白は除去される', () => {
  assert.strictEqual(addTodo([], '  牛乳  ')[0].title, '牛乳');
});

// T4
test('T4: 切り替えると指定した id の done が true になる', () => {
  assert.strictEqual(toggleTodo(sample(), 1)[0].done, true);
});

test('T4: 存在しない id では内容が変わらない', () => {
  assert.deepStrictEqual(toggleTodo(sample(), 99), sample());
});

// T5
test('T5: 2回切り替えると done が元に戻る', () => {
  assert.deepStrictEqual(toggleTodo(toggleTodo(sample(), 1), 1), sample());
});

// T6
test('T6: 削除すると指定した要素だけが消え、ほかは残る', () => {
  assert.deepStrictEqual(removeTodo(sample(), 2), [
    { id: 1, title: 'A', done: false },
    { id: 3, title: 'C', done: false },
  ]);
});

test('T6: 存在しない id では何も消えない', () => {
  assert.deepStrictEqual(removeTodo(sample(), 99), sample());
});

// T7
test('T7: addTodo は元の配列を変更しない', () => {
  const original = sample();
  addTodo(original, 'D');
  assert.deepStrictEqual(original, sample());
});

test('T7: toggleTodo は元の配列を変更しない', () => {
  const original = sample();
  toggleTodo(original, 1);
  assert.deepStrictEqual(original, sample());
});

test('T7: removeTodo は元の配列を変更しない', () => {
  const original = sample();
  removeTodo(original, 1);
  assert.deepStrictEqual(original, sample());
});
