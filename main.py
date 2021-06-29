import timeit
import logging

def salary_calculator(salary):

    print("----Function starts the execution:------")
    try:
        salary = float(salary)
        if(salary==0):
            logging.warning("salary cannot be zero")
        elif (salary<0):
            logging.error("salary cannot be a negative number")
        elif (salary>=50000):
            tax = 0.15*salary
            netsalary = salary-tax

        else:
            netsalary = salary
            print("No taxable Amount")
            logging.info("No taxable Amount")

    except Exception as exception:
        logging.exception("Exception occurred!!!! Enter numeric value",exception)

    return netsalary

def main():
    e_name = input("Enter the name of Employee \n")
    c_name = input("Enter the company name \n")
    salary = input("Enter the salary of Employee \n")
    start_time =(timeit.default_timer())
    netsalary = salary_calculator((salary))
    end_time =(timeit.default_timer())
    time_taken = (end_time - start_time)
    print('The net salary of' + e_name + " worked in " + c_name + " is",netsalary )
    logging.info("The net salary of  " + e_name + " worked in " + c_name + " is",netsalary )
    print(f"Function takes ", time_taken )

main()
