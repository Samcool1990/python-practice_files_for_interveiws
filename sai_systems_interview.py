# Sort a list wihout sort function
def sorting_algo(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


list1 = [5, 7, 9, 7, 6, 9, 4]
print(sorting_algo(list1))
# remove one elemnt from the sorted list


# http vs https


# 401         vs  403
#Unauthorized &  Forbidden access

# SELECT * FROM your_table
# ORDER BY your_column DESC
# LIMIT 1,6;

# git add .
# The git add command adds a change in the working directory to the staging area.
# git stash
# git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on
# something else, and then come back and re-apply them later on.
