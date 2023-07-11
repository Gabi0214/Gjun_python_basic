# 定義類別, 與類別屬性(封裝在類別中的變數和函式)
class IO:
    supportedSrcs = ["console", "file"]

    def read(src):
        print("Read from: ", src)
# 使用類別
