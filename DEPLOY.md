# 公開・更新の仕組み（しずく コーポレートサイト）

このサイトは **GitHub → Netlify の自動デプロイ** で公開しています。
ファイルを編集して GitHub に push すると、**約30〜60秒で自動的に本番サイトへ反映**されます。

- 本番URL: https://sizucu.netlify.app
- GitHubリポジトリ: `sizucu-website`（Private）
- ホスティング: Netlify（サイト名 `sizucu`）

---

## 更新のやり方

### 方法A: Claude に頼む（おすすめ）

「サイトの○○を直して公開して」と Claude Code に頼めば、編集から push まで自動で行います。
push されると Netlify が自動デプロイします。

### 方法B: 自分で公開する

1. このフォルダ内の HTML を編集する
2. **`公開.bat` をダブルクリック**する
   - 変更を自動でコミットし、GitHub に push します
3. 30〜60秒後に https://sizucu.netlify.app に反映されます

> `公開.bat` は内部で `publish.ps1` を呼び、`git add → commit → push` をまとめて実行します。

---

## 公開される範囲とされない範囲

`netlify.toml` でリポジトリのルートを公開しています。ただし以下は **`.gitignore` で除外**しており、
GitHub にも Web にも公開されません（個人情報・内部メモのため）。

- `README.md` … 社内向け詳細ドキュメント（連絡先メール等を含む）
- `CLAUDE_CODE_GUIDE.md` … 開発メモ
- `deploy.ps1` … 旧・手動デプロイ用スクリプト（緊急時の予備として残置）
- `backup_*/` `Netlifyアップ用/` `files.zip` … 過去バージョン・作業フォルダ

---

## 元に戻したいとき（ロールバック）

- **GitHub**: 過去のコミットにいつでも戻せます（全履歴が保存されています）
- **Netlify**: 管理画面 https://app.netlify.com/projects/sizucu の「Deploys」から、
  過去のデプロイを選んで「Publish deploy」でワンクリック巻き戻しできます

---

## 緊急時の予備手段（旧方式）

GitHub / Netlify 連携が使えない緊急時のみ、従来の手動デプロイも使えます。

```powershell
# Netlify CLI で直接デプロイ（要 netlify login）
powershell -ExecutionPolicy Bypass -File .\deploy.ps1
```

または Netlify 管理画面の「Deploys」へファイルをドラッグ&ドロップ。

---

最終更新: 2026年6月（GitHub + Netlify 自動デプロイを構築）
