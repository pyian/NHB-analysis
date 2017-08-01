import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def variation_per_day(df, col):
    df_hour = df.resample('H').mean()

    plt.figure(dpi=200)

    # iterate colour
    x = np.linspace(0, 1, 13)
    cmap = plt.get_cmap('tab20')
    i = 0

    for day in list(df_hour.index.day.unique()):
        df = df_hour[df_hour.index.day == day]
        color = cmap(x[i])
        plt.plot(df.index.hour, df[col],
                 '-o', color=color, label=day)
        i += 1
    # Turns off interactive mode (needs plt.show())
    plt.ioff()
    plt.legend(ncol=3)
    title = col + '_Variation_per_Day'
    plt.title(title)
    plt.xlabel('Hour')
    plt.ylabel('Strain (ue)')
    plt.xlim([0, 23])
    plt.savefig(title)
    plt.close()
    print('Figure saved as {}'.format(title + '.png'))


def plot_columns_variation_per_day(df):
    # get all columns from dataframe
    columns = df.columns
    # filter out 'Min' and 'Max'
    columns = [x for x in columns if 'Min' not in x and 'Max' not in x]
    i = 0

    for col in columns:
        if 'Min' not in col and 'Max' not in col:
            print('Plotting {}... {:.1f}%'.format(col, i+1/len(columns)*100))
            variation_per_day(df, col)
            i += 1


print('HI')
df = pd.read_pickle('all-df.p')
# plot all columns (except min and max) variation per day
plot_columns_variation_per_day(df)
