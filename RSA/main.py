from rsa import RSA
from dh import DiffieHelman

if __name__ == "__main__":
    p = 6142
    q = 5311
    message = 'Neque porro quisquam est qui dolorem ipsum quia...'
    rsa = RSA(p, q)
    print('\n\n---------------------RSA---------------------------------')
    print(f"p: {rsa.p}, q: {rsa.q}, n: {rsa.n}, phi: {rsa.phi}, e: {rsa.e}, d: {rsa.d}")
    print('---------------------ENCRYPT/DECRYPT---------------------')
    print(f"Message: {message}")
    rsa_encrypted = rsa.encrypt(message)
    print(f"Encrypted message (first 3 characters): {rsa_encrypted[:3]}...")
    rsa_decrypted = rsa.decrypt(rsa_encrypted)
    print(f"Decrypted message: {rsa_decrypted}")
    print('---------------------DiffieHelman------------------------')
    dh = DiffieHelman(p)
    print(f"p: {dh.p}, g: {dh.g},\nPerson A private key: {dh.x}, Person B private key: {dh.y},\nX: {dh.X}, Y: {dh.Y}, \nPerson A session key: {dh.k_A}, Person B session key: {dh.k_B}")
    print('---------------------END---------------------------------\n')