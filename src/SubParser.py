class SubParser:
  @classmethod
  def parse(cls, url):
    return cls(url).parse 

  # TODO extract html from url, and check if link exists in post
  def parse(self, url):
    print(url)