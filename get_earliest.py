def get_earliest(date1,date2):
    (a1,b1,c1) = date1.split("/")
    (a2,b2,c2) = date2.split("/")
    if (c1,a1,b1) > (c2,a2,b2):
        return date1
    else:
        return date2
    return 
result = get_earliest("06/21/1958", "06/24/1958")
print(result)

# def get_earliest(*dates):
#     """Return earliest of given MM/DD/YYYY-formatted date strings."""
#     def date_key(date):
#         (m, d, y) = date.split('/')
#         return (y, m, d)
#     return min(dates, key=date_key)