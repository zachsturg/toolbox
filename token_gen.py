#call generate_token to generate a coresense token
import requests
import hmac
import time
import base64

#remove trailing '=' and replace +, /.  To be used after b64 encoding credentials
def url_safe(b):
    '''Returns bytes cleaned of +, /, and =.'''
    b=b.decode().replace('+','-')
    b=b.replace('/', '-')
    b=b.replace('=','').encode()
    return b


def generate_token(myUserId, mySignKey, token_duration = 600):

    token_headers={'alg':'HS256'}

    #change 'exp' as needed.  It's the token expiration time stamp.  Can be up to
    #str(time()+3600*24)[:10]
    params={'sub':myUserId,'exp': str(time.time()+token_duration)[:10]}

    t1=base64.b64encode(json.dumps(token_headers).encode())
    t2=base64.b64encode(json.dumps(params).encode())
    message = t1 +b'.'+t2
    message=url_safe(message)

    #generate signature for that message, based on the key
    sig=hmac.new(mySignKey.encode(), message,'sha256')

    #concatenate signature in string form after base64 encoding it.
    token= message.decode() +'.' + base64.b64encode(sig.digest()).decode()

    #remove bad characters (commented after I noticed CREST likes those bad charact)
    #token =url_safe(token.encode()).decode()

    return token

def main():
    try:
        from charset_normalizer import __version__ as charset_normalizer_version
    except ImportError:
        charset_normalizer_version = None

    if __name__ == '__main__':
        main()
