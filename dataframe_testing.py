from s3_util import S3Utility
from azure_util import AzureUtility
from data_util import DataUtility as util
from cloud_util import CloudUtility
import pandas as pd


if __name__ == "__main__":
    # grades = ["prime", "choice", "select", "no roll"]
    # result1 = util.deserialize_object("OffalPricing42924pdfparagraph.obj")

    object_files = ["BrandtBeefPricingMay2024pdf.obj", "Brandt_Beef_Pricing_April_(version_1)_(1)pdf.obj", "test_spreadpdf.obj", "OffalPricing42924pdf.obj", "910NegotiatedPriceListpdf.obj", "NBPPriceList_Apr_17_2024(2)pdf.obj" ,"FedBeefExternalPricelist(1)pdf.obj"]
    for obj in object_files:
        result = util.deserialize_object(obj)
        print(f"[ {obj} ]")
        print("====================================")
        for index in range(len(result.tables)):
            print("-----------------------------------")
            print(f"----------[   TABLE {index}   ]----------")
            df = util.get_improper_dataframe(result.tables[index])
            df = util.preprocess_df(df)
            df = util.set_row_as_headers(df, util.detect_category_column(df))
            df.reset_index(drop=True, inplace=True)
            pd.set_option('display.max_columns', None)  # Show all columns
            print(df.head(10))
            # print("Find any price column in here? ", util.find_in_rows(df, "price") or util.find_in_rows(df, "pricing") or util.find_in_rows(df, "FOB") or util.find_in_rows(df, "F.O.B."))
            # print("Find any meat grades in here?", util.find_grades(df))
            # print("Found array for grades:", util.get_grades(df))
            # print("The category column might be in ", util.detect_category_column(df))
            # print("I think the row to set columns to is ", util.set_row_as_headers(df))
            
            print("------------------------------------")
            
            

            print("---------------NEW------------------")
            
            columns_list = df.columns.tolist()
            print("List of columns:", columns_list)
            # df = util.preprocess_df(df)
            print(df.head(5))
            print("HELLO?? WTF")
            print("When I ask for the ONETH row I get:\n", df.iloc[1])
            print("---------------NEW------------------")
    print("====================================")
    
    # print("Find any meat grades in here?", util.find_grades(df))


    # result = util.deserialize_object("BrandtBeefPricingMay2024pdf.obj")
    # df = util.get_improper_dataframe(result.tables[1])
    # util.preprocess_df(df)
    # pd.set_option('display.max_columns', None)  # Show all columns
    # print(df.head(5))
    # util.find_in_rows(df, "price")
    
    # print("Find any meat grades in here?", util.find_grades(df))
    # print(df.head)
    
    # print(df.head)
    # print(len(result.paragraphs))

    # paragraphs = [paragraph.content for paragraph in result1.paragraphs]
    # util.find_in_paragraphs(paragraphs, "prime")
   
   
   
   
   
   
   
   
   
   
   
   
   
    # print(result)
    # print(result.tables[0])
    # util.print_raw_table(result.tables[1])
    # table = result.tables[1]
    # df = util.get_dataframe(table)
    # print(df)


    # df = util.get_improper_dataframe(result.tables[0])
    # df = df.drop(df.columns[:2], axis=1)
    # df = df.dropna()
    # df.columns = df.iloc[0]
    # df = df[1:]
    # df = df.reset_index(drop=True)
    # pd.set_option('display.max_columns', None)
    # print(df.head)
    # for col in df.columns:
    #     print(col)
    # print(df["Description"])

    # result = util.deserialize_object("test_spreadpdf.obj")
    
    # df = util.get_dataframe(result.tables[0])
    # for col in df.columns:
    #     print(col)