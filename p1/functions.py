def get_requirements():

    print("\nProgram Requirements:\n"
          + "1. Run demo.py. \n"
          + "2. If errors, more than likely missing installations. \n"
          + "3. Research how to do the following installations: \n"
                + "a. pandas\n."
                + "b. pandas-datareader\n"
                + "c. matplotlib\n"
          + "4. Create at least 3 functions that are called by the program: \n"
                + "a. main() - calls the two other functions\n"
                + "b. get_requirements() - displays program requirements\n"
                + "c. data_analysis_1() - displays the following data\n")
    

def data_analysis_1():

    import datetime as dt
    import pandas_datareader as pdr
    import matplotlib.pyplot as plt
    from matplotlib import style


    start = dt.datetime(2010, 1, 1)

    end = dt.datetime.now()

    df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)

    print("\nPrint number of records: ")
    print(len(df))

    print("\nPrint columns: ")
    print(df.columns)

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first five lines: ")
    print(df.head())

    print("\nPrint last five lines: ")
    print(df.tail())

    print("\nPrint first 2 lines: ")
    print(df.head(2))

    print("\nPrint last 2 lines: ")
    print(df.tail(2))

    style.use('ggplot')

    df['DJIA'].plot()
    df['SP500'].plot()
    plt.legend()
    plt.show()