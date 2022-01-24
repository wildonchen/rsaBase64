from urllib.parse import urlparse
import json
def rsaBase64Page(self):
    req_data = self.rfile.read(int(self.headers['content-length'])) #获取from-data
    path=urlparse(self.path).path
    if path=="/rsaBase64/encode":
        keyType='pubkey'
    else:
        keyType='privkey'
    from lib.rsaBase64 import rsaBase64
    postContent=self.getPostValue(req_data,'content')
    postKey=self.getPostValue(req_data,keyType)
    if postContent!='' and postKey!='':
        if path=="/rsaBase64/encode":
            content= rsaBase64.encode(postContent,postKey) #获取加密字符
            code=200
        else:
            content= rsaBase64.decode(postContent,postKey) #获取解密字符
            code=200
    else:
        content='请检查参数是否完整 [content 要加密的字符] ['+keyType+' 符合RSA规则的加密公钥]'
        code=500
    encoded = json.dumps({"code":code,"content": content}).encode("UTF-8") #定义json结构
    self.writeJson(encoded) #返回json格式