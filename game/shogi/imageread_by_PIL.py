from scene import *
from PIL import Image
import ui, io
#from requests import get

class MyScene (Scene):
    def setup(self):
        # pilimageを読み込む
        pil_img = Image.open('hu.JPG')
        pil_img = pil_img.resize((100, 100))
        ''' urlから読み込むときはrequestsをインポートして以下の書き方 '''
        #url = 'https://'
        #pil_img = Image.open(io.BytesIO(get(url).content))

        # pilimageをtextureに変換する
        #pilimgfile = io.Bytes.IO()
        #pil_img.save(pilimgfile, format='png')
        #bytes_img = pilimgfile.getvalue()
        #uiimg = ui.Image.from_data(bytes_img)
        ''' 以下の書き方でもOK '''
        with io.BytesIO() as f:
            pil_img.save(f, format='png')
            uiimg = ui.Image.from_data(f.getvalue())

        texture = Texture(uiimg)

        # SpriteNodeを使い、スクリーンに追加する
        self.img = SpriteNode(texture, position=self.size/2)
        self.add_child(self.img)

if __name__=='__main__':
    run(MyScene(), show_fps=False)
