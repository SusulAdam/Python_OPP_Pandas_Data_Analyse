import pandas as pd
from functools import reduce
import scipy.stats as stats


class AnalyzatorOfData:
    
    def __init__(self, _dataFrame):
        self._dataFrame= _dataFrame
    
    def __del__(self):
        print("objected delated")
   
    
    def get_dataFrame(self):
        self.getDataFrame= pd.read_excel(self._dataFrame)
        return self.getDataFrame
    
    def get_dropNa(self):
        self.getDataFrame= self.getDataFrame.dropna()
        return self.getDataFrame
    
    def get_count_column(self, num_col):
        self.count_column = len(self.getDataFrame.iloc[:, num_col])
        return print(f'Column {num_col} has {self.count_column} rows')
        
    def get_count_row(self, num_row):
        self.count_row = len(self.getDataFrame.iloc[num_row,:])
        return print(f'Row {num_row} has {self.count_row} columns')
    
    def get_column(self, col):
        self.getColumn = pd.DataFrame(self.getDataFrame.iloc[:, col])
        return self.getColumn
    
    def get_row(self, row):
        self.getRow = pd.DataFrame(self.getDataFrame.iloc[row, :])
        return self.getRow

    def sum_col_int(self, col):
        self.sum_col = reduce(lambda x1, x2: int(x1) +int(x2), self.get_column(col))
        return print(f'Sum of row: {col} is {self.sum_col}')
    
    def sum_col_str(self, col):
        self.sum_col = reduce(lambda x1, x2: str(x1) +str(x2), self.get_column(col))
        return print(f'Sum of row: {col} is {self.sum_col}')
    
    def get_mean_column(self, mean):
        self.mean = self.get_column(mean).mean()
        return print(f'Mean of column: {mean} is {self.mean}')
    
    def get_max_of_col(self, maxmium):
        self.maximum = self.get_column(maxmium).max()
        return print(f'Max of column: {maxmium} is {self.maximum }')
    
    def get_min_of_col(self, minimum):
        self.minimum = self.get_column(minimum).min()
        return print(f'Min of column: {minimum} is {self.minimum}')



class Diagrams(AnalyzatorOfData):
    
    
    def __init__(self, _dataFrame):
        super().__init__(_dataFrame)  
        
    def get_box_plot(self, col):
        self.box_plot= self.get_column(col)
        return self.box_plot.boxplot()
    
    def get_two_box_plot(self, boxplt_1, boxplt_2): 
        self.box_plot_2= self.getDataFrame.boxplot(column=[boxplt_1, boxplt_2])
        return self.box_plot_2
    
    
    def get_histogram(self, col):
        self.histogram= self.get_column(col)
        
        return self.histogram.hist()
    
    def get_plot_kde_two_factors(self, col, col2):
        self.first_kde=self.get_column(col)
        self.second_kde=self.get_column(col2)
        self.kdee = pd.concat([self.first_kde, self.second_kde], axis=1)
        return self.kdee.plot.kde()
    
    def get_plot_kde_third_factors(self, col, col2, col3):
        self.first_kde=self.get_column(col)
        self.second_kde=self.get_column(col2)
        self.third_kde=self.get_column(col3)
        self.kdee = pd.concat([self.first_kde, self.second_kde, self.third_kde], axis=1)
        return self.kdee.plot.kde()
    
    
class StatisticCalculation(AnalyzatorOfData):
    
    def __init__(self, _dataFrame):
        super().__init__(_dataFrame)
  
    def get_skew(self, skew):
        
        self.getSkew=self.get_column(skew).skew()
        return print(f"Skew: {self.getSkew}")
    
    def get_kurtosis(self, kurtosis):
        
        self.getKurtosis=self.get_column(kurtosis).kurtosis()
        
        return print(f"Kurtosis: {self.getKurtosis}")
        
        
class Statistic_analysis(AnalyzatorOfData):
        
        
   
    def __init__(self, _dataFrame):
        super().__init__(_dataFrame)
    
    def shapiro_Wilk_normality_test(self, col, col2):
        self.first_data = self.get_column(col)
        self.second_data = self.get_column(col2) 
        self.first_data_shapiro= stats.shapiro(self.first_data)
        self.second_data_shapiro= stats.shapiro(self.second_data)
        print('Shapiro-Wilk normality test')
        print(f'p for column: {col}: {self.first_data_shapiro}')
        print(f'p for column: {col2}: {self.second_data_shapiro}')
        
    def one_way_anova_test(self,col, col2):
        self.first_data = self.get_column(col)
        self.second_data = self.get_column(col2) 
        F, p = stats.f_oneway(self.first_data, self.second_data)
        print('F statistic = {} and probability p = {}'.format(F, p))
      
    def two_sided_test_for_the_null_hypothesis(self,col, col2):
        self.first_data = self.get_column(col)
        self.second_data = self.get_column(col2) 
        print(' apply ttest_indep()')
        t, p = stats.ttest_ind(self.first_data, self.second_data)
        print(f'{col} vs {col2}:', t, p)
        



#Basic Operation on Data Frame   
analyzator = AnalyzatorOfData('./data.xlsx')
analyzator.get_dataFrame()
analyzator.get_dropNa()
analyzator.get_count_column(2)
analyzator.get_count_row(1)
analyzator.sum_col_int(3)
#analyzator.sum_col_str()
analyzator.get_mean_column(3)
analyzator.get_max_of_col(3)
del analyzator
print()
print()


##Diagrams##
diagram = Diagrams('./data.xlsx')
diagram.get_dataFrame()
diagram.get_dropNa()
##Choose one of type boxplot##
diagram.get_box_plot(4)
#diagram.get_two_box_plot('Systolic pressure', 'Diastolic pressure')
diagram.get_histogram(3)
diagram.get_plot_kde_two_factors(5, 6)
diagram.get_plot_kde_third_factors(4,10,11)
print()
print()


##Statictic calculation##
statistic_calculation = StatisticCalculation('./data.xlsx')
statistic_calculation.get_dataFrame()
statistic_calculation.get_dropNa()
statistic_calculation.get_skew(4)
statistic_calculation.get_kurtosis(5)
print()
print()


## Sttistic anaylsis
statistic_analysis = Statistic_analysis('./data.xlsx')
statistic_analysis.get_dataFrame()
statistic_analysis.get_dropNa()
statistic_analysis.shapiro_Wilk_normality_test(6,7)
statistic_analysis.one_way_anova_test(6,7)
statistic_analysis.two_sided_test_for_the_null_hypothesis(6,7)

