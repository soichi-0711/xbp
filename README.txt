================================================================
  Template Party — マイテンプレ構成
================================================================

作成日時: 2026-05-06 20:47:56
フレーム: ビジネスイメージ（frame12-biz1）
         (id: frame12-biz1)

パーツ注入先: トップページ (index.html)

[同梱ファイルと使い方]

 index.html / page.html       : フレームの土台HTML
                                （選択された方の <main> に選択パーツを流し込み済み）
 css/style.css  他            : フレームのベースCSS
 css/parts.css                : 選択したパーツのCSSを連結済み
 js/parts.js                  : 選択したパーツのJSを連結済み

> そのままブラウザで index.html を開けば、選択したパーツが
  フレームのレイアウト・CSSに乗った状態で表示されます。

[選択したパーツ（4 件／注入順）]

 01. フッターブロック（footer3）
     id    : footer3
     html  : index.html の </div><!--/#contents--> の直下に注入（footer専用位置）
     css   : css/parts.css に連結済み

 02. CTAセクション（ui-tools-cta1）
     id    : ui-tools-cta1
     html  : index.html の <main> に注入済み
     css   : css/parts.css に連結済み

 03. CTAセクション（ui-tools-cta1）
     id    : ui-tools-cta1
     html  : index.html の <main> に注入済み
     css   : css/parts.css に連結済み

 04. CTAセクション（ui-tools-cta1）
     id    : ui-tools-cta1
     html  : index.html の <main> に注入済み
     css   : css/parts.css に連結済み

---
Template Party — https://template-party.com/