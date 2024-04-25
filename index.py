import random
import os #ファイル、フォルダのパス取得

#色付け
RED = "\033[31m"


#フォントスタイル
MARKER = "\033[7m"
BOLD = "\033[1m" #太字
UNDERLINE = "\033[4m"

#末尾制御
END = "\033[0m"

def save_score(score,high_score):
    if score > high_score:
        with open("high_score.txt","w") as file:
            file.write(str(score))
        return score
    return high_score

def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt","r") as file:
            return int(file.read())
    else:
        return 0

def game_intro():
    print(f"{BOLD}{UNDERLINE}～ CRAP LUCK GAME ～{END}")#クソ運ゲー
    print("１.ゲームが開始すると、３つの選択肢のうちランダムに\"１つ\"が安全な選択として抽選されます。")
    print("２.プレイヤーは\"1,2,3\"の中から一つを選び、その選択が安全であればスコアが１点加算され、ゲームが続行します。")
    print("３.安全でない選択をするとゲームオーバーとなり、現在のスコアとハイスコアが表示されます。")
    print(f"４.{RED}運ゲー{END}")
    input("Enterキーを押すとゲームスタート！")

def play_game(high_score,score):
    while True:
        safe_line = random.randint(1,3)
        os.system('cls' if os.name == 'nt' else 'clear')  # 画面をクリア
        print(f"ハイスコア：{high_score}")
        print(f"スコア：{score}")
        print("\n１, ２, ３の数字から一つを入力選択, \" q \" でゲーム終了します >>", end="")

        move = input()
        if move.lower() == "q":
            print("\nゲームを終了します")
            print(f"最終スコア：{score}")
            save_score(score, high_score)
            break
        elif move in ["1", "2", "3"]:
            player_choice = int(move)
            if player_choice != safe_line:
                print(f"{RED}ゲームオーバー！{END}")
                print("運に見放されました。")
                print(f"スコア：{score}")
                high_score = save_score(score, high_score)
                choice = input("最初から「1」 / 終了する「Enter」 >> ")
                if choice.lower() == "1":
                    return play_game(high_score, 0)  # 最初から始める
                else:
                    break  # ゲームを終了
            score += 1


def game_main():
    high_score = load_high_score()    
    score = 0

    game_intro()#ゲーム説明
    play_game(high_score,score)

if __name__ == "__main__":
    game_main()