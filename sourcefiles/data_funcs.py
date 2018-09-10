def typecast(val):
    if val in ['TRUE','T']:
        return True
    elif val in ['FALSE','F']:
        return False
    else:
        try:
            return(int(val))
        except Exception:
            try:
                return(float(val))
            except Exception:
                return(val)

if __name__ == '__main__':
    pass