# LUCK GAME(運試しゲーム)

このゲームは、ランダムに生成される安全な選択肢をプレイヤーが当てるシンプルな運試しゲームです。

ゲーム進行は以下の通りです。

1. **ゲームモードの選択**:
    - ゲームが開始すると、プレイヤーはまずゲームモードを選択します。2択ゲームか3択ゲームのいずれかを選びます。

2. **選択肢の設定**:
    - 選択したモードに基づいて、ランダムに「1つ」の安全な選択肢が設定されます。
    - 2択ゲームの場合は「1または2」、3択ゲームの場合は「1から3」の中から選びます。

3. **選択肢の選択**:
    - プレイヤーは提示された選択肢の中から一つを選択します。
    - その選択が安全な選択肢と一致すれば、スコアが1点加算され、ゲームは続行されます。

4. **ゲームオーバー**:
    - 誤った選択をすると、「運に見放されました」と表示されゲームオーバーとなります。
    - その時点でのスコアが記録され、最高スコアを更新していた場合は新しいハイスコアが保存されます。

# Features

**シンプルなルール**　  ：選択式直感ゲーム

**選択肢に応じた緊張感**：選択肢が増えるほど、リスクが増します

**繰り返し遊べる設計**　：ランダム性により、毎回異なる結果が得られます


# DEMO
タイトル＆モード選択画面：
![スクリーンショット1](https://github.com/lenechapion/luck-game/assets/155729519/b7b26f11-359c-4ff1-a288-d52dd112dd43)

プレイ画面：
選択肢が一致するとスコアアップと１秒間表示された後、ゲームが継続します。

![スクリーンショット2](https://github.com/lenechapion/luck-game/assets/155729519/f945057b-ff67-4ffe-bb5a-c7994f57f901)

リザルト画面：

![スクリーンショット3](https://github.com/lenechapion/luck-game/assets/155729519/57035c03-90ff-4a51-99bf-c745f80d011d)



# Requirement

Python標準のライブラリで動作します。


# Installation

下記SSHソースコードをダウンロードし、Python環境で直接実行することができます。

git clone git@github.com:lenechapion/luck-game.git

# Usage

上記のインストール手順に従い、ローカルの環境でゲームを起動してください。
コンソール上でゲームをプレイできます。

# Note

このゲームは完全にランダムに基づいているため、戦略よりも運が重要になります。
それぞれのモードでベストスコアを目指しましょう。
また、連続で成功すると特定回数毎に、追加コメントが表示されます。

---
現在の仕様では、選択モード問わずスコア結果は統合され、最高スコアのみ記録されるようになっています。（修正済み）