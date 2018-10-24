print("%0.1f" % sum(int(fields.split(',')[1]) * float(fields.split(',')[2])
          for fields in open("d:\\testdata\\stocks.csv")))