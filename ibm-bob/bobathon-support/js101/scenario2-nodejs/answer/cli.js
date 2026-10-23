const readline = require('node:readline');
const { addTodo, toggleTodo, removeTodo } = require('./todo');

let todos = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: '> ',
});

function parseId(text) {
  return /^[0-9]+$/.test(text) ? Number(text) : null;
}

function handleLine(line) {
  const input = line.trim();
  if (input === '') return;

  const spaceIndex = input.search(/\s/);
  const command = spaceIndex === -1 ? input : input.slice(0, spaceIndex);
  const arg = spaceIndex === -1 ? '' : input.slice(spaceIndex + 1).trim();

  if (command === 'add') {
    const next = addTodo(todos, arg);
    if (next.length === todos.length) {
      console.log('タイトルを入力してください');
    } else {
      todos = next;
      const added = todos[todos.length - 1];
      console.log(`追加しました: ${added.id}: ${added.title}`);
    }
  } else if (command === 'list') {
    if (todos.length === 0) {
      console.log('(タスクはありません)');
    } else {
      for (const todo of todos) {
        console.log(`[${todo.done ? 'x' : ' '}] ${todo.id}: ${todo.title}`);
      }
    }
  } else if (command === 'done' || command === 'remove') {
    const id = parseId(arg);
    if (id === null || !todos.some((todo) => todo.id === id)) {
      console.log(`id が見つかりません: ${arg}`);
    } else if (command === 'done') {
      todos = toggleTodo(todos, id);
      console.log(`切り替えました: ${id}`);
    } else {
      todos = removeTodo(todos, id);
      console.log(`削除しました: ${id}`);
    }
  } else if (command === 'exit') {
    rl.close();
    return;
  } else {
    console.log(`不明なコマンドです: ${input}`);
  }
}

rl.on('line', (line) => {
  handleLine(line);
  rl.prompt();
});
rl.on('close', () => process.exit(0));
rl.prompt();
