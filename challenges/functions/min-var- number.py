def custom_min_num(*args, low_limit=None):
    if low_limit is None:
        print(min(args))
    else:
        nums = [x for x in args if x >= low_limit]
        print(min(nums))


custom_min_num(1, 2, -5, 7, low_limit=1)
