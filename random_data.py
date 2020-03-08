import random

product_name = ["Apple_1", "Microsoft_2", "Amazon_3", "Alphabet_4", "Berkshire_5", "Facebook_6", "Alibaba_7", "Tencent_8",
                "JPMorgan_9", "JohnsonandJohnson_10", "Visa_11", "ExxonMobil_12", "ICBC_13", "Walmart_14", "BankOfAmerica_15",
                "Nestle_16", "Samsung_17", "Procter_18", "Royal_Dutch_Shell_19", "Intel_20", "Cisco_21", "Mastercard_22",
                "Verizon_23", "Walt_Disney_24", "AT&T_25", "Chevron_26", "Home_Depot_27", "Nike_28", "Fargo_29", "Boeing_30",
                "CocaCola_31", "Oracle_32", "Toyota_33", "Novartis_34", "HSBC_35"]
buy_sell = ["1","2"]
force_orders = ["Day","Good Till Cancel (GTC)","At the opening (OPG)","Immediate or Cancel (IOC)", "Fill or kill (FOK)",
                "Good Till Crossing (GTX)", "Good Till Date"]
order_types = ["Market","Limit","Stop","Stop limit","Market on close"]
stocks = ["FUT","OPT","CS"]

x = int(input("Enter the number : "))

stringToWrite = ""
def random_sentence():
    """Creates random and return sentences."""
    return ("FIX.4.2|""D|""{}|{}|{}|{}|{}|{}|{}|{}"
                .format(product_name[random.randint(0,34)]
                    , buy_sell[random.randint(0,1)]
                    , random.randrange(0,1000,1)
                    , order_types[random.randint(0,4)]
                    , force_orders[random.randint(0,6)]
                    , stocks[random.randint(0,2)]
                    , random.randint(0,10)
                    , random.randint(0,200)))

# prints random sentences
for sentence in list(map(lambda x: random_sentence(), range(0, x))):
     file = open("C:\\Users\\prave\\OneDrive\\Desktop\\Python\\FIX_Messages.txt","w")
     stringToWrite += sentence + "\n"
     file.writelines(stringToWrite)
     file.close()
