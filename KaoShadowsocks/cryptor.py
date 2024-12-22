from Crypto.Cipher import AES, ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt_data_chacha20_poly1305(data, key):
    # 生成一个随机的16字节nonce
    nonce = get_random_bytes(16)

    # 创建ChaCha20-Poly1305加密器对象
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)

    # 加密数据
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # 返回加密后的数据、nonce和认证标签
    return ciphertext, nonce, tag


def decrypt_data_chacha20_poly1305(ciphertext, key, nonce, tag):
    # 创建ChaCha20-Poly1305解密器对象
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)

    # 解密数据
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # 返回解密后的数据
    return plaintext


def encrypt_data_aes256(data, key):
    # 生成一个随机的Initialization Vector (IV)
    iv = get_random_bytes(16)

    # 创建一个AES加密器对象
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 对数据进行填充
    padded_data = pad(data, AES.block_size)

    # 使用AES加密器加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 返回加密后的数据和IV
    return encrypted_data, iv


def decrypt_data_aes256(encrypted_data, key, iv):
    # 创建一个AES解密器对象
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 使用AES解密器解密数据
    decrypted_data = cipher.decrypt(encrypted_data)

    # 对解密后的数据进行反填充
    unpadded_data = unpad(decrypted_data, AES.block_size)

    # 返回解密后的数据
    return unpadded_data

# # 32字节的AES密钥（256位）
# key = b'0123456789abcdef0123456789abcdef'
#
# # 要加密的字节数据
# data_to_encrypt = b'This is a secret message.'
#
# # 加密数据
# encrypted_data, iv = encrypt_data(data_to_encrypt, key)
# print("Encrypted Data:", encrypted_data)
#
# # 解密数据
# decrypted_data = decrypt_data(encrypted_data, key, iv)
# print("Decrypted Data:", decrypted_data.decode('utf-8'))
