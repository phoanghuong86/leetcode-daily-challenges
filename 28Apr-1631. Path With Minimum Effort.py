class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		num_rows = len(heights)
		num_cols = len(heights[0])
		move_dirs = [(0,1), (1,0), (0,-1), (-1,0)]

		def bfs(cost):
			queue = [(0,0)]
			visited = set()
			visited.add((0,0))
			while len(queue)>0:
				pop_item = queue.pop(0)
				y, x = pop_item
				if y==num_rows-1 and x==num_cols-1:
					return True
				for move_dir in move_dirs:
					ty, tx = move_dir
					dy = y+ty
					dx = x+tx
					if 0<=dy<num_rows and 0<=dx<num_cols and (dy, dx) not in visited: 
						if abs(heights[dy][dx]-heights[y][x])<=cost: 
							queue.append((dy,dx))
							visited.add((dy,dx))
			return False                

		left, right = 0, 10**6+1
		while left<right: 
			mid = left + (right-left)//2
			if bfs(mid):
				right = mid 
			else:
				left = mid+1
		return left
