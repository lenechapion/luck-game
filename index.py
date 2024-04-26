import random
import os #ファイル、フォルダのパス取得

#色付け
RED = "\033[31m"


#フォントスタイル
MARKER = "\033[7m"
BOLD = "\033[1m" #太字
UNDERLINE = "\033[4m"

#末尾制御(スタイルリセット)
END = "\033[0m"

def save_score(score,high_score):
    if score > high_score:
        with open("high_score.txt","w") as file:#ファイル書き込み
            file.write(str(score))
        return score
    return high_score

def load_high_score():
    if os.path.exists("high_score.txt"):#ファイル存在確認
        with open("high_score.txt","r") as file:#ファイル読み込み
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
    print("１.ゲームが開始すると、２～３つの選択肢のうちランダムに\"１つ\"が一致選択として抽選されます。")
    print("２.プレイヤーは\"1~2\" , \"1~3\"の中から一つを選び、その選択が一致すればスコアが１点加算され、ゲームが続行します。")
    print("３.誤った選択をするとゲームオーバーとなります。")
    print(f"４.{RED}運ゲー{END}")
    input("Enterキーを押すとゲームスタート！")

def play_game(high_score,score,choices):
    while True:
        safe_line = random.randint(1,choices)#ランダム抽選
        os.system('cls' if os.name == 'nt' else 'clear')  # コンソール画面をクリア
        print(f"ハイスコア：{high_score}")
        print(f"スコア：{score}")
        print(f"\n1 ~ {choices}の数字から一つを入力選択, \" q \" でゲーム終了します >>", end="")

        move = input()
        if move.lower() == "q":
            print("\nゲームを終了します！")
            print(f"最終スコア：{score}")
            save_score(score, high_score)
            break
        if move.isdigit() and 1 <= int(move) <= choices:#選択肢数字のみ受付
            player_choice = int(move)
            if player_choice != safe_line:
                print(f"{RED}ゲームオーバー！{END}")
                print("運に見放されました。")
                print(f"スコア：{score}")
                high_score = save_score(score, high_score)
                choice = input("最初から「1 + Enter」 / 終了する「Enterのみ」 >> ")
                if choice.lower() == "1":
                    return play_game(high_score, 0, choices)  # スコア０で最初から始める
                else:
                    print("ゲームを終了します！")
                    break  # ゲームを終了
            score += 1
            if score % 50 == 0:
                print(f"\n{score}回達成！")



#ハイスコア読み込みとゲーム導入
def game_main():
    high_score = load_high_score()    
    score = 0
    game_intro()#ゲーム説明
    mode = get_game_mode() #モード選択
    choices = 2 if mode == 2 else 3
    play_game(high_score,score,choices)

if __name__ == "__main__":
    game_main()