def function():

    try: # try to open the file
        with open("filename.txt","r") as file:
            for i in (content := file.readlines()):
                print(i,end="") 

    except Exception as e: # return error if something goes wrong or try block fail
        return f"\nERROR: {e}"
    
    else: # runs if no exception or error
        return "\nCode Successfully Run"

    finally: # always runs
        print("\nExecution finished")

print(function())