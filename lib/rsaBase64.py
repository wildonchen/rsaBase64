#!coding=UTF-8

# ------------------------------------------------------------------
# Title        RSA+BASE64加解密方法
# Author    chenqiwei
# Created   2021/12/24
# Update    2022/01/12
# pip3 install pycryptodome  
# ------------------------------------------------------------------

import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto import Random

class rsaBase64:
    def encode(bizcontent,publicKey):
        rsakey = RSA.importKey(base64.b64decode(publicKey))
        bizcontent = bytes(bizcontent, encoding="utf-8")
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        length = len(bizcontent)
        default_length = 117
        offset = 0
        res = bytes()
        while length - offset > 0:
            if length - offset > default_length:
                _res = cipher.encrypt(bizcontent[offset:offset + default_length])
            else:
                _res = cipher.encrypt(bizcontent[offset:])
            offset += default_length
            res += _res
        return base64.b64encode(res).decode('utf-8')

    def decode(bizcontent, privateKey):
        MAX_DECRYPT_BLOCK = 256
        bizcontent = base64.b64decode(bytes(bizcontent, encoding='utf-8'))
        privateKey = base64.b64decode(bytes(privateKey, encoding='utf-8'))
        privateKey = RSA.import_key(privateKey)
        dsize = SHA256.digest_size
        sentinel = Random.new().read(15 + dsize)
        cipher = Cipher_pkcs1_v1_5.new(privateKey)
        input_len = len(bizcontent)
        off_set = 0
        _bizcontent = bytes()
        while input_len - off_set > 0:
            if input_len - off_set > MAX_DECRYPT_BLOCK:
                _cache = cipher.decrypt(bizcontent[off_set:MAX_DECRYPT_BLOCK + off_set], sentinel)
            else:
                _cache = cipher.decrypt(bizcontent[off_set:], sentinel)
            off_set += MAX_DECRYPT_BLOCK
            _bizcontent += _cache
        return _bizcontent.decode('utf-8')

if __name__ == "__main__":
    postPubkey='jvthTjq+M/iQ5FNDe+wBXRry/DxUtj/vVUT9EhYha1pyUioIhUEwi/3JKKzDsMnZpvKn8FM58i77Qx93OqWEBLv8KpQ07GPafpXJmmgJtcyj+Bgob7IAICutV69JVaQm/qejiALVREWB5RfGRNgZKTuVDvhqn3KsIYCZcxBBsvJtrUbicUacbad2s4G+WbmkOyVamtXwczk/H65YYHx18q9dqBzPHbBwnoGMFzrbrBsDU+mUL9bLT0dpfRQUl7r+yWLjxwNTYjOATAudenP2gl4zWOkP3w/lx9OYbWkPCn0yFfaqJ49teNyRyasYBhfGgFvVfI3rRORjTiBbIL+zsQ=='
    postPrivkey='MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALnzUD3QV1bruXLxzLgmEXwQpTHiSl+HTDKv1Ub5apTkqNfUABNounQAk/HW0CTJcJDDomJ7GIkvGh2bj03TR3e4GRXJH4W8f/zRJML+MUzrtX/zsN/c2UEEPbs7KdujqLcG5zm5IR3CAetpJFqQrVh8IEQLyZ7xujKZjdisVku/AgMBAAECgYAwX6y7N+zQrugCkAa6zSR1Svs+m+jPKypWcUmhehcQ/t8xrnQKmI8QyGm0Wzawqzq+XjZrOiyq23cGxsYj79fCSqazlfEtl36WZL6N7LyPCiI7W7HEjTzkNACKouTTwzg2vsAIbCQCUBmYTet5Be2r0nupJdsTuy31OY3+HseIGQJBAOLHVlpa6KyhJLLybO9Zc59gfEVu9R4zomnQi6NSZAmTfhfa1JL/CHm4aFp5FImxCqBtxY6ErTDgsY33VZPdVj0CQQDR6TDlPoRGuDX9eoF+WzkhyfpjHilIzF432nHGbY1+bLQXgO2bjFdhEG6J0Jpg6xHtyKHu6yhYkkOnblXbcIWrAkEAgArCw/NuSgIWIX9laGLeOI+WuvFiLrJCsnIQVZ+wYgPH/xoMSg77LxaivOp+YRv3/wrbr5NT4jQLrDeJNxqSlQJAHxGIryWFpoH1W8MaD32pAxtF+A2qxp+ZAmNOm7PzUVb9gM0QXglzlWY9NiCt+NJSIQOlFBuyKQndAZcPFh+daQJBANbD7Kpo3zTjEp5TNexmETJI5khnhZaTnp7hXKyJBcxLTpi2zYFirtwkjKUo/aApgv8DXuZjmLI0JjXB30kqgA8='

    str=rsaBase64.encode("hello",postPubkey)
    print("rsaEncrypt: "+str)

    content = rsaBase64.decode(str, postPrivkey)
    print("rsaDecrypt: "+content)
