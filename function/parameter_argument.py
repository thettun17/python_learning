def greet_user(first_name, last_name): #parameter
    print(f"Hello {first_name} {last_name}")


# ======== Positional Argument ==========
greet_user("Thet", "Tun") #argument 

#========= Keyword Argument ========
greet_user(last_name="Tun", first_name="Thet") 


# Pure Function
# Pure function ဆိုတာက same input ကိုဘယ်နှစ်ခါပဲ ပေးပေး same result ကိုပဲပြန်ပေးပါတယ်

# Higher Order Function
# Higher Order Function ဆိုတာက Function တစ်ခုကို Parameter တစ်ခုအနေနဲ့လက်ခံတာ