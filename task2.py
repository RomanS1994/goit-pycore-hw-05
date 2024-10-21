from typing import Callable
import re




def generator_numbers(text: str):
    '''
    A function to create a generator

    Parameters:  text(str) text with information about the salary
    '''
    pattern = r'\d+\.\d+|\d+'  
    for el in re.findall(pattern, text):
        yield float(el)  


def sum_profit(text: str, func: Callable):
    '''
    Function for summing numbers

    Parameters: 
    text (str): The input text to analyze
    func (Callable): The function that generates numbers

    Returns:
    float: The sum of all numbers generated from the text
    '''

    return sum(func(text))






text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


