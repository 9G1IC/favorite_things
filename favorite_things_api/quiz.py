
from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdcOABOYfrzBAeKTF-_N1h2TjqxDUfaE8VCp-afiPZh1XEbyelTq8tu_yonLIEo-Ig0aMjBmQKa39cyZ-Qtrsa3aYYDG-GL0Cl18MsmMQEl6fQMIQbs22fCUn6FB5kPe-pGbMYzUO_C-R9wrdhwUqKCCkV-F6d8Vcl2qGHZ5HNcalp390='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
