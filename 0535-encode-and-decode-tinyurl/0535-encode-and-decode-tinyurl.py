class Codec:

    def __init__(self):
        self.url_map={}
        self.base_url="http://tinyurl.com"
        self.key_length=6
    def generateKey(self):
        characters=string.ascii_letters +string.digits
        print(string.ascii_letters,string.digits)
        return "".join(random.choice(characters) for _ in range(self.key_length))



    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key=self.generateKey()
        while key in self.url_map:
            key=self.generate_key()
        self.url_map[key]=longUrl
        return self.base_url+key


 
       

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # print(self.encodeMap)
        # print(self.decodeMap)
        # return self.decodeMap[shortUrl]

        key=shortUrl[len(self.base_url):]
        return self.url_map.get(key)
       

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))