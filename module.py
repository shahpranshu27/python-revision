def myFunc():
    print("Hello from myFunc!")
    
if __name__ == "__main__":
    print("module.py is being run directly")
    myFunc()
    print(__name__) # It prints '__main__' when directly run, and 'module' when imported

'''
If the module is imported, the code inside the if block will not execute.
'''