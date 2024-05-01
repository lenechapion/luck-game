import random
import os #ファイル、フォルダのパス取得
import time

#色付け
RED = "\033[31m"


#フォントスタイル
MARKER = "\033[7m"
BOLD = "\033[1m" #太字
UNDERLINE = "\033[4m"

#末尾制御(スタイルリセット)
END = "\033[0m"

def save_score(score, high_score, mode):
    filename = f"high_score_mode_{mode}.txt"#ファイル書き込み
    if score > high_score:
        with open(filename, "w") as file:
            file.write(str(score))
        return score
    return high_score

def load_high_score(mode):
    filename = f"high_score_mode_{mode}.txt"
    if os.path.exists(filename):#ファイル存在確認
        with open(filename, "r") as file:#ファイル読み込み
            return int(file.read())
        #ファイルが無ければ０を返す    
    else:
        return 0


def get_game_mode():
    while True:
        print(f"{BOLD}モード選択{END}")
        print("1： 2択バージョン")
        print("2： 3択バージョン")
        mode = input("選択入力してください (1 or 2) >>")
        if mode in ["1","2"]:
            return int(mode)
        print("無効な入力です！ 1 or 2 を入力してください\n")



def game_intro():
    print(f"{BOLD}{UNDERLINE}～ CRAP LUCK GAME ～{END}")#タイトル：クソ運ゲー
    print("***このゲームは次のように進行します***")
    print("１.ゲームが開始すると、まずゲームモードを選択します。")
    print("　 ２択or３択ゲームのどちらかを選択してください。\n ")
    print("２.選択したモードに基づいて、ランダムに\"１つ\"の安全な選択肢が設定されます。")
    print("　 ２択ゲームの場合:「１または２」")
    print("　 ３択ゲームの場合:「１ から ３」の中から選びます。\n")
    print("３.プレイヤーは提示された選択肢の中から一つを選択入力し、それが一致すればスコアが１点加算され、ゲームが続行されます。\n")
    print("４.誤った選択をすると、ゲームオーバーとなり、その時点でのスコアが記録されます。")
    print("　 最高スコアを更新していた場合は新しいハイスコアが保存されます。\n")
    print(f"５.{BOLD}要は{RED}運ゲー{END}{BOLD}です。{END}")
    input("***Enterキーを押すとゲームスタート！***\n")

def play_game(high_score, score, choices, mode):
    while True:
        safe_line = random.randint(1, choices)
        os.system('cls' if os.name == 'nt' else 'clear')#コンソール画面をクリア
        print(f"ハイスコア：{high_score}")
        print(f"スコア：{score}")
        print(f"\n1 ~ {choices} の数字から一つを入力選択, \"q\" でゲーム終了します >>", end="")

        move = input()
        if move.lower() == "q":
            print("\nゲームを終了します！")
            print(f"最終スコア：{score}")
            save_score(score, high_score, mode)
            break
        elif move.isdigit() and 1 <= int(move) <= choices:#選択肢数字のみ受け付け
            player_choice = int(move)
            if player_choice == safe_line:
                print("スコアアップ！")
                score += 1
                if score % 10 == 0:#10回ごとにメッセージ表示
                    print(f"\n{score}回達成！！")
                time.sleep(1)#１秒表示
            else:
                print(f"{RED}ゲームオーバー！{END}")
                print("運に見放されました。")
                print(f"スコア：{score}")
                high_score = save_score(score, high_score, mode)
                choice = input("最初から「1 + Enter」 / 終了する「Enterのみ」 >> ")
                if choice.lower() == "1":
                    return play_game(high_score, 0, choices, mode)  # スコア0で最初から始める
                else:
                    print("ゲームを終了します！")
                    print("お疲れさまでした！")
                    break
        else:
            print("無効な入力です！")



#ハイスコア読み込み＋ゲーム導入
def game_main():
    game_intro()  # ゲーム説明
    mode = get_game_mode()  # モード選択
    #選択肢の数決定
    choices = 2 if mode == 1 else 3#mode1=2択,それ以外は3択
    high_score = load_high_score(mode)  # モードに基づいたハイスコアを読み込み
    score = 0
    play_game(high_score, score, choices, mode)

if __name__ == "__main__":
    game_main()