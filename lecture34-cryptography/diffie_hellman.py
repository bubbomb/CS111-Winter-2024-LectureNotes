import random

def diffie_hellman_exchange(p=5, g=3):

    print('-------------------------------------------')
    alice_secret = random.randint(1,10000)
    bob_secret = random.randint(1, 10000)

    alice_public = (g ** alice_secret) % p
    bob_public = (g ** bob_secret) % p

    print('ALICE PUBLIC KEY: ', alice_public)
    print('BOB PUBLIC KEY: ', bob_public)

    alice_shared_secret = (bob_public ** alice_secret) % p
    bob_shared_secret = (alice_public ** bob_secret) % p

    print(bob_shared_secret == alice_shared_secret)
    assert bob_shared_secret == alice_shared_secret



diffie_hellman_exchange()
diffie_hellman_exchange()
diffie_hellman_exchange(p=23)
diffie_hellman_exchange(p=23)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=137, g=101)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
diffie_hellman_exchange(p=7919, g=2437)
