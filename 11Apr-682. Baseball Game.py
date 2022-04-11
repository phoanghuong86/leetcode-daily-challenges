class Solution:
	def calPoints(self, ops: List[str]) -> int:
		result = []
		sum_ = 0
		for value in ops:
			if value == 'C':
				sum_ -= result.pop()
				continue
			elif value == 'D':
				result.append(result[-1]*2)
			elif value == '+':
				result.append(result[-1]+result[-2])
			else:
				result.append(int(value))
			sum_ += result[-1]
		return sum_
