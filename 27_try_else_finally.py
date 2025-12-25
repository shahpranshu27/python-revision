'''
When try-except blocks are run without errors, the else block is executed.
This is useful for code that should only run if no exceptions were raised in the try block.
'''

'''
finally block is always executed, regardless of whether an exception occurred or not.
'''

try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except ValueError:
    print("That's not a valid number!")

else:
    print("Thank you for entering a valid number.")
    
finally:
    print("Execution completed.")