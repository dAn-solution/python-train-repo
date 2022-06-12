# Coding Challenge

Coding Challengeに挑戦しよう！

## Coding Challengeとは？
- DataScienceHubのメンバー限定コンテンツです．
- 毎週プログラミングの課題が追加されます．課題に従ってコーディングしてください．
- コミュニティ標準の言語はPythonですが，ご自身で好きな言語を使っていただいて構いません．
- 環境はご自身で作成してください．基本Python3を動かせればOKです．
- レベルはbeginner, intermediate, advancedの３つです．
- 課題は，各課題のフォルダのREADME.mdファイルに書いてあります．
- 締め切りなどはありません．好きな課題を自由に提出してください． 
- 答えは公開しません．提出されたものの中で模範回答レベルのものが出てきたら，それを一旦の模範回答として周知します．
- 運営側で提出されたプルリクエストに対してラベルをつけることがあります．ラベルの種類は現在4つあります．(後述)
- コードレビューやコメントが欲しい人は，PR(Pull Request)作成時に@dshub-communityにメンションし，その旨コメントに書いてください．また，Slackの#coding-challengeチャンネルに@かめもしくは@永山をメンションしてPRのURLを投稿してください．(詳細は[こちら](https://datawokagaku.com/coding_challenge/))
- 運営チームによるコードレビューはお時間いただきます．ご了承ください，advancedの課題は特に時間を要します！
- レビューはPython3のみとなります．
- プログラミングに正解はありませんので，模範回答よりいい書き方ができる場合もありますし，レビューコメントが必ずしも正解とは限りません．
- レビューで細かい点は指摘しません．クリティカルなところ，もう一歩先のレベルなど，ちょっとしたアドバイスをします．
- もっと色々気になる！という人は他の人のコードとそのレビューコメントを確認してください．
- 他の人のコードはPRの一覧から見ることができます．是非他の人がどのように取り組んでいるか見てみましょう！
- 他の人のコードで気になったことがあったら是非DataScienceHub内で聞いてみましょう！その際は#coding-challengeチャンネルをお使いください
- 完成しなくても，好きなタイミングでPRを出してOKです．分からないことがあればDataScienceHub内で質問してみましょう！誰か答えてくれるかも？？
- コードレビューでの指摘を修正したものを全て確認するのは大変なので，修正してさらにレビューが欲しい場合のみ，Slackにて再度新しくスレッドを立ててください．
- 同じ課題で複数回レビュー依頼をするとだんだん指摘内容が細かい点になっていき課題の本質とはずれていく＆終わりがないので，ある程度納得いくコードが書けたら他の方のコードやレビューコメントを読むことをお勧めします!



## 参加方法
参加方法は簡単です．より詳細な手順は[こちら](https://datawokagaku.com/coding_challenge/)をご参照ください．  
一般的な開発フローと同じなので，GitHubのいい練習にもなると思います．
基本的な流れは以下です．
1. 本リポジトリをforkする
2. cloneする
3. 本リポジトリをupstreamとして登録し，fetch&mergeで常に最新にしておく
4. masterからブランチを作成し，coding!
5. PR (Pull Request)  (課題のフォルダ名をPR名にしてください．)
これだけ！

## 課題一覧
---
### beginner
#### list-comprehension: リスト内包表記の課題
#### refactoring: リファクタリングの課題
#### linear-search-challenge: 線形探索の課題
#### roman-numerals-challenge: ローマ数字変換の課題
#### word-count-challenge: 単語カウントの課題  
#### anagram-challenge: アナグラムの課題
#### block-stairs-challenge: 階段の課題
#### rock-paper-scissors-challenge: じゃんけんの課題
#### coin-combination-challenge: 支払い金額の組み合わせ問題
#### prepare-coins-challenge: 利用硬貨の最適化の課題
#### rotate-list-challenge: リスト回転の課題
#### lambda-function-challenge: ラムダ関数の課題
#### try-except-practice: try-exceptの課題
---
### intermediate
#### 99-bottoles-challenge: 再帰の課題
#### binary-search-challenge: 二分探索の課題
#### swirl-list-challenge: 渦巻きリストの課題
#### fill-in-square-battle: マス塗り対戦
#### bubble-sort-challenge: バブルソートの課題
#### quick-sort-challenge: クイックソートの課題
#### run-length-encoding: 連長圧縮の課題
#### run-length-decoding: 連長復号の課題
#### tower-of-hanoi: ハノイの塔
#### reverse-polish-notation: 逆ポーランド記法
#### triangular-num-challenge: 三角数の課題
#### knapsack-challenge: ナップサック問題(動的計画法)
#### base-n-conversion: n進数変換の課題
#### higher-lower-game: higher or lower カードゲームの課題
#### max-substring-challenge: 最長部分文字列の課題
#### depth-first-search-challenge: 深さ優先探索の課題
#### move-chars-challenge: 文字移動の課題
#### add-binary-numbers: 2進数加法演算の課題
#### descending-order-numbers: 降順数リストの課題
---
### advanced
#### eight-puzzle-challenge: 幅優先探索の課題

## ラベル一覧
運営側で提出されたPRに対してラベルをつける場合があります．
ラベルの種類は以下の通りです．
- 模範解答レベル：課題の本質がきちんと解けていて，コードも読みやすく，無駄のない効率的なコードに対してつけます．
- 独創的：運営側でも想定していなかった，意外な方法で実装されたものに対してつけます．
- 親切：コードが読みやすく，リファクタリングもしやすく，きちんとコメントが書かれているものに対してつけます．
- 高品質：テストがきちんとされていて，品質が高いと思われるものに対してつけます．
#### 扱い方
- これらのラベルは，目指すものではありません．(例:ラベル欲しさに頑張ってテストコードを書く必要はありません．)
- 「このコードより自分の(または別の)コードの方が模範解答に近い！」という場合は是非#coding-challengeチャンネルに投稿してください．(時間差で運営側で審議中の場合もございますので，少しお時間経ってから投稿いただければと思います．)
- 逆に「このコードは○○という理由でこのラベルはふさわしくないのではないか？」という意見があれば，それも是非#coding-challengeチャンネルに投稿してください．
- PRを検索する際に，ラベルでフィルタできますので，是非ご活用ください．
- 権限上はラベルは誰でも付けれますが，ラベルづけは全て運営側で行いますので変更しないようお願いいたします．