from scene import *
from PIL import Image, ImageDraw
import ui, io

screen_size = get_screen_size()
#I want the board size to be a multiple of 9 because the shogi board is 9 × 9 square
board_size  = int(screen_size.x * 0.9) // 9 * 9
square_size = int(board_size / 9)
piece_size  = int(square_size * 0.9)

def original_image2Texture(img_name, size_x, size_y):
	img = Image.open(img_name)
	img = img.resize((size_x, size_y))
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
		
class shogi (Scene):
	def setup(self):
		self.rootNode = Node(parent = self)	
		self.background_color = '#f9ffec'
		
		#draw shogi board
		#To add 1 to board_size to draw the right and bottom lines
		im = Image.new('RGB', (board_size + 1, board_size + 1), (255, 255, 255))
		draw = ImageDraw.Draw(im)
		for x in range(9):
			for y in range(9):
				draw.rectangle((square_size * x, 			 square_size * y, 
											  square_size * (x + 1), square_size * (y + 1)), 
												fill = (190, 160, 150), outline = (0, 0, 0))
		board = convert_PILImage2Texture(im)
		self.board = SpriteNode(board, position=self.size/2)
		self.rootNode.add_child(self.board)
		
		#add all pieces
		hu2 = original_image2Texture('hu.PNG', piece_size, piece_size)
		new_hu = piece(hu2, square_size * 8.5, square_size * 8.5)
		self.rootNode.add_child(new_hu)
		
		#hu = Image.open('hu.PNG')
		#hu = hu.resize((int(square_size * 0.9), int(square_size * 0.9)))
		#hu = convert_PILImage2Texture(hu)
		#self.test_module = SpriteNode(hu, z_position = 1)
		#self.test_module.position = \
		#	coordinate_on_board(square_size * 2.5, 
		#										  square_size * 2.5)
		#self.rootNode.add_child(self.test_module)
		#self.test_module.previous_position = self.test_module.position
		
		#後で消す
		#hu2 = piece(hu, square_size * 2.5, square_size * 8.5)
		#self.rootNode.add_child(hu2)
		#hu3 = piece(hu, square_size * 1.5, square_size * 4.5)
		#self.rootNode.add_child(hu3)
		#hu4 = piece(hu, square_size * 6.5, square_size * 2.5)
		#self.rootNode.add_child(hu4)
		#hu5 = piece(hu, square_size * 3.5, square_size * 7.5)
		#self.rootNode.add_child(hu5)
		
	def touch_began(self, touch):
		x, y = touch.location
		
	def touch_moved(self, touch):
		x, y = touch.location
		move_action = Action.move_to(x, y, 0.1, TIMING_BOUNCE_OUT)
		self.test_module.run_action(move_action)
		
	def touch_ended(self, touch):
		x, y = touch.location
		if x < 300:
			x, y = self.test_module.previous_position
			move_action = Action.move_to(x, y, 0.1, TIMING_BOUNCE_OUT)
			self.test_module.run_action(move_action)
		else:
			self.test_module.previous_position = x, y
						
class piece (SpriteNode):
	def __init__(self, img, x, y, ):
		SpriteNode.__init__(self, img)
		self.position = coordinate_on_board(x, y)
	
if __name__ == '__main__':
	run(shogi(), PORTRAIT, show_fps = True)
