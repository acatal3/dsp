import pandas 
FB=pandas.read_csv('football.csv', index_col=0)
FB['GD'] = abs(FB["Goals"]-FB["Goals Allowed"])
team = FB['GD'].idxmin()
print team 
  
      
