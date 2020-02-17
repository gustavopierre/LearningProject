import ffn
price = ffn.get('itsa4.sa,flry3.sa', start='2010-01-01')

stats = price.calc_stats()
stats.display()