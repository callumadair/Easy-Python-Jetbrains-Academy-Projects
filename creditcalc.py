import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = vars(parser.parse_args())

arg_count = 0
for arg in args.values():
    if arg is not None:
        arg_count += 1

try:
    parameter_exception = Exception('Incorrect parameters.')
    if arg_count >= 4:
        loan_type = str(args['type'])
        annuity = float(args['payment']) if args['payment'] is not None else None
        principal = float(args['principal']) if args['principal'] is not None else None
        periods = int(args['periods']) if args['periods'] is not None else None
        interest = float(args['interest']) if args['interest'] is not None else None
        nom_int = interest / (12 * 100) if interest is not None else None
        total = None

        if loan_type == 'annuity':
            if annuity is None:
                annuity = math.ceil(
                    principal * ((nom_int * math.pow(1 + nom_int, periods)) / (math.pow(1 + nom_int, periods) - 1)))
                print('Your annuity payment = ' + str(annuity))

            elif principal is None:
                principal = math.floor(annuity / ((nom_int * math.pow(1 + nom_int, periods))
                                                  / (math.pow(1 + nom_int, periods) - 1)))
                print('Your loan principal = ' + str(principal))
            elif periods is None:
                periods = math.ceil(math.log((annuity / (annuity - nom_int * principal)), nom_int + 1))

                num_years = math.floor(periods / 12)
                num_months = periods - (num_years * 12)
                output = 'It will take '

                if num_years == 0:
                    output += str(num_months)
                else:
                    output += str(num_years) + ' year'
                    if num_years > 1:
                        output += 's'
                    if num_months != 0:
                        output += 'and ' + str(num_months) + ' month'
                        if num_months > 1:
                            output += 's'
                output += ' to repay this loan!'
                print(output)
            else:
                raise parameter_exception
            total = annuity * periods
        elif loan_type == 'diff' and annuity is None:
            print('diff')
            total = 0
            for m in range(1, periods + 1):
                cur_diff = math.ceil((principal / periods) + nom_int * (principal - ((principal * (m - 1)) / periods)))
                total += cur_diff
                print('Month ' + str(m) + ': payment is ' + str(cur_diff))
        else:
            raise parameter_exception
        if total is not None and principal is not None:
            overpayment = int(total - principal)
            print('Overpayment = ' + str(overpayment))
    else:
        raise parameter_exception
except Exception as e:
    print(str(e))
