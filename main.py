class Caesar_cipher:
    def __init__(self, text: str, n: int):
        self.text = text
        self.num = n

    def caesar_encryption(self):
        self.text = "".join([chr(ord(t) + self.num) for t in self.text])
        print(f'暗号化:{self.text}',end='\n')

    def caesar_composite(self):
        self.text = "".join([chr(ord(t) - self.num) for t in self.text])
        print(f'複合化:{self.text}',end='\n')

    def __str__(self):
        return f'登録文字:{self.text} 移行させる数:{self.num}\n'


file_name = 'sample.txt'
sample_text = 'サンプルテキスト'
num_of_move_char = 3

try:
    f = open(file_name, 'r', encoding='UTF-8')
    input_text = f.read()
    f.close()
    # print(f'読み込まれたファイルの内容は\n{input_text}\nです。\n')
except FileNotFoundError:
    print(f'ファイル:{file_name}が無かったので\n{sample_text}\nを代入します。\n')
    input_text = 'サンプルテキスト'


input01 = Caesar_cipher(input_text, num_of_move_char)
print(str(input01),end='\n')
input01.caesar_encryption()
input01.caesar_composite()