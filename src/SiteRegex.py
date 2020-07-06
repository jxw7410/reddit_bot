import re 

class SiteRegex:
  @classmethod 
  def is_amazon_product_url(cls, url):
    regex = r'/.*amazon\.com.*\/(dp|gp)\/(product\/)?(\w{10}).*/'
    return len(re.findall(regex, url)) > 0
