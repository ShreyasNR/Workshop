def list_avg(L):
    try:
     s =  sum(L)/len(L)
    except TypeError:
        print('Not all elements are numeric')
    except ZeroDivisionError:
        print('Empty list')
    except:
        print('unknown error')
    return s
print(list_avg([21,6,8]))