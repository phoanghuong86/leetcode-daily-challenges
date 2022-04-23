class Codec:

	def encode(self, longUrl: str) -> str:
		"""Encodes a URL to a shortened URL.
		"""
		self.url_list = longUrl.split('/')
		encode_token = 0
		for ch in self.url_list[-1]:
			encode_token += ord(ch)
		res_list = self.url_list[:2] + [self.url_list[-1]] + [str(encode_token)]
		return '/'.join(res_list)    


	def decode(self, shortUrl: str) -> str:
		"""Decodes a shortened URL to its original URL.
		"""
		url_keyword = shortUrl.split('/')[-2]
		res = self.url_list[:-1] + [url_keyword]
		return '/'.join(res)    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
