def duration(x):
    d = int(x/86400)
    h = int((x%86400)/3600)
    m = int((x%3600)/60)
    s = int(x%60)
    print("Your input is equal to", d, "days,", h, "hours,", m, "minutes,", "and", s, "seconds.")
x = 5454666666

duration(x)