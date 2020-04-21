from scene import *
from PIL import Image, ImageDraw
import ui, io

def original_image2Texture(img_name):
	img = Image.open(img_name)
	img = img.resize((piece_size, piece_size))
	img = convert_PILImage2Texture(img)	
	return img
	
def convert_PILImage2Texture(img):
	with io.BytesIO() as f:
			img.save(f, format='png')
			img = ui.Image.from_data(f.getvalue())
	return Texture(img)
	
def coordinate_on_board(x, y):
		return ((((screen_size.x - board_size) * 0.5) + x),
						(((screen_size.y - board_size) * 0.5) + y))
																   
class shogi(Scene):
	def setup(self):
		self.rootNode = Node(parent = self)	
		self.background_color = '#f9ffec'
		
		#draw shogi board
		#To add 1 to board_size to draw the right end and bottom lines
		img = Image.new('RGB', (board_size + 1, board_size + 1), (255, 255, 255))
		draw = ImageDraw.Draw(img)
		for x in range(9):
			for y in range(9):
				draw.rectangle((square_size * x, 			 square_size * y, 
											  square_size * (x + 1), square_size * (y + 1)), 
												fill = (190, 160, 150), outline = (0, 0, 0))
		board = convert_PILImage2Texture(img)
		self.board = SpriteNode(board, position=self.size/2)
		self.rootNode.add_child(self.board)
		self.setup_all_pieces()
		
	def setup_all_pieces(self):
		self.piece_list = []
		for x in range(9):
				self.hu = Hu(x + 1, 3)
				self.rootNode.add_child(self.hu)
				self.piece_list.append(self.hu)
		self.kyosya = Kyosya(1, 1)
		self.rootNode.add_child(self.kyosya)
		self.piece_list.append(self.kyosya)
		self.kyosya = Kyosya(9, 1)
		self.rootNode.add_child(self.kyosya)
		self.piece_list.append(self.kyosya)
		self.keima = Keima(2, 1)
		self.rootNode.add_child(self.keima)
		self.piece_list.append(self.keima)
		self.keima = Keima(8, 1)
		self.rootNode.add_child(self.keima)
		self.piece_list.append(self.keima)
		self.ginsyo = Ginsyo(3, 1)
		self.rootNode.add_child(self.ginsyo)
		self.piece_list.append(self.ginsyo)
		self.ginsyo = Ginsyo(7, 1)
		self.rootNode.add_child(self.ginsyo)
		self.piece_list.append(self.ginsyo)
		self.kinsyo = Kinsyo(4, 1)
		self.rootNode.add_child(self.kinsyo)
		self.piece_list.append(self.kinsyo)
		self.kinsyo = Kinsyo(6, 1)
		self.rootNode.add_child(self.kinsyo)
		self.piece_list.append(self.kinsyo)
		self.hisya = Hisya(8, 2)
		self.rootNode.add_child(self.hisya)
		self.piece_list.append(self.hisya)
		self.kakugyo = Kakugyo(2, 2)
		self.rootNode.add_child(self.kakugyo)
		self.piece_list.append(self.kakugyo)
		self.ousyo = Ousyo(5, 1)
		self.rootNode.add_child(self.ousyo)
		self.piece_list.append(self.ousyo)
		
	def touch_began(self, touch):
		x, y = touch.location
		
	def touch_moved(self, touch):
		x, y = touch.location
		move_action = Action.move_to(x, y, 0.1, TIMING_BOUNCE_OUT)
		self.hu.run_action(move_action)
		
	def touch_ended(self, touch):
		x, y = touch.location
		if x < 300:
			x, y = self.hu.previous_position
			move_action = Action.move_to(x, y, 0.1, TIMING_BOUNCE_OUT)
			self.hu.run_action(move_action)
		else:
			self.hu.previous_position = x, y
						
class Piece(SpriteNode):
	def __init__(self, img, x, y):
		SpriteNode.__init__(self, img)
		self.position = squares[str(x) + ',' + str(y)]
		self.previous_position = squares[str(x) + ',' + str(y)]
		
class Hu (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, hu, x, y)
		
class Keima (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, keima, x, y)
		
class Kyosya (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, kyosya, x, y)
		
class Ginsyo (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, ginsyo, x, y)
		
class Kinsyo (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, kinsyo, x, y)
		
class Kakugyo (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, kakugyo, x, y)
		
class Hisya (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, hisya, x, y)
		
class Ousyo (Piece):
	def __init__(self, x, y):
		Piece.__init__(self, ousyo, x, y)

screen_size = get_screen_size()
#I want the board size to be a multiple of 9 because the shogi board is 9 × 9 square
board_size  = int(screen_size.x * 0.9) // 9 * 9
square_size = int(board_size / 9)
piece_size  = int(square_size)

#road all pieces
hu       = original_image2Texture('image/hu.PNG')
keima    = original_image2Texture('image/keima.PNG')
kyosya   = original_image2Texture('image/kyosya.PNG')
ginsyo   = original_image2Texture('image/ginsyo.PNG')
kinsyo   = original_image2Texture('image/kinsyo.PNG')
kakugyo  = original_image2Texture('image/kakugyo.PNG')
hisya    = original_image2Texture('image/hisya.PNG')
ousyo    = original_image2Texture('image/ousyo.PNG')
gyokusyo = original_image2Texture('image/gyokusyo.PNG')
tokin    = original_image2Texture('image/tokin.PNG')
narikei  = original_image2Texture('image/narikei.PNG')
narikyo  = original_image2Texture('image/narikyo.PNG')
ryuma    = original_image2Texture('image/ryuma.PNG')
ryuou    = original_image2Texture('image/ryuou.PNG')

#name each square
squares = {}
for row in range(9):
	for column in range(9):
		squares.update({str(row + 1) +  ',' + str(column + 1):
			         coordinate_on_board(square_size * (row + 0.5),
																   square_size * (column + 0.5))})

if __name__ == '__main__':
	run(shogi(), PORTRAIT, show_fps = True)