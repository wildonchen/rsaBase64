# rsaBase64
使用python 编写的 rsaBase64 加解密接口，使用公钥加密，私钥解密。公钥和私钥需要符合 RSA PKCS#8 格式

## 依赖

pip3 install pycryptodome  



## 接口

### /rsaBase64/encode

RSA+BASE64 加密

请求方式：POST（form-data）

| 参数      | 必填 | 值        | 说明                                                         |
| --------- | ---- | --------- | ------------------------------------------------------------ |
| content   | 是   | str       | 需要加密的内容                                               |
| pubkey    | 是   | str       | 加密的公钥                                                   |
| urlencode | 否   | true\|get | true: 将内容进行url编码后再进行加密，get:将加密后的内容进行url编码 |

### /rsaBase64/decode

RSA+BASE64 解密

请求方式：POST（form-data）

| 参数    | 必填 | 值   | 说明         |
| ------- | ---- | ---- | ------------ |
| content | 是   | str  | 待解密的内容 |
| privkey | 是   | str  | 解密的私钥   |



## 使用

### Windows

在目录下执行 start.bat，默认端口 8808

### Linux

在目录下执行 ./start.sh，默认端口 8808

停止执行 ./stop.sh



