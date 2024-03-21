import pandas as pd
import account_validation as validationLayer

def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.2')

    if validationLayer.validateAcct(event['AcctNo']) == "Pass":
        print("Passed")




