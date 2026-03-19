def say(): # This block runs only when this file is imported.
    return "Hello World!"

# from Main_Guard import say
# print(say())

if __name__ =="__main__": # This block runs only when this file is executed directly. It will NOT run if this file is imported.
    print("\"Main_Guard.py\" in runing!")
    print(say())