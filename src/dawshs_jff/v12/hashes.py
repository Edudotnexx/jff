import uuid
from hashlib import md5

signature = b"0\x82\x03z0\x82\x02b\x02\x01\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000\x81\x821\x100\x0e\x06\x03U\x04\x03\x0c\x07MahsaNG1\x150\x13\x06\x03U\x04\x0b\x0c\x0cMahsaNet Dev1\x160\x14\x06\x03U\x04\n\x0c\rMahsaNet Inc.1\x110\x0f\x06\x03U\x04\x07\x0c\x08Dortmund1\x1f0\x1d\x06\x03U\x04\x08\x0c\x16North Rhine-Westphalia1\x0b0\t\x06\x03U\x04\x06\x13\x02DE0\x1e\x17\r230831211522Z\x17\r480824211522Z0\x81\x821\x100\x0e\x06\x03U\x04\x03\x0c\x07MahsaNG1\x150\x13\x06\x03U\x04\x0b\x0c\x0cMahsaNet Dev1\x160\x14\x06\x03U\x04\n\x0c\rMahsaNet Inc.1\x110\x0f\x06\x03U\x04\x07\x0c\x08Dortmund1\x1f0\x1d\x06\x03U\x04\x08\x0c\x16North Rhine-Westphalia1\x0b0\t\x06\x03U\x04\x06\x13\x02DE0\x82\x01\"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xc1\xd2O#|oX\x97\xb7\xff\t\xa7~\xa1\xf0\x93\xa0\xd5\x99\xc7b\xff\xd2\xee\x17Q\x1d\x00\xaf\xe7\xefP\x067G\n\x02\xd9\xf0\xec!\xbex\xbd\x8cd\xb47\xc5\x80\xb0B\xdeh\x19\xcc\xccl\xcf\x04\x89\x04\xaa\xe27\xd2\x12<|_\xad\x9c\x04h\x02\xfd\x87\xfb#\xddh\x9dSD\xea\"x\xb9\xb1&\x1bP\xe6\x18\xfb\xa1\xc3]\x85\xfa>\x98\xa1\xccq\xee\xc2\n\xbe\xeeu\x94Rb\xfb\xde]\xc9\xba'9@\x198(B\xcax\xe6\xb0A\xb5R\xe6\xb6a\xce\x06\x03!/B\x19O\xe8\xf2\xe3\xff\x91\x06,\xb1\xbc!\xf1\xb1\xe4\xaa~\x03\xd2\xef4\x1b\xd0\x88\r\xb4\xcd\x9b\xb7I0\xae\x16\x03\xaa\xb54\x89\x984O\xc8P*\xa3~M\xf3\xe8\xd2\xdfEQwd\xea9<Xu8\xf6\xc3%\xd6\xac\x96\xad\x0b?\x10\x16\x0bm\xd4\xc2\xf6\xc7X\x8d\xf00\xc6\xcfX\r\x05%\x19`b\x01\xa1\x83\xf6`\xd5\xe2H\xd8\xdf\x80G\xcfC*j)\xa1\x12\x9f\x80+\x01\x02\x03\x01\x00\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00NY<\xfa\xdaX\xfai%#T,Dd\xe0\xfd\xfc~\x95n\x95\x07_d8\xd4\x08!KI<1/\xb3\x9fe\x97w\xd7s%c\x85}7W\xf7\x8c[\xbf\x14y\x189\xb3L}\x96\xd4\xbc\xb1\x8f_\xf4\xc0C\x0b\xbdu\xcd\xdeEc3\xc4\xa7\xb6\xc7g_\x0e;\xa9?\x1cBxK\xb7\x9e'\x1e\x85\x12\xf0\xf3\xd5\xa6/w\xfd\xc9\x1d*\xbb\x95x\xc9\t\xf8X\xc1\x95hAavf '\x18\x9a$h\x81g\xc4\xc9\xb8\xb6[\xeb\xda\xb8\xda\xe6~\xf9s\xd4]\xd3\x01Jq\xdd\xf3\x1f\xda\xb4\t\xf0\xeaU\x18Xr\x93\xb0/\xacS\x99\xf1M@k\x86[E9\xa6&\xb4A\x1f1\xf9\x1d(\x87\xea8;\xf61x\xa5\xd9\xb6\xa3\xa6\xaf\xa4\x80\xc9\xe9F2.|d=\xe4\xb8\x17\x1f\x85=\xa2D\xb6=\x92\xb6\xc3H\xeace0\xbeg\xe5\xeb\x0e@\xb2\x0c0\x02R\xfb]\x97\xa9<I\xd6X\x11\xd2\xd3\x1b\xff'\x8e\x13A\xbf\xf2@+\xc5bZ"
signature_md5 = "d63b2eabf70b5fefc6ac38be9923bd1b"
app_name = "com.MahsaNet.MahsaNG"


def f_g(seed: str | bytes):
    if isinstance(seed, str):
        input_bytes = seed.encode()
    else:
        input_bytes = seed
    message_digest = md5(input_bytes)
    res = message_digest.hexdigest()
    while len(res) < 32:
        res = "0" + res
    return res


def f_e():
    return signature_md5 or f_g(signature)


def f_b(string: str):
    return f_g(f_g(app_name) + f_e()[4:12] + string)

def f_d(str0, str2, str3, str4, str5):
    return f_g(f_g(str0)[2:27] + str2 + str4 + f_g(str3)[3:25] + str2 + str5)[0:20]


def i_o(ip: str, timestamp: str):
    return f_g(
        ip
        + f_g(app_name)[10:18]
        + f_e()[18:29]
        + timestamp
        + f_b(timestamp)
    )[10:20]

def g_a():
    return str(uuid.uuid4())


def g_h():
    f1580a = 16
    return g_l(f_g(g_a()), f1580a)

def g_g():
    f1581b = 8
    return g_l(f_g(g_a()), f1581b)

def g_i(str0):
    return g_l(str0, 3)

def g_j(str0):
    return str0[3:]


def g_l(s: str, i2: int):
    return s[:i2]

def j_i_q():
    return f_g("jfdvgjk5643790jgvdhnmddhssnyyy9521gfnbvfty")[4:23]

def j_i_a(str1, str2, str3):
    g2 = f_g(g_a())
    l2 = g_l(g2, 7)
    substring = g2[7:17]
    substring2 = g2[17:24]
    str4 = l2 + substring + substring2
    str5 = str4[5:9] + str4[14:18] + str4[20:22]
    i2 = g_i(str2)
    j2 = g_j(str2)
    l3 = g_l(str1, 5)
    substring3 = str1[5:]
    d2 = f_d(str1, str5, str3, i2, j2)
    return l2 + l3 + d2[0:12] + j2 + substring + d2[12:20] + i2 + substring3 + substring2

def generate_hash(ip: str, timestamp: str):
    return i_o(ip, timestamp)


def generate_token():
    h2 = g_h()
    g2 = g_g()
    return j_i_a(h2, g2, j_i_q())
