import os, requests, json, sys
from time import sleep
from huepy import *

__version__ = "1.3.5"

API = "https://lookup.binlist.net/"

def Bin_Info():


    def banner():
        print(purple("""
                        :::.                      
                    .XXr;;;rrX7                   
                  iWa,        :@S                 
                 rM   .i;;i;;.  Mi                
                 @   aXi:,,,iZ  .M                
                i2  X.       i:  @i               
                a  ir   :r.   S  ,M               
               Xi  X.MM2. ,2MM8i  2Z              
              ;S  a;rXMMM @MMSiB.  Xr             
             ,8  2i.;:; : : ii;72   i,           V     V   I   T T T T T   T T T T T   O O O
             B .2      ,   ,     X.   ,           V   V    I       T           T      O     O
            0:.SX ;ai, 7   :: iS. 8i  i;           V V     I       T           T      O     O
           2X 7 rr.iXi,:rXX;,:r;i;iiX  2r           V      I       T           T       O O O
          iW X   :;,.7.. ..,.;i;;:  iX  M.        
          M X      .iiX::i::S7S,     X. Br        
          M ,       ;,XX7SXXX,,      S  M         
          S0        i :     : ..    S  Z2         
           @M:   .:i  ,:   :   ;;;::iiM0          
        :72XXBW88SXXi  :i..;X2SXXrSXrrS72Xi       
     :7ri:       r:i;r;,  ,07, ..:;      ,ii.     
     B                 ,;X2                 ri    
    .a                   X                  :2  
            Extraer informacion de un bin \n"""))

    
    def clean():

        if os.name == 'nt':

            os.system('cls')

        else:

            os.system('clear')

    def main():

        clean() 
        banner()
        
        try:
            
            BIN = input(red("   BIN > "))
            clean(); banner()

            data = requests.get(API+BIN).json()
            sys.stdout.flush()

            print(info(yellow("BIN INFORMATION " +red(BIN + "\n"))))
            sleep(0.7)
            print(good(red("[Country]: " +yellow(data['country']['name']))))
            sleep(0.7)
            print(good(red("[Sheme]: " +yellow(data['scheme']))))
            sleep(0.7)
            print(good(red("[Type]: " +yellow(data['type']))))
            sleep(0.7)
            print(good(red("[Brand]: " +yellow(data['brand']))))
            sleep(0.7)
            print(good(red("[Bank Name]: " +yellow(data['bank']['name']))))
            sleep(0.7)
            print(good(red("[Latitude]: " +yellow(data['country']['latitude']))))
            sleep(0.7)
            print(good(red("[Longitude]: " +yellow(data['country']['longitude']))))
            sleep(0.7)
            print(good(red("[Bank URL]: " +yellow(data['bank']['url']))))
            sleep(0.7)
            print(good(red("[Bank Phone]: " +yellow(data['bank']['phone']))))
            sleep(0.7)
            print(good(red("[Bank City]: " +yellow(data['bank']['city'] + "\n"))))

        except:

            print(bad(yellow("An Error Ocurred...")))
            exit()

    main()


if __name__ == "__main__":

    print(info(lightred(("An Error Ocurred..."))))

else:

    Bin_Info()