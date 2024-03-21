# import pandas as pd
# from validation import account_validation as validationLayer
# from testing import account_testing as testingLayer
import pandas as pd

def lambda_handler(event, context):
    print("test")
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.2')

    # if validationLayer.validateAcct(event['AcctNo']) == "Pass":
    #     print("Passed")

    # if testingLayer.testAcct(event['AcctNo']) == "Acct no is 10 characters":
    #     print("Passed")
  




