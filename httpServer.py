#!coding=UTF-8

# ------------------------------------------------------------------
# Title        Web入口
# Author    chenqiwei
# Created   2021/12/24
# Update    2022/01/12
# ------------------------------------------------------------------

from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse
import io,shutil,json,os,re,urllib.parse

class MyHttpHandler(BaseHTTPRequestHandler):

    def writeJson(self,code,content='',message=''):
        '''输出json内容'''
        if content=='':
            content={}
        if message=='' and code == 200:
            message='请求成功'
        elif message=='' and code == 500:
            message='服务器异常'
        outContent = json.dumps({"code":code,"data":content,"message":message},ensure_ascii=False).encode("UTF-8") #定义json结构
        f = io.BytesIO()     
        f.write(outContent)     
        f.seek(0)     
        self.send_response(code)     
        self.send_header("Content-type", "application/json; charset=UTF-8")     
        self.send_header("Content-Length", str(len(outContent)))     
        self.end_headers()     
        shutil.copyfileobj(f,self.wfile)

    def notFound(self):
        '''输出404'''
        f = open(os.getcwd()+'readme.json','rb')
        readme=f.read()
        f.close()
        self.writeJson(404,json.loads(readme),'路径不存在')

    def getPostValue(self,data,key):
        '''获取请求头的post值'''
        if self.command!='POST':
            return ''
        contentInfo = data.decode()
        reCon = re.findall(r'Content-Disposition: form-data; name="(.*?)"(.*?)\r\n\r\n(.*?)\r\n', contentInfo, re.DOTALL)
        content=''
        for name in reCon:
            if key== name[0]:
                content=name[2]
                break
        return content

    def do_GET(self): 
        self.notFound()

    def do_POST(self): 
        req_data = self.rfile.read(int(self.headers['content-length'])) #获取from-data
        path=urlparse(self.path).path
        ##################
        # RSA+BASE64 加解密 #
        ##################
        if (path=="/rsaBase64/encode" or path=="/rsaBase64/decode") and os.path.exists('./lib/rsaBase64.py'):
            if path=="/rsaBase64/encode":
                keyType='pubkey'
            else:
                keyType='privkey'
            from lib.rsaBase64 import rsaBase64
            postContent=self.getPostValue(req_data,'content')
            postUrlcode=self.getPostValue(req_data,'urlencode')
            postKey=self.getPostValue(req_data,keyType)
            if postContent!='' and postKey!='':
                if keyType=="pubkey":
                    if postUrlcode=='get':
                        content= rsaBase64.encode(postContent,postKey) #加密
                        content=urllib.parse.quote(content,'utf-8')
                        content=urllib.parse.quote(content,'utf-8')#云盟专用，双重url编码
                    elif postUrlcode=='true':
                        postContent=urllib.parse.quote(postContent,'utf-8')
                    else:
                        content= rsaBase64.encode(postContent,postKey) #加密
                    code=200
                    message='请求成功'
                    content= {"content":content} 
                elif keyType=="privkey":
                    postContent=urllib.parse.unquote(postContent,'utf-8') #url解码，解决get传参产生的url编码
                    if postUrlcode=='get':
                        postContent=urllib.parse.unquote(postContent,'utf-8')  #云盟专用，双重url解码
                    try:
                        content=urllib.parse.unquote(rsaBase64.decode(postContent,postKey)) #解密后，先url解码
                    except:
                        code=500
                        content=''
                        message='解密失败'
                    else:
                        try:
                            content=json.loads(content)
                        finally:
                            code=200
                            message='请求成功'
                            content= {"content":content} 
            else:
                content=''
                message='请检查参数是否完整 [content 要加密的字符] ['+keyType+' 符合RSA PKCS#8 格式的'+keyType+']'
                code=500
            self.writeJson(code,content,message) #返回json格式
        else:
            self.notFound()

port=8808
httpd=HTTPServer(('',port),MyHttpHandler)     
print("Server started on 0.0.0.0,port "+str(port)+".....")     
httpd.serve_forever()