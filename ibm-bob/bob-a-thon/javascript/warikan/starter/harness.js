/*
 * harness.js — ブラウザーだけで動く、小さなテストランナー（主催者提供・編集しないでください）
 *
 * 使い方（tests.js に書く）:
 *   check("説明", 実際の値, 期待する値);
 *
 *   例:
 *   check("10,000円を3人で割ると1人3,334円", calcSplit({ total: 10000, people: 3 }).each, 3334);
 *   check("結果をまとめて確認", calcSplit({ total: 10000, people: 3 }), { each: 3334, change: 2 });
 *   check("人数0はエラー", calcSplit({ total: 100, people: 0 }), { error: ANY_TEXT });
 *
 * ルール:
 *   - 期待する値がオブジェクトのときは、書いたキーだけを比べます（他のキーは無視）
 *   - ANY_TEXT は「空でない文字列なら何でもよい」の意味です（エラーメッセージの確認に使う）
 *   - section("見出し") で結果をグループ分けできます
 */
(function () {
  'use strict';

  var results = [];          // { section, name, ok, actual, expected, error }
  var currentSection = '';
  // logic.js / tests.js の読み込み中に起きたエラー（構文エラー・未定義の関数など）。
  // test.html の先頭で window.__loadErrors に集めている（logic.js より前に仕掛ける必要があるため）
  var loadErrors = window.__loadErrors || (window.__loadErrors = []);
  if (!window.__loadErrorsHooked) {
    window.__loadErrorsHooked = true;
    window.addEventListener('error', function (e) {
      var where = e.filename ? e.filename.split('/').pop() + (e.lineno ? ':' + e.lineno : '') : '';
      var msg = (where ? where + ' — ' : '') + (e.message || String(e.error));
      if (loadErrors.indexOf(msg) < 0) loadErrors.push(msg);
    });
  }
  // logic.js が読めていても calcSplit が無い（名前違い・文法ミスで途中まで）ことがあるので先に確かめる
  if (typeof window.calcSplit !== 'function') {
    loadErrors.push('logic.js に calcSplit という名前の関数が見つかりません（AGENTS.md の契約どおり function calcSplit(input) を定義してください）');
  }

  window.ANY_TEXT = { __anyText: true };

  function isPlainObject(v) {
    return v !== null && typeof v === 'object' && !Array.isArray(v);
  }

  function matches(actual, expected) {
    if (expected === window.ANY_TEXT) {
      return typeof actual === 'string' && actual.trim().length > 0;
    }
    if (isPlainObject(expected)) {
      if (!isPlainObject(actual)) return false;
      return Object.keys(expected).every(function (k) { return matches(actual[k], expected[k]); });
    }
    if (Array.isArray(expected)) {
      if (!Array.isArray(actual) || actual.length !== expected.length) return false;
      return expected.every(function (v, i) { return matches(actual[i], v); });
    }
    if (typeof expected === 'number' && typeof actual === 'number') {
      if (Number.isNaN(expected) && Number.isNaN(actual)) return true;
      return Math.abs(actual - expected) < 1e-9;
    }
    return actual === expected;
  }

  function show(v) {
    if (v === window.ANY_TEXT) return '（何か文字列）';
    if (v === undefined) return 'undefined（値がありません）';
    if (typeof v === 'number' && Number.isNaN(v)) return 'NaN（数値になっていません）';
    if (typeof v === 'number' && !Number.isFinite(v)) return String(v) + '（無限大）';
    if (typeof v === 'function') return '（関数）';
    try { return JSON.stringify(v); } catch (e) { return String(v); }
  }

  window.section = function (title) {
    currentSection = String(title || '');
  };

  window.check = function (name, actual, expected) {
    results.push({ section: currentSection, name: String(name), ok: matches(actual, expected), actual: actual, expected: expected });
  };

  // 実行中に例外が出るケースを安全に書くための補助: run(() => calcSplit(...))
  window.run = function (fn) {
    try { return fn(); } catch (e) { return { error: '例外: ' + (e && e.message ? e.message : String(e)) }; }
  };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function summaryText() {
    var lines = [];
    var pass = results.filter(function (r) { return r.ok; }).length;
    var fail = results.length - pass;
    lines.push('【テスト結果】 ' + results.length + '件中 ' + pass + '件 成功 / ' + fail + '件 失敗');
    if (loadErrors.length) {
      lines.push('');
      lines.push('【読み込みエラー】');
      loadErrors.forEach(function (m) { lines.push('  ' + m); });
    }
    var sec = null;
    results.forEach(function (r) {
      if (r.section !== sec) { sec = r.section; if (sec) { lines.push(''); lines.push('■ ' + sec); } }
      lines.push((r.ok ? '  ○ ' : '  × ') + r.name);
      if (!r.ok) {
        lines.push('      期待: ' + show(r.expected));
        lines.push('      実際: ' + show(r.actual));
      }
    });
    return lines.join('\n');
  }

  function render() {
    var root = document.getElementById('results');
    if (!root) return;
    var pass = results.filter(function (r) { return r.ok; }).length;
    var fail = results.length - pass;
    var html = '';

    var status = 'empty', label = 'テストがまだありません';
    if (loadErrors.length) { status = 'fail'; label = '読み込みエラーがあります'; }
    else if (results.length && fail === 0) { status = 'pass'; label = 'すべて成功'; }
    else if (fail > 0) { status = 'fail'; label = fail + '件 失敗'; }

    html += '<div class="banner ' + status + '">' +
      '<div class="big">' + esc(label) + '</div>' +
      '<div class="small">' + results.length + '件中 ' + pass + '件 成功 / ' + fail + '件 失敗</div>' +
      '</div>';

    if (loadErrors.length) {
      html += '<div class="loaderr"><strong>読み込みエラー</strong>（logic.js や tests.js の文法ミス、存在しない関数の呼び出しなど）<ul>';
      loadErrors.forEach(function (m) { html += '<li>' + esc(m) + '</li>'; });
      html += '</ul><p>このメッセージを Bob に貼り付けて「このエラーを直して」と頼んでください。</p></div>';
    }

    if (!results.length && !loadErrors.length) {
      html += '<p class="hint">tests.js に <code>check(...)</code> を書くと、ここに結果が並びます。' +
        'cases.md の表を Bob に渡して「tests.js にテストを追加して」と頼みましょう。</p>';
    }

    var sec = null;
    results.forEach(function (r, i) {
      if (r.section !== sec) {
        sec = r.section;
        if (sec) html += '<h2>' + esc(sec) + '</h2>';
      }
      html += '<div class="case ' + (r.ok ? 'ok' : 'ng') + '">' +
        '<div class="mark">' + (r.ok ? '○' : '×') + '</div>' +
        '<div class="body"><div class="name">' + (i + 1) + '. ' + esc(r.name) + '</div>';
      if (!r.ok) {
        html += '<table class="diff"><tr><th>期待</th><td>' + esc(show(r.expected)) + '</td></tr>' +
          '<tr><th>実際</th><td>' + esc(show(r.actual)) + '</td></tr></table>';
      }
      html += '</div></div>';
    });
    root.innerHTML = html;

    var ta = document.getElementById('summary');
    if (ta) ta.value = summaryText();
    document.title = (status === 'pass' ? '○ ' : status === 'fail' ? '× ' : '') + '割り勘 テスト結果';
  }

  function copySummary() {
    var ta = document.getElementById('summary');
    var msg = document.getElementById('copymsg');
    if (!ta) return;
    var text = ta.value;
    function done(ok) {
      if (msg) {
        msg.textContent = ok ? 'コピーしました。Bob のチャットに貼り付けてください。' : 'コピーできませんでした。下の枠の文字を選んでコピーしてください。';
        msg.className = ok ? 'copied' : 'copyfail';
      }
      if (!ok) { ta.focus(); ta.select(); }
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { fallback(); });
    } else {
      fallback();
    }
    function fallback() {
      try {
        ta.focus(); ta.select();
        done(document.execCommand('copy'));
      } catch (e) { done(false); }
    }
  }

  window.addEventListener('DOMContentLoaded', function () {
    render();
    var btn = document.getElementById('copy');
    if (btn) btn.addEventListener('click', copySummary);
    var rl = document.getElementById('reload');
    if (rl) rl.addEventListener('click', function () { location.reload(); });
  });

  // Playwright 等からの検証用
  window.__harness = { results: results, loadErrors: loadErrors, summaryText: summaryText };
})();
