# import time libarary
import time

# Define a function with parameters annotated with their types and docstring defined for the function for better readability
def get_welcome_msg(employee_name: str, role: str) -> str:
    """
      This function returns a welcome message for a new employee 
      
      Args:
      employee_name (str): The name of the employee
      role (str): The role of the employee
      
      Returns:
      str: A welcome message for the new employee
      """
    # time.sleep(3)
    welcome_message = f"Welcome {employee_name}! We're excited to have you on this role: {role}. Your joining time is: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    return welcome_message

"""
Why use functions:

* A function accepts input and returns output
* Team collaboration
* Reuse of code
* External libraries
* A function can use other functions
* A function can be used in multiple files
* A function can be used in multiple projects
* A function can be used in multiple teams
* A function can have arguments and return values annotated with their types
* A function can have a docstring to describe what it does

"""






