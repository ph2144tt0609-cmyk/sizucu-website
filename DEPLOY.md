# 公開・更新の仕組み（しずく コーポレートサイト）

このサイトは **GitHub Pages（deploy-from-branch / main）** で公開しています。
ファイルを編集して GitHub に push すると、**約1〜2分で自動的に本番サイトへ反映**されます。

- 本番URL: https://www.sizucu.co.jp/
- GitHubリポジトリ: `sizucu-website`（Public — GitHub Pages 無料枠の要件）
- ホスティング: GitHub Pages（main ブランチのルートをそのまま配信）
- 旧URL: https://sizucu.netlify.app → `_redirects` により新URLへ301転送
  （Netlify のデプロイ再開後に有効化。2026-07-10 に移行）

---

## 独自ドメインの初回設定（1回のみ）

このリポジトリには `CNAME`（`www.sizucu.co.jp`）を配置済みです。ドメイン取得後、
DNSを次のように設定し、DNS設定と同じタイミングでこの変更を `main` に反映します。

| 種別 | ホスト名 | 値 |
|---|---|---|
| CNAME | `www` | `ph2144tt0609-cmyk.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

1. GitHubリポジトリの **Settings → Pages → Custom domain** に `www.sizucu.co.jp` を入力
2. DNS Checkが成功したら **Enforce HTTPS** を有効化
3. GitHubアカウント側でドメイン所有権を確認し、サブドメイン乗っ取り対策を行う

> **重要**: ドメイン取得・DNS設定より先に `CNAME` を `main` へ反映しないこと。
> 先に反映すると、現在のGitHub Pages URLから未設定ドメインへ転送され、サイトを閲覧できなくなる可能性があります。

[GitHub公式: カスタムドメインの管理](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

---

## 更新のやり方

### 方法A: Claude に頼む（おすすめ）

「サイトの○○を直して公開して」と Claude Code に頼めば、編集から push まで自動で行います。
push されると GitHub Pages が自動で再配信します。

### 方法B: 自分で公開する

1. このフォルダ内の HTML を編集する
2. **`公開.bat` をダブルクリック**する
   - 変更を自動でコミットし、GitHub に push します
3. 1〜2分後に https://www.sizucu.co.jp/ に反映されます

> `公開.bat` は内部で `publish.ps1` を呼び、`git add → commit → push` をまとめて実行します。

---

## 公開される範囲とされない範囲

main ブランチのルートがそのまま公開されます。ただし以下は **`.gitignore` で除外**しており、
GitHub にも Web にも公開されません（個人情報・内部メモのため）。

- `README.md` … 社内向け詳細ドキュメント（連絡先メール等を含む）
- `CLAUDE_CODE_GUIDE.md` … 開発メモ
- `deploy.ps1` … 旧・手動デプロイ用スクリプト（緊急時の予備として残置）
- `backup_*/` `Netlifyアップ用/` `files.zip` … 過去バージョン・作業フォルダ

> **注意**: リポジトリは Public のため、コミットしたファイルはすべて誰でも閲覧できます。
> 個人情報・内部メモは絶対にコミットしないこと（.gitignore を必ず確認）。

---

## GitHub Pages で使えない Netlify 機能（移行時の対応）

- `_redirects`（短縮URL 301） → 各エイリアスの meta refresh スタブ
  （`midori.html` `numazu.html` `koen.html` `shizuoka.html` `career.html` `jobs.html` `benefits.html`）
  で代替。`/recruit` など**ファイル名と同じ拡張子なしURLは GitHub Pages が自動解決**する。
- `_headers`（セキュリティ/キャッシュヘッダー） → GitHub Pages 非対応のため廃止（静的サイトのため影響軽微）
- お問い合わせフォームは **Formspree** のためホスティング非依存（そのまま動作）

---

## 元に戻したいとき（ロールバック）

- **GitHub**: 過去のコミットにいつでも戻せます（全履歴が保存されています）
- 巻き戻したいコミットへ `git revert` して push すれば、1〜2分で本番も戻ります

---

最終更新: 2026年7月10日（Netlify → GitHub Pages へ移行）
