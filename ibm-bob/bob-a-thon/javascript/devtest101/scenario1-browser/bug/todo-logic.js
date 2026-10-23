// Bugあり、ToDo のロジック。画面(DOM)には依存しない。引数の配列は変更しない。

function addTodo(list, title) {
  const trimmed = String(title).trim();
  if (trimmed === '') {
    return list.slice();
  }
  const maxId = list.reduce((max, todo) => Math.max(max, todo.id), 0);
  return [...list, { id: maxId + 1, title: trimmed, done: false }];
}

function toggleTodo(list, id) {
  return list.map((todo) =>
    todo.id === id ? { ...todo, done: !todo.done } : { ...todo }
  );
}

function removeTodo(list, id) {
  return list.filter((todo) => todo.id === id);
}
