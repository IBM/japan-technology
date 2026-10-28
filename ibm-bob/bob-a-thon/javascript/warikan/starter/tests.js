// tests.js — 自動テストを書くファイル
//
// 1行が1つのテストです。test.html を開くと、上から順に実行されて ○ × が並びます。
//
//   check("説明（日本語でOK）", 実際の値, 期待する値);
//
// 書き方の例（先頭の // を外すと動きます）:
//   section("基本の割り勘");
//   check("12,345円を5人で割ると1人2,469円", calcSplit({ total: 12345, people: 5 }).each, 2469);
//   check("人数が0ならエラーになる", calcSplit({ total: 1000, people: 0 }), { error: ANY_TEXT });
//
// このファイルの中身は cases.md の表をもとに Bob が追加します。
