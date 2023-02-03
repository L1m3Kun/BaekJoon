def stars(n):
    if n == 1:
        # if input number is 1, returns just 1 star
        return ['*']
    # multi of 3 makes stars list
    num = n // 3
    # save func activation before as s
    s = stars(num)

    # makes new list for result
    star =[]
    # first line
    # saved stars * 3 append in star list
    for i in s:
        star.append(i*3)
    # second line
    # it takes blank in middle so append blanks as divided 3 between star lists
    for i in s:
        star.append(i + " " * num + i)

    # las line is equals first line
    for i in s:
        star.append(i*3)

    # return star list made of star lists
    return star

# input
N = int(input())

# for removing list symbol([])
s = stars(N)
for i in s:
    print(i)






#     num = n // 3
#
#
#
#     if n < 3:
#         top = t * n
#         mid = t + m * num + t
#         return top, mid
#     else:
#         top = t * num + "\n" + m * num + "\n" + t * num
#         mid = (t + " " * num + t) + "\n" + (m + " " * num + m) + "\n" + (t + " " * num + t)
#
#     stars(num, top, mid)
#
#     return top + "\n" + mid + "\n" + top
#
#
#
# st = "*"
# bl = " "
#
# # 3
# t = st * 3
# m = st + bl + st
#
# # 9
# def top(t, m):
#     return t  + "\n" + m  + "\n" + t
#
#
# top1 = t * 3 + "\n" + m * 3 + "\n" + t * 3
# mid1 = (t + " " * 3 + t) + "\n" + (m + " " * 3 + m) + "\n" + (t + " " * 3 + t)
# n = 9
# # 27
# print(stars(n, st, bl))



























# def star(n, st, bl):
#     num = n // 3
#     st = st * n
#     bl = st + bl + st
#     top_bottom = st + "\n" + bl * num + "\n" + st
#     midium = ""
#
#     if n < 3:
#         # return f'{"*" * n}\n{"* *" * (num)}\n{"*" * n}'
#         return st + "\n" + bl + "\n" +st
#     # result_fir = st * n +"\n"+ (st + bl + st) *num +"\n"+ st* n
#     # result_mid = (st * num + bl * num + st * num) + "\n" + ((st + bl + st)+" "*num + (st + bl + st) ) + "\n" + (st * num + bl * num + st * num)
#     # return result_fir + "\n" + result_mid + "\n" + result_fir
#     else:
#
#         midium = (st * num + bl * num + st * num) + "\n" + (bl+" "*num + bl) + "\n" + (st * num + bl * num + st * num) +"\n"+ top_bottom
#
#
#
#     star(num, st, bl)
#
#     return top_bottom + midium

#
#
# st = "*"
# bl = " "
# print(star(3, st, bl))