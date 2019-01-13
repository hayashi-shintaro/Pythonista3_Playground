from scene import *

class shogi (Scene):
	def setup(self):
		self.shogi_board = Node(parent = self)	
		self.background_color = '#f9ffec'
		tile = SpriteNode('plc:Wood_Block', position = (70, 1000))
		self.shogi_board.add_child(tile)
		
		self.test_module = SpriteNode('iob:social_apple_outline_256', z_position = 1)
		self.test_module.position = (70, 1000)
		self.shogi_board.add_child(self.test_module)
		self.test_module.previous_position = self.test_module.position
		
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
			
#class piece (SpriteNode):
#	def setup(self):
	
#class oshou(piece):
if __name__ == '__main__':
	run(shogi(), PORTRAIT, show_fps = True)
